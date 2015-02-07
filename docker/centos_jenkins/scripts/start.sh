#!/bin/bash
# Starts up Jenkins within the container.

# Stop on error
set -e

LIB_DIR=/var/lib/jenkins
LOG_DIR=/var/log
CACHE_DIR=/var/cache/jenkins/war

mkdir -p $LIB_DIR
mkdir -p $CACHE_DIR
mkdir -p "$LOG_DIR/jenkins"

chown -R jenkins:jenkins $LIB_DIR
chown -R jenkins:jenkins $CACHE_DIR
chown -R jenkins:jenkins "$LOG_DIR/jenkins"

echo "Starting Jenkins..."
/etc/init.d/jenkins start
