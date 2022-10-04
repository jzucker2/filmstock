#!/bin/bash

echo "-----------"
# need to check if file exists!
rm /home/pi/Documents/filmstock/flaskapp.pid
echo "-----------"

exec /home/pi/.local/bin/gunicorn --pid /home/pi/Documents/filmstock/flaskapp.pid -c gunicorn.conf.py "app:create_app()"
