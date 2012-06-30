#!/bin/bash

export PROJECT_NAME=pycon
export INSTANCE_TYPE=qa
export FCGI_PORT=7892
export DOMAIN=unomena.net

export SERVER_NAME=$PROJECT_NAME.$INSTANCE_TYPE.$DOMAIN
export SERVER_NAMES="$SERVER_NAME"

./build_common.sh