#! /usr/bin/bash

VIRTUALENV_PATH="/home/souchela/"
VIRTUALENV_ACTIVE=${VIRTUALENV_PATH}bin/activate

UWSGI_PID_FILE="uwsgi.pid"


# Activate python virtual environment.
echo "Activating python virtual environment..."
source $VIRTUALENV_ACTIVE && echo "python virtual environment activated!"

# Stop old uwsgi process.
echo "Stoping old uwsgi process..."
kill -9 `cat ${UWSGI_PID_FILE}` && echo "uwsgi stopped!"

# Start new uwsgi process
echo "Starting uwsgi process..."
uwsgi --ini souchela_uwsgi.ini && echo "uwsgi started!"


sleep 3
# Check if uwsgi is running on port 8888
netstat -nlp | grep 8888
