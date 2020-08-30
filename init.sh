sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default      
#sudo ln -sf /home/pavel/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf

sudo service nginx restart
gunicorn -c etc/gunicorn.conf.py hello:application

