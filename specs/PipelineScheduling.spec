PipelineScheduling
==================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-2-manual-stages-that-run-till-file-exists" - setup
* With "1" live agents in directory "PipelineScheduling" - setup
* Capture go state "PipelineScheduling" - setup

PipelineScheduling
------------------

tags: restful api, #2482, svn support, scheduling, diagnostics messages, rerun, 1646, scheduling, svn support, ant support, automate, stage1

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage detail page for "pipeline-2-manual-stages-that-run-till-file-exists" "1" "defaultStage" "1" with stage history page size "1"

* Verify stage "defaultStage" has action "Cancel"
* Verify stage "defaultStage" does not have action "Rerun"

* For pipeline named "pipeline-2-manual-stages-that-run-till-file-exists"
* Schedule should return code "404"

* Stop "1" jobs that are waiting for file to exist

* Navigate to stage detail page for "pipeline-2-manual-stages-that-run-till-file-exists" "1" "defaultStage" "1" with stage history page size "1"

* Wait for stage result to show "Passed"
* Trigger stage "secondStage"

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Verify stage "2" is "Building" on pipeline with label "1"
* Navigate to stage detail page for "pipeline-2-manual-stages-that-run-till-file-exists" "1" "secondStage" "1" with stage history page size "1"

* Verify stage "secondStage" has action "Cancel"
* Verify stage "secondStage" does not have action "Rerun"

* For pipeline named "pipeline-2-manual-stages-that-run-till-file-exists"
* Schedule should return code "404"

* Stop "1" jobs that are waiting for file to exist




Teardown of contexts 
* Capture go state "PipelineScheduling" - teardown
* With "1" live agents in directory "PipelineScheduling" - teardown
* Using pipeline "pipeline-2-manual-stages-that-run-till-file-exists" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


