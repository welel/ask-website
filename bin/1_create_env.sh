#!/bin/bash
sudo apt update                                                                                                 
sudo apt install python3.5                                                                                      
sudo apt install python3.5-dev                                                                                  
sudo unlink /usr/bin/python3                                                                                    sudo ln -s /usr/bin/python3.5 /usr/bin/python3                                                                  virtualenv -p /usr/bin/python3 ../env 
#virtualenv ../env
source ./../env/bin/activate
pip install gunicorn
pip install django==2.0
pip install mysqlclient
deactivate
