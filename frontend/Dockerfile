FROM node:12

WORKDIR /src

COPY package.json package.json
COPY yarn.lock yarn.lock
RUN yarn install

COPY . .

EXPOSE 3000
CMD yarn start
