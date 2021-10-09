#!/bin/bash

cd /home/repl

# Wait for flask-server to be up and running
until nc -vz localhost 5000; do
    echo "no connection"
    sleep 0.1
done

# Wait for Airflow server to be up and running
until nc -vz localhost 3010; do
    echo "no connection"
    sleep 0.1
done

# Wait for GoTTY to be up and running
until nc -vz localhost 3010; do
    echo "no connection"
    sleep 0.1
done
