sudo cp -rf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf                  
sudo rm -rf /etc/nginx/sites-enabled/default                                    
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf      
sudo /etc/init.d/nginx restart
