# IDP Library Autohrization Service

## Endpoints

### POST localhost:8089/register

Register a new user. Expects the following body:

```json
{
    "username": "username",
    "password": "password",
    "email": "email@mail.com"
}
```

### POST localhost:8089/login

Login a user. Expects the following body

```json
{
    "username": "username",
    "password": "password"
}
```

Will return a JWT token (which expires in 2 hours from the last login) that can be used to authorize operations:

```json
{
    "token": "fake_token"
}
```

### GET localhost:8089/authorize

Authorizes an user to perform operations. expects an authorization header with the token received from the login:

```Authorization: Bearer <token>```

Will return a 200 if the token is valid and the user data, 401 otherwise.


Successfull response:
```json
{
    "isAuthorized": true,
    "userId": 12345,
    "username": "username",
}
```

Failed response:
```json
{
    "isAuthorized": false
}
```


