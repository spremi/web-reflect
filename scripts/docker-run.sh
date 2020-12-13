#!/bin/bash
#
# web-reflect
#
# Copyright (c) 2020, Sanjeev Premi.
#

docker run --publish 5500:5500 --detach --name web-reflect web-reflect:latest

ret=${?}

[ ${ret} -eq 0 ] && echo "web-reflect is running :)" || echo "web-reflect is not running :("
