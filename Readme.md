# Literally just an RPG item list from Redis
Simple Project to merge some tech and to testdrive Copilot (Works great!):
- Front-end: [Vue.js](https://vuejs.org/)
- API: [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- Database: [Redis](https://redis.io/docs/stack/json/)
- Copilot <3: [Copilot](https://copilot.github.com/)

And also running them inside Docker containers.

## How to run

Just compose it and run it. If changes are made, make sure to add the `--build` flag in order to rebuild the images.

``` 
docker-compose up
```

## Accessing the apps

The Vue app runs in https://localhost:8080.

The Flask API runs in https://localhost:5000.

## Accessing Redis
Redis can be accessed by the following command:
```
docker exec -ti vuetesting_redis_1 redis-cli
```

The only key stored so far is *items*. It can be accessed by the following command:
```
JSON.GET items
```
