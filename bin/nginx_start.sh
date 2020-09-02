#!/bin/bash

exec sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default      
#exec sudo ln -sf /home/pavel/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

exec sudo service nginx restart
