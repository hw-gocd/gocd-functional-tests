## Pre-Requisites
* Maven
* [Brew Cask](http://caskroom.io)
* [Gauge](http://getgauge.io)

## Setup
* ``` git clone``` as a sibling directory to
  [go.cd](http://github.com/gocd/gocd)
* ```$ cd gocd-functional-tests```l
* ```$ brew cask install firefox```
* ```$ gauge --install java```
* ```$ gauge --install html-report```
* ```$ mvn validate```

## Prepare
* cd to ```gocd``` codebase, run : ```$ ./bn clean
  cruise:prepare dist ALLOW_NON_PRODUCTION_CODE=yes```
* cd to ```gocd-functional-tests``` and run : ```$ ./b clean setup```
* ```./b start_server``` 

## Running tests

* ```gauge specs/AdminTaskListing.spec```
