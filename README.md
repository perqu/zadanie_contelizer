## Zadanie rekrutacyjne Contelizer

## Docker-compose configuration

- `app`: Django app - Web server

## How to run the project

1. Clone the repository
2. convert .envexample to .env and update your data
3. Install docker (https://www.docker.com/get-started/)
4. Run `docker-compose up --build`
5. Open http://localhost:8888/text/ in your browser to see task1
6. Open http://localhost:8888/pesel/ in your browser to see task2

## Tests

1. Run `docker-compose up --build`
2. Run `docker exec -it 'dockerid' /bin/bash`
3. Run `python manage.py test`

To check docker container id run `docker ps`

## Warnings

Task1 - Words connected to a character that is not a letter will not be shuffled because they are not a valid word
