PIpelineLockingOnDashboard
==========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "pipeline-with-lock-all-manual" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "PIpelineLockingOnDashboard" - setup

PIpelineLockingOnDashboard
--------------------------

tags: pipeline-dashboard, #3740

* Looking at pipeline "pipeline-with-lock-all-manual"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Verify the lock status is "locked" - On Pipeline Dashboard Page
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Verify stage "1" is "Passed" on pipeline with label "1"
* Verify the lock status is "click_to_unlock" - On Pipeline Dashboard Page

* Unlock the pipeline - On Pipeline Dashboard Page

* Looking at pipeline "pipeline-with-lock-all-manual"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "2"
* Verify the lock status is "locked" - On Pipeline Dashboard Page
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Verify stage "1" is "Passed" on pipeline with label "2"
* Verify the lock status is "click_to_unlock" - On Pipeline Dashboard Page

* Unlock the pipeline - On Pipeline Dashboard Page
* Click on pipeline name

* Approve stage "stage-2" with label "2"

* Verify stage "2" is "Building" on pipeline with label "2"
* Verify the lock status is "locked" - On Pipeline Dashboard Page
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Verify stage "2" is "Passed" on pipeline with label "2"




Teardown of contexts 
* Capture go state "PIpelineLockingOnDashboard" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "pipeline-with-lock-all-manual" - teardown
* Basic configuration - teardown


