#!/bin/sh

esh -o /etc/nginx/conf.d/default.conf /etc/nginx/default.conf.esh
exec nginx -g 'daemon off;'