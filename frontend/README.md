# Front-end setup

This front-end contains a basic React app which displays a list of clinicians.

## Installing requirements

```
yarn install
```

or

```
npm install
```

## Run server

```
yarn start
```

or

```
npm run start
```

## Communicating with the API

For an example, see `fetchClinicians` in `frontend/src/requests.js`

The url of the backend server is defined by the `proxy` field in `package.json`. It defaults to `localhost:8000`.