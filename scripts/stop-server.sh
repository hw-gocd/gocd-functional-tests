#!/bin/bash

HERE=$PWD
CRUISE=../../
SERVER_DIR=$CRUISE/target/go-server*

echo "Stopping server...
cd $SERVER_DIR
bash stop-server.sh

echo "Done."
