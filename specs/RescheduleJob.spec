RescheduleJob
=============

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline" - setup
* With "1" live agents in directory "RescheduleJob" - setup
* Capture go state "RescheduleJob" - setup

RescheduleJob
-------------

tags: 1995, 2126, 2126, automate

* Looking at pipeline "basic-pipeline"
* Trigger pipeline

* Wait for agent to show status "building"

* Kill all agents
* Restart all agents

* Wait for first stage to pass with pipeline label "1"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "Start to build basic-pipeline" twice





Teardown of contexts
* Capture go state "RescheduleJob" - teardown
* With "1" live agents in directory "RescheduleJob" - teardown
* Using pipeline "basic-pipeline" - teardown
* Basic configuration - teardown


