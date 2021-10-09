#!/bin/bash

# Update base_url Airflow config when the user session starts
sed -i "s/base_url.*/base_url = http:\/\/localhost:3000\/proxy\/absolute\/$PROXYTOKEN\/airflow/g" /home/repl/airflow/airflow.cfg
