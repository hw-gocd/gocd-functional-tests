StageDetailsForPipelineLock
===========================

Setup of contexts
* Basic configuration - setup
* Using pipeline "pipeline-with-lock-all-manual" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "StageDetailsForPipelineLock" - setup

StageDetailsForPipelineLock
---------------------------

tags: stage-details, automate, pipeline-locking, 3659

* Looking at pipeline "pipeline-with-lock-all-manual"
* Trigger pipeline
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Wait for stage "stage-1" status to be "Passed" with label "1"
* Navigate to stage "stage-1" of run "1" having counter "1"

* Verify the lock status is "Click to unlock"
* Unlock the pipeline
* Verify the lock status is "UNLOCKED"

* Looking at pipeline "pipeline-with-lock-all-manual"
* Trigger pipeline
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Wait for stage "stage-1" status to be "Passed" with label "2"
* Navigate directly to stage "stage-1" of run "1" having counter "1"

* Verify the lock status is "Locked by 2"

* Looking at pipeline "pipeline-with-lock-all-manual"
* Navigate to stage "stage-1" of run "2" having counter "1"

* Rerun stage "stage-1"
* Verify the lock status is "LOCKED"





Teardown of contexts
* Capture go state "StageDetailsForPipelineLock" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "pipeline-with-lock-all-manual" - teardown
* Basic configuration - teardown


