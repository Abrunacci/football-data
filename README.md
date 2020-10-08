# Football-Data Test
API that imports and expose football data obtained from football-data.org

## How to run?


### Prerequisites:

    - Docker: [installation guides](https://docs.docker.com/get-docker/)
    - Docker-compose: [installation guides](https://docs.docker.com/compose/install/)

### Build and run:

Go to the root folder of this project and run:

```docker-compose build --no-cache```

Once the process is finished run:

```docker-compose up```

You can now open a navigator and go to:

http://localhost:8000/docs

and test the API from the swagger.

# NOTE:
If you have an API-key for football-data.org, you must change the value of `EXTERNAL_API_TOKEN` inside the file `.docker/development/env/public`. Otherwise the import of players will be affected by football-data.org restrictions.