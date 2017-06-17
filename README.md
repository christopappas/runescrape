# runescrape

Django app for mining hiscores from OSRS highscores and putting it in a DB

## Developer Setup

COMING SOON...

## Deploying

This app runs asyncronous tasks using celery and rabbitmq. A very informal deployment includes 3 shells open, 1 with the Django app running, another with the broker (rabbitmq), and another with celery running.

With rabbitmq installed, you should be able to get it running with something like:

```
$ rabbitmq-server
```

With celery installed, you should be able to get the celery workers running with something like:

```
$ celery -A runescrape worker --loglevel=info
```
