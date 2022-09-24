#!/bin/sh

echo "Set up the DB!"
echo "Going with DB_LOCATION ---> $DB_LOCATION"

# check for db first
rm app/app.db
echo "Done deleting (or checking) for /app.db"

# should probably call `set_up_db.sh` instead of copypasta
echo "First perform flask migrations"
flask db upgrade
echo "Now ensure default admin"
python ensure_admin.py

echo "Done setting up the $DB_LOCATION db!!!"
