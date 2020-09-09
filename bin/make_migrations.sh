#!/bin/bash
source ./../env/bin/activate
$PWD/../ask/manage.py makemigrations
$PWD/../ask/manage.py migrate
deactivate
