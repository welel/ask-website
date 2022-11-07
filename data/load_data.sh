#!/bin/bash
python ../ask/manage.py loaddata ../data/users.json
python ../ask/manage.py loaddata ../data/questions.json
python ../ask/manage.py loaddata ../data/answers.json