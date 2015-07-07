#!/bin/bash

echo "Processes before attemping kill"
pgrep -u `whoami` -f go.jar
pgrep -u `whoami` -f firefox


echo "Killing........."
pkill -u `whoami` -f go.jar
pkill -u `whoami` -f firefox
sleep 3
pkill -9 -u `whoami` -f go.jar
pkill -9 -u `whoami` -f firefox

echo "Processes left behind after attempting kill"
pgrep -u `whoami` -f go.jar
pgrep -u `whoami` -f firefox

echo "Thanking you,"
echo "Yours faithfully"
echo "Kill Bill"
exit 0