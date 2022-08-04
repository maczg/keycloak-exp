#!/bin/sh

NAMESERVER=$(cat /etc/resolv.conf | grep nameserver | head -n 1 | cut -f2 -d' ')
nginx -g daemon off;