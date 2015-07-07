#!/bin/bash

HERE=$PWD
CRUISE=../..

for agent_folder in `ls -d $CRUISE/target/twist-agents/*`
do
  echo "Cleaning up agent at $agent_folder..."
  if [ -e $agent_folder/cruise-agent.pid ]; then
    cd $agent_folder
    bash stop-agent.sh
    cd -
  fi
  rm -rf $agent_folder
done

echo "Done."

