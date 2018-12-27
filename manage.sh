#!/usr/bin/env bash
source venv/bin/activate
export PYTHONPATH=$PWD:$PYTHONPATH

export TOKEN=768289439:AAERK5Cj5RqyZ6yjbOcWOk-_lCTsW2o6OTU
export HOST=f3c67f50.ngrok.io

PROJECT_NAME=test

export DB_NAME=${PROJECT_NAME}_bot
export DB_USER=${PROJECT_NAME}_advbot
export DB_PASSWORD=${PROJECT_NAME}_11bot22
export DB_SERVER=localhost

python djtbot/manage.py $1 $2