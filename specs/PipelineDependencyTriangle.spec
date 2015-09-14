PipelineDependencyTriangle
==========================

Setup of contexts
* Basic configuration - setup
* Using pipeline "fourth, fifth, another-sixth" - setup
* With "2" live agents in directory "StageDetails" - setup
* Capture go state "PipelineDependencyTriangle" - setup

PipelineDependencyTriangle
--------------------------

tags: dependency pipeline, 3695, 3957, automate, failing, server_restart_needed

* Stop server
* Start server with fanin turned off

* Trigger pipelines "fourth" and wait for labels "1" to pass
* Trigger pipelines "fourth" and wait for labels "2" to pass
* Trigger pipelines "fifth" and wait for labels "1" to pass
* Looking at pipeline "fifth"
* Pause pipeline with reason "pausing to test dependency"
* Looking at pipeline "another-sixth"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Open changes section for counter "1"

* Looking at material of type "Pipeline" named "${runtime_name:fourth}" for pipeline "another-sixth" with counter "1"
* Verify modification "0" has revision "${runtime_name:fourth}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:fifth}" for pipeline "another-sixth" with counter "1"
* Verify modification "0" has revision "${runtime_name:fifth}/1/defaultStage/1"
* Verify material has changed

* Trigger pipelines "fourth" and wait for labels "3" to pass
* Trigger pipelines "fourth" and wait for labels "4" to pass
* Looking at pipeline "another-sixth"
* Verify pipeline is at label "1" and does not get triggered






Teardown of contexts
* Capture go state "PipelineDependencyTriangle" - teardown
* With "2" live agents in directory "StageDetails" - teardown
* Using pipeline "fourth, fifth, another-sixth" - teardown
* Basic configuration - teardown


