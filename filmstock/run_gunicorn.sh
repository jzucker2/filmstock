#!/bin/bash

echo "-----------"
# need to check if file exists!
rm /home/pi/Documents/filmstock/flaskapp.pid
echo "-----------"

exec /home/pi/.local/bin/gunicorn --pid /home/pi/Documents/filmstock/flaskapp.pid -w 1 --bind 0.0.0.0:1915 "app:create_app()"
