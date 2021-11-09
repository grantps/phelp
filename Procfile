## The WEB_CONCURRENCY environment variable is automatically set by Heroku,
## based on the processes' Dyno size.
## This feature is intended to be a sane starting point for your application.
## We recommend knowing the memory requirements of your processes
## and setting this configuration variable accordingly.

## heroku config:set WEB_CONCURRENCY=3

## https://devcenter.heroku.com/articles/python-gunicorn

web: gunicorn phelp/run:app --workers $WEB_CONCURRENCY

