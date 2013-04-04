#!/bin/sh

msg="No parameters at all!"
if [ "$1" != "" ]; then
    msg=$1
fi

echo $msg