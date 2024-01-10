const express = require('express');
const bodyParser = require('body-parser');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcrypt');
const { Pool } = require('pg');

const app = express();

const PORT = 8089;
const SALT_ROUNDS = 10
const JWT_SECRET = process.env.JWT_SECRET;

const pool = new Pool({
  user: process.env.PGUSER,
  host: process.env.PGHOST,
  database: process.env.PGDATABASE,
  password: process.env.PGPASSWORD,
  port: 5432,
});

app.use(bodyParser.json());

app.post('/register', (req, res) => {
  const { username, password, email } = req.body;
  pool.query('SELECT * FROM users WHERE username = $1 OR email = $2', [username, email], (error, result) => {
    if (error) {
      console.error(error);
      return res.status(500).json({ message: 'Server error' });
    }

    if (result.rows.length > 0) {
      return res.status(401).json({ message: 'User or email already used' });
    }
  });

  bcrypt.hash(password, SALT_ROUNDS, function(err, hash) {
    if (err) {
      return res.status(500).json({ message: err.message });
    }

    const query = {
      text: 'INSERT INTO users(username, password, email) VALUES($1, $2, $3)',
      values: [username, hash, email],
    };

    pool
      .query(query)
      .then(() => {
        console.log(`User ${username} created successfully`);
        res.status(201).json({ message: 'User created successfully' })
      })
      .catch((err) => {
        console.log(err)
        res.status(500).json({ message: err.message })
      });
  });
});

app.post('/login', (req, res) => {
  const { username, password } = req.body;

  pool.query('SELECT * FROM users WHERE username = $1', [username], (error, result) => {
    if (error) {
      console.error(error);
      return res.status(500).json({ message: 'Server error' });
    }

    const user = result.rows[0];

    if (!user) {
      return res.status(401).json({ message: 'Incorrect credentials' });
    }

    bcrypt.compare(password, user.password, function(err, result) {
      if (err || result === false) {
        return res.status(401).json({ message: 'Incorrect credentials' });
      }

      const token = jwt.sign(
        { userId: user.id, username: user.username },
        JWT_SECRET,
        { expiresIn: '2h' }
      );
        
      console.log(`User ${username} logged in successfully`)
      res.json({ token });
    });
  });
});

app.get('/authorize', (req, res) => {
  const token = req.headers.authorization?.split(' ')[1];

  if (!token) {
    return res.status(401).json({ isAuthorized: false });
  }

  jwt.verify(token, JWT_SECRET, (err, decoded) => {
    if (err) {
      return res.status(401).json({ isAuthorized: false });
    }

    res.status(200).json({ isAuthorized: true, userId: decoded.userId, username: decoded.username });
  });
});

app.listen(PORT, () => {
  console.log(`Server started on port ${PORT}`);
});