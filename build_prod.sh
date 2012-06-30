#!/bin/bash

export PROJECT_NAME=pycon
export INSTANCE_TYPE=prod
export FCGI_PORT=7890
export DOMAIN=unomena.net

export SERVER_NAME=$PROJECT_NAME.$INSTANCE_TYPE.$DOMAIN
export SERVER_NAMES="$SERVER_NAME pycon.org.za"

./build_common.sh