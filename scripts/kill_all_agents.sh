#!/bin/bash
ps aux | grep agent.jar | grep -v grep | grep -v go.jar | awk '{print $2}' | xargs kill -9
ps aux | grep agent-bootstrapper.jar | grep -v grep | grep -v go.jar | awk '{print $2}' | xargs kill -9
