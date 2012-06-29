#!/bin/bash

python bootstrap.py
bin/buildout buildout:newest=true buildout:server-names="geodb.qa.unomena.net geodb.qa.praekelt.com" buildout:server-name=geodb.qa.unomena.net buildout:fcgi-port=7882

sudo chmod -R 777 logs

bin/django syncdb
bin/django evolve --execute --noinput

sudo rm /etc/nginx/sites-available/geodb_qa.conf
sudo ln -s $PWD/nginx/geodb.qa.unomena.net.conf /etc/nginx/sites-available/geodb_qa.conf
sudo rm /etc/nginx/sites-enabled/geodb_qa.conf
sudo ln -s /etc/nginx/sites-available/geodb_qa.conf /etc/nginx/sites-enabled/geodb_qa.conf

sudo bin/django.fcgi restart
sudo service nginx restart
sudo service memcached restart
