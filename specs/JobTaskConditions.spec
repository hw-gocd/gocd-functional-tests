JobTaskConditions
=================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "pipeline-with-runif" - setup
* With "1" live agents in directory "AgentsUIScreen" - setup
* Capture go state "JobTaskConditions" - setup

JobTaskConditions
-----------------

tags: 2318, runif, automate


* Trigger pipeline
* Verify stage "1" is "Failed" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "job-with-runif"

First task fails, second task is runif pass, third task is runif failed and the fourth is runif all.
* Open console tab
* Verify console contains "Build failed"
* Verify console does not contain "Sleeping for 30 seconds so you can see the build in the new dashboard"
* Verify console contains "Sleeping for 6 seconds so you can see the build in the new dashboard"
* Verify console contains "Echoing a message"




Teardown of contexts 
* Capture go state "JobTaskConditions" - teardown
* With "1" live agents in directory "AgentsUIScreen" - teardown
* Using pipeline "pipeline-with-runif" - teardown
* Basic configuration - teardown


