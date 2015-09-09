JobRerunConfigDeletion
======================

Setup of contexts
* Basic configuration - setup
* Using pipeline "pipeline-with-3-jobs" - setup
* Capture go state "JobRerunConfigDeletion" - setup

JobRerunConfigDeletion
----------------------

tags: 4137, stage-details, job-rerun, scheduling, rerun

* Looking at pipeline "pipeline-with-3-jobs"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Cancel "defaultStage" - Already On Stage Detail Page

* Remove job "second" from stage "defaultStage" in pipeline "pipeline-with-3-jobs"

* Looking at pipeline "pipeline-with-3-jobs"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Go to jobs tab

* Rerun "second" jobs
* Verify rerun failed with cause "Cannot rerun job 'second'. Configuration for job doesn't exist."
* Verify looking at "defaultStage" having counter "1"





Teardown of contexts
* Capture go state "JobRerunConfigDeletion" - teardown
* Using pipeline "pipeline-with-3-jobs" - teardown
* Basic configuration - teardown


