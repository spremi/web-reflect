#!/bin/bash
#
# web-reflect
#
# Copyright (c) 2020, Sanjeev Premi.
#

port=5500

#
# Use CURL with plain text
#
curl_plain () {
    local method=${1}
    local route=${2}

    printf "\n:: %-6s (TEXT) %6s\n" ${method} ${route}

    curl -X ${method} \
        -H "Content-Type: text/plain" \
        -w "\n%{http_code}\n" \
        -d "Hello" \
        http://localhost:${port}${route}
}

#
# Use CURL with json data
#
curl_json () {
    local method=${1}
    local route=${2}

    printf "\n:: %-6s (JSON) %6s\n" ${method} ${route}

    curl -X ${method} \
        -H "Content-Type: application/json" \
        -w "\n%{http_code}\n" \
        -d '{"name":"abc","email":"abc@def.com"}' \
        http://localhost:${port}${route}
}

echo "::"
echo ":: Testing web-reflect"
echo "::"
echo " : Using port ${port}"
echo "::"

#
# GET
#
curl_plain  GET     /api/s
curl_plain  GET     /api/e

curl_plain  GET     /api/s?a=b'&'c=d

curl_json   GET     /api/s
curl_json   GET     /api/e

curl_json   GET     /api/s?a=b'&'c=d

#
# POST
#
curl_plain  POST    /api/s
curl_plain  POST    /api/e

curl_plain  POST    /api/s?a=b'&'c=d

curl_json   POST    /api/s
curl_json   POST    /api/e

curl_json   POST    /api/s?a=b'&'c=d

#
# PUT
#
curl_plain  PUT     /api/s
curl_plain  PUT     /api/e

curl_plain  PUT     /api/s?a=b'&'c=d

curl_json   PUT     /api/s
curl_json   PUT     /api/e

curl_json   PUT     /api/s?a=b'&'c=d

#
# DELETE
#
curl_plain  DELETE  /api/s
curl_plain  DELETE  /api/e

curl_plain  DELETE  /api/s?a=b'&'c=d

curl_json   DELETE  /api/s
curl_json   DELETE  /api/e

curl_json   DELETE  /api/s?a=b'&'c=d
