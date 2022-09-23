#!/bin/sh

gunicorn -w 2 -b 0.0.0.0:1915 "app:create_app()"
