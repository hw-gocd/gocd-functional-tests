PipelineLayoutStageActions
==========================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-with-3-stages" - setup
* With "1" live agents in directory "PipelineLayout" - setup
* Capture go state "PipelineLayoutStageActions" - setup

PipelineLayoutStageActions
--------------------------

tags: 3657, pipeline layout, automate

* Looking at pipeline "pipeline-with-3-stages"
* Trigger pipeline "pipeline-with-3-stages"
* Verify stage "1" is "Building" on pipeline with label "1"

* Stop "1" jobs that are waiting for file to exist

* Looking at pipeline "pipeline-with-3-stages"
* Wait for stage "first" status to be "Passed" with label "1"
* Navigate to stage "first" of run "1" having counter "1"

* Verify stage "first" has action "Rerun"
* Verify stage "first" does not have action "Trigger"
* Verify stage "first" does not have action "Cancel"
* Verify stage "second" has action "Trigger"
* Verify stage "second" does not have action "Rerun"
* Verify stage "second" does not have action "Cancel"
* Verify stage "third" does not have any action
* Rerun stage "first"

* Looking at pipeline "pipeline-with-3-stages"
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "first" of run "1" having counter "2"

* Verify stage "first" does not have action "Rerun"
* Verify stage "first" does not have action "Trigger"
* Verify stage "first" has action "Cancel"
* Verify stage "second" does not have any action
* Verify stage "third" does not have any action
* Cancel "first" - Already On Stage Detail Page

* Looking at pipeline "pipeline-with-3-stages"
* Wait for stage "first" status to be "Cancelled" with label "1"
* Navigate to stage "first" of run "1" having counter "2"

* Verify stage "first" has action "Rerun"
* Verify stage "first" does not have action "Trigger"
* Verify stage "first" does not have action "Cancel"
* Verify stage "second" has action "Trigger"
* Verify stage "second" does not have action "Rerun"
* Verify stage "second" does not have action "Cancel"
* Verify stage "third" does not have any action
* Trigger stage "second"

* Looking at pipeline "pipeline-with-3-stages"
* Wait for stage "second" status to be "Building" with label "1"
* Navigate to stage "second" of run "1" having counter "1"

* Verify stage "first" does not have any action
* Verify stage "second" does not have action "Trigger"
* Verify stage "second" does not have action "Rerun"
* Verify stage "second" has action "Cancel"
* Verify stage "third" does not have any action

* Stop "1" jobs that are waiting for file to exist

* Looking at pipeline "pipeline-with-3-stages"
* Wait for stage "second" status to be "Passed" with label "1"
* Navigate to stage "second" of run "1" having counter "1"

* Verify stage "first" has action "Rerun"
* Verify stage "first" does not have action "Trigger"
* Verify stage "first" does not have action "Cancel"
* Verify stage "second" has action "Rerun"
* Verify stage "second" does not have action "Trigger"
* Verify stage "second" does not have action "Cancel"
* Verify stage "third" has action "Trigger"
* Verify stage "third" does not have action "Rerun"
* Verify stage "third" does not have action "Cancel"

* Unlock "pipeline-with-3-stages"

* Looking at pipeline "pipeline-with-3-stages"
* Trigger pipeline
* Wait for stage "first" status to be "Building" with label "2"

* Stop "1" jobs that are waiting for file to exist

* Looking at pipeline "pipeline-with-3-stages"
* Wait for stage "first" status to be "Passed" with label "2"
* Navigate directly to stage "first" of run "1" having counter "1"

another instance has lock
* Verify stage "first" does not have any action
* Verify stage "second" does not have any action
* Verify stage "third" does not have any action

* Looking at pipeline "pipeline-with-3-stages"
* Navigate to stage "first" of run "2" having counter "1"

this instance has lock
* Verify stage "first" has action "Rerun"
* Verify stage "first" does not have action "Trigger"
* Verify stage "first" does not have action "Cancel"
* Verify stage "second" has action "Trigger"
* Verify stage "second" does not have action "Rerun"
* Verify stage "second" does not have action "Cancel"
* Verify stage "third" does not have any action





Teardown of contexts
* Capture go state "PipelineLayoutStageActions" - teardown
* With "1" live agents in directory "PipelineLayout" - teardown
* Using pipeline "pipeline-with-3-stages" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


