#!/bin/bash

gnome-terminal -e cd medicalDatabase
python3.6 manage.py runserver
echo "Hey"
$SHELL