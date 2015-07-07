PipelineUnlocking
=================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-2-manual-stages-that-run-till-file-exists, pipeline-with-failing-stage" - setup
* With "1" live agents in directory "pipeline-unlocking" - setup
* Capture go state "PipelineUnlocking" - setup

PipelineUnlocking
-----------------

tags: 3378, 3411, feeds, restful api, shine, 3426, automate, failing

Verify can unlock a pipeline that's waiting for a manual stage to be triggered

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Trigger pipeline

* Stop "1" jobs that are waiting for file to exist

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Verify stage "1" is "Passed" on pipeline with label "1"

* Verify can unlock "pipeline-2-manual-stages-that-run-till-file-exists"

Verify can unlock a pipeline that's been cancelled

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "2"
* Navigate to stage "defaultStage" of run "2"

* Wait for agent to show status "building"

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Verify stage "1" is "Building" on pipeline with label "2"
* Navigate to stage "defaultStage" of run "2"

* Cancel "defaultStage" - Already On Stage Detail Page
* Wait for stage result to show "Cancelled"

* Verify can unlock "pipeline-2-manual-stages-that-run-till-file-exists"

Verify a stage can be rerun after releasing the lock

* Rerun stage "defaultStage"

* Wait for agent to show status "building"

* Stop "1" jobs that are waiting for file to exist

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Navigate to stage "defaultStage" of run "2"

* Verify stage bar is displaying run "2" of "2"
* Wait for stage result to show "Passed"

Verify a manual stage of the same instance can be triggered

* Trigger stage "secondStage"

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Verify stage "2" is "Building" on pipeline with label "2"

Verify completing a pipeline will unlock it

* Stop "1" jobs that are waiting for file to exist

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Verify stage "2" is "Passed" on pipeline with label "2"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "3"

* Stop "1" jobs that are waiting for file to exist

Verify a pipeline with a failed stage can be unlocked

* Looking at pipeline "pipeline-with-failing-stage"
* Trigger pipeline
* Verify stage "1" is "Failed" on pipeline with label "1"

* Verify can unlock "pipeline-with-failing-stage"





Teardown of contexts 
* Capture go state "PipelineUnlocking" - teardown
* With "1" live agents in directory "pipeline-unlocking" - teardown
* Using pipeline "pipeline-2-manual-stages-that-run-till-file-exists, pipeline-with-failing-stage" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


