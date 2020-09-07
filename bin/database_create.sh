#!/bin/bash
source ./.env
sudo /etc/init.d/mysql start
sudo mysql -uroot -e "create user '$USER'@'localhost' identified by '$DATABASE_PASSWORD';"
sudo mysql -uroot -e "create database ask;"
sudo mysql -uroot -e "grant all privileges on ask.* to '$USER'@'localhost' with grant option;"
