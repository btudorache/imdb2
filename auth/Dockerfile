FROM node:14

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8089

ADD init.sql /docker-entrypoint-initdb.d

CMD [ "node", "index.js" ]
