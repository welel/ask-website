#!/bin/bash
sudo ln -sf $PWD/../etc/nginx.conf /etc/nginx/sites-enabled/ask.conf
sudo service nginx restart
