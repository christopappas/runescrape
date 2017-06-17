# runescrape

Django app for mining hiscores from OSRS highscores and putting it in a DB

## Developer Setup (Mac)

To set up your local checkout do the following:

```
# Clone the repo
$ git clone git@github.com:christopappas/runescrape.git
$ cd runescrape

# Create and activate your virtual environment
$ virtualenv ve --prompt="(Runescape)"
$ . ve/bin/activate

# Install requirements
$ pip install -r requirements/base.txt
$ pip install -r requirements/test.txt 

# Run Tests!
$ python ./manage.py test
```

You should now have a development environment setup suitable to get going.

## Deploying

This app is intended to run asyncronous tasks using celery and rabbitmq. A very informal deployment includes 3 shells open, 1 with the Django app running, another with the broker (rabbitmq), and another with celery running.

With rabbitmq installed, you should be able to get it running with something like:

```
$ rabbitmq-server
```

With celery installed, you should be able to get the celery workers running with something like:

```
$ celery -A runescrape worker --loglevel=info
```
