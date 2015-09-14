StageDetailsJobTab
==================

Setup of contexts
* Basic configuration - setup
* Using pipeline "pipeline-with-3-jobs" - setup
* With "3" live agents in directory "StageDetails" - setup
* Capture go state "StageDetailsJobTab" - setup

StageDetailsJobTab
------------------

tags: 3609, stage-details, automate

* Looking at pipeline "pipeline-with-3-jobs"
* Trigger pipeline
* Verify stage "1" is "Failing" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Go to jobs tab

* Verify "first" ends with state "Building" and result "Active"
* Verify "second" ends with state "Completed" and result "Failed"
* Verify "third" ends with state "Completed" and result "Passed"
* Stop "1" jobs waiting for file
* Verify "first" ends with state "Completed" and result "Passed"
* Verify "second" ends with state "Completed" and result "Failed"
* Verify "third" ends with state "Completed" and result "Passed"




Teardown of contexts
* Capture go state "StageDetailsJobTab" - teardown
* With "3" live agents in directory "StageDetails" - teardown
* Using pipeline "pipeline-with-3-jobs" - teardown
* Basic configuration - teardown


