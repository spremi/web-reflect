#
# Base image
#
FROM alpine:3.12.2

#
# It appears that LANG=C is not compatible with Python3.
#
ENV LANG C.UTF-8

#
# Install run-time dependencies
#
RUN apk add --no-cache ca-certificates
RUN apk add --no-cache tzdata
RUN apk add --no-cache python3
RUN apk add --no-cache curl

#
# Create directory for 'recrepo'
#
ENV WEB_REFLECT_DIR /usr/local/recrepo

RUN mkdir -p ${WEB_REFLECT_DIR}/content

#
# Copy contents to 'recrepo'
#
COPY reflect/app.py               ${WEB_REFLECT_DIR}/.

COPY reflect/content/favicon.png  ${WEB_REFLECT_DIR}/content/.
COPY reflect/content/index.html   ${WEB_REFLECT_DIR}/content/.
COPY reflect/content/error.html   ${WEB_REFLECT_DIR}/content/.
COPY reflect/content/style.css    ${WEB_REFLECT_DIR}/content/.

#
# Expose the port used by the application.
#
EXPOSE 5500

#
# Start the server on 0.0.0.0 for port-forwarding to work.
#
WORKDIR ${WEB_REFLECT_DIR}

CMD ["python3", "app.py", "--bind",  "0.0.0.0"]
