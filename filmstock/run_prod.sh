#!/bin/sh

gunicorn -w 2 -b 0.0.0.0:1927 "app:create_app()"
