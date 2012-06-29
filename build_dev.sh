#!/bin/bash

PROJECT_NAME = pycon
PROJECT_TYPE = dev

python bootstrap.py
bin/buildout \
    buildout:server-names="$PROJECT_NAME.$PROJECT_TYPE.unomena.net" \
    buildout:server-name=$PROJECT_NAME.$PROJECT_TYPE.unomena.net \
    buildout:fcgi-port=7891

sudo chmod -R 777 logs

bin/django syncdb
bin/django evolve --execute --noinput

sudo rm /etc/nginx/sites-available/$PROJECT_NAME_$PROJECT_TYPE.conf
sudo ln -s $PWD/nginx/$PROJECT_NAME.$PROJECT_TYPE.unomena.net.conf /etc/nginx/sites-available/$PROJECT_NAME_$PROJECT_TYPE.conf
sudo rm /etc/nginx/sites-enabled/$PROJECT_NAME_$PROJECT_TYPE.conf
sudo ln -s /etc/nginx/sites-available/$PROJECT_NAME_$PROJECT_TYPE.conf /etc/nginx/sites-enabled/$PROJECT_NAME_$PROJECT_TYPE.conf

sudo bin/django.fcgi restart
sudo service nginx restart
sudo service memcached restart