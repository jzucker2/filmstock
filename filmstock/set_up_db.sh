#!/bin/sh

echo "Set up the DB!"
echo "Going with DB_LOCATION ---> $DB_LOCATION"

echo "First perform flask migrations"
flask db upgrade
echo "Now ensure default admin"
python ensure_admin.py

echo "Done setting up the $DB_LOCATION db!!!"
