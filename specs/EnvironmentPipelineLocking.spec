EnvironmentPipelineLocking
==========================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "environment-pipeline, environment-failing-pipeline, environment-pipeline-locked" - setup
* With "1" live agents in directory "pipeline-locking" - setup
* Capture go state "EnvironmentPipelineLocking" - setup

EnvironmentPipelineLocking
--------------------------

tags: 3378, 3411, feeds, restful api, shine, 3426, automate, 3431, stage1

* Add environment "uat" to agents "2"

* Verify unlocking "environment-pipeline" is not acceptable because "no lock exists within the pipeline configuration for environment-pipeline"
* Verify unlocking "environment-pipeline-locked" is not acceptable because "lock exists within the pipeline configuration but no pipeline instance is currently in progress"

* Looking at pipeline "environment-pipeline-locked"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Wait for stage "secondStage" status to be "Building" with label "1"

* Verify unlocking "environment-pipeline-locked" is not acceptable because "locked pipeline instance is currently running (one of the stages is in progress)"

* Looking at pipeline "environment-pipeline-locked"
* Wait for stage "secondStage" status to be "Passed" with label "1"

* Verify can unlock "environment-pipeline-locked"

Verify a stage can be rerun after releasing the lock

* Looking at pipeline "environment-pipeline-locked"
* Rerun stage "defaultStage" for current pipeline having pipeline label "1"
* Wait for stage "defaultStage" status to be "Building" with label "1"
* Wait for stage "defaultStage" status to be "Passed" with label "1"
* Wait for stage "secondStage" status to be "Building" with label "1"
* Wait for stage "secondStage" status to be "Passed" with label "1"

* Verify can unlock "environment-pipeline-locked"

Verify a manual stage of the same instance can be triggered

* Looking at pipeline "environment-pipeline-locked"
* Trigger pipeline
* Wait for stage "secondStage" status to be "Passed" with label "2"
* Navigate to the pipeline history page for pipeline "environment-pipeline-locked"

* Looking at pipeline with label "2"
* Approve stage "lastStage"

* Looking at pipeline "environment-pipeline-locked"
* Wait for stage "lastStage" status to be "Building" with label "2"

Verify completing a pipeline will unlock it

* Looking at pipeline "environment-pipeline-locked"
* Wait for stage "lastStage" status to be "Passed" with label "2"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "3"

Verify a pipeline with a failed stage can be unlocked

* Looking at pipeline "environment-failing-pipeline"
* Trigger pipeline
* Verify stage "1" is "Failed" on pipeline with label "1"

* Verify can unlock "environment-failing-pipeline"





Teardown of contexts 
* Capture go state "EnvironmentPipelineLocking" - teardown
* With "1" live agents in directory "pipeline-locking" - teardown
* Using pipeline "environment-pipeline, environment-failing-pipeline, environment-pipeline-locked" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


