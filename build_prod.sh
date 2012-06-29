#!/bin/bash

python bootstrap.py
bin/buildout buildout:newest=true buildout:server-names="geodb.unomena.com geodb.com www.geodb.com" buildout:server-name=geodb.com buildout:fcgi-port=7884

sudo chmod -R 777 logs

bin/django syncdb
bin/django evolve --execute --noinput

sudo chmod -R 777 logs

sudo rm /etc/nginx/sites-available/geodb.conf
sudo ln -s $PWD/nginx/geodb.com.conf /etc/nginx/sites-available/geodb.conf
sudo rm /etc/nginx/sites-enabled/geodb.conf
sudo ln -s /etc/nginx/sites-available/geodb.conf /etc/nginx/sites-enabled/geodb.conf

sudo bin/django.fcgi restart
sudo service nginx restart
sudo service memcached restart
