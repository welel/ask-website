sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default      
#sudo rm /etc/nginx/sites-enabled/test.conf
#sudo ln -s /home/pavel/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo service nginx restart
gunicorn -c hello.py hello:application

