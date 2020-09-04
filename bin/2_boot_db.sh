#!/bin/bash
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create database ask;"
sudo mysql -uroot -e "grant all privileges on *.* to 'box'@'localhost' with grant option;"
#~/web/ask/manage.py makemigrations
#~/web/ask/manage.py migrate
