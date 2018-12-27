#!/usr/bin/env bash
source venv/bin/activate
export PYTHONPATH=$PWD:$PYTHONPATH
export DEBUG=False
export TOKEN=768289439:AAERK5Cj5RqyZ6yjbOcWOk-_lCTsW2o6OTU
export HOST=''
export LMS_ALLOWED_HOSTS="[\"localhost\"]"
PROJECT_NAME=test
export LMS_DB_NAME=elms_${PROJECT_NAME}_bot
export LMS_DB_USER=${PROJECT_NAME}_advbot
export LMS_DB_PASSWORD=${PROJECT_NAME}_11bot22
export LMS_DB_SERVER=localhost
python djbot/manage.py $1 $2