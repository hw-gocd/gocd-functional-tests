StageLocking
============

Setup of contexts
* Basic configuration - setup
* Using pipeline "pipeline-with-lock" - setup
* With "1" live agents in directory "StageLocking" - setup
* Capture go state "StageLocking" - setup

StageLocking
------------

tags: 3249, stage-locking, timer, automate

* Looking at pipeline "pipeline-with-lock"
* Trigger pipeline
* Wait for stage "stage-1" status to be "Passed" with label "1"

* For pipeline "pipeline-with-lock" - Using pipeline api
* Schedule should return code "409"

* Looking at pipeline "pipeline-with-lock"
* Wait for stage "stage-2" status to be "Passed" with label "1"

* For pipeline "pipeline-with-lock" - Using pipeline api
* Schedule should return code "202"








Teardown of contexts
* Capture go state "StageLocking" - teardown
* With "1" live agents in directory "StageLocking" - teardown
* Using pipeline "pipeline-with-lock" - teardown
* Basic configuration - teardown


