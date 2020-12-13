# web-reflect

This is a simple server that echoes / **reflects** back any HTTP request back
to the caller.

## Features

1. A standalone server with no additional dependencies.
1. Distinct endpoints ``/api/s`` and ``/api/e`` for **success** and **error**
   responses respectively.
   - Payload can be **plain text** or **json**.
   - Payload is included in *success* responses.
   - The response contains additional information that can be used for debug.
1. Parses query parameters.
1. Supports GET, POST, PUT, DELETE and **OPTIONS**.
1. Support for CORS.
1. Includes a **success** (*default*) and **error** page for browsers.
   - Error page is shown for all pages - other than the default index.
1. Can be readily deployed as **docker container**.
   - Includes scripts to build and run the container.
1. Includes a test script to quickly view all responses.

Screenshots &amp; examples can be viewed **[HERE](docs/examples.md)**.

## Deploy

To run the application without customization:
```console
$ cd reflect
$ python app.py
```
Here is complete list of parameters:
```console
$ python app.py -h
usage: app.py [-h] [-b BIND] [-p PORT] [-c] [-d]

web-reflect: A simple HTTP reflect server.

optional arguments:
  -h, --help            show this help message and exit
  -b BIND, --bind BIND  Host name/address to bind.
  -p PORT, --port PORT  Port to listen.
  -c, --cors            Enable CORS.
  -d, --debug           Show debug messages.
```
Currently, option ``-d`` is unused.

## Deploy with Docker

The commands below are available as individual bash scripts in the 'scripts'
directory:
- ``docker-bld.sh`` to build the docker image.
- ``docker-run.sh`` to launch the docker image.
- ``docker-shell.sh`` to open interactive shell in running container.

### Build docker image
```console
$ docker build --force-rm --no-cache -t web-reflect .
$ docker image ls
REPOSITORY             TAG        IMAGE ID       CREATED              SIZE
web-reflect            latest     c83xxxxxx2d3   About a minute ago   51.9MB
```

### Run the image
```console
$ docker run --publish 5500:5500 --detach --name web-reflect web-reflect:latest
```
As necessary, the image can be stopped and started.
```console
$ docker stop web-reflect
$ docker start web-reflect
```

## License
BSD-3-Clause Copyright [Sanjeev Premi](https://github.com/spremi)
