#!/bin/bash
#
# web-reflect
#
# Copyright (c) 2020, Sanjeev Premi.
#

docker build --force-rm --no-cache -t web-reflect .

ret=${?}

[ ${ret} -eq 0 ] && docker image ls || echo "Docker build failed :("
