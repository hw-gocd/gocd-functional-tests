PipelineDependencyWithDependencyMaterialAtHop
=============================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "fourth, fifth, sixth, last-sixth" - setup
* With "2" live agents in directory "StageDetails" - setup
* Capture go state "PipelineDependencyWithDependencyMaterialAtHop" - setup

PipelineDependencyWithDependencyMaterialAtHop
---------------------------------------------

tags: dependency pipeline, 3695, automate

Get to a sane state

* Trigger pipelines "fourth" and wait for labels "1" to pass
* Trigger pipelines "fifth" and wait for labels "1" to pass
* Trigger pipelines "sixth" and wait for labels "1" to pass
* Looking at pipeline "last-sixth"
* Verify stage "1" is "Passed" on pipeline with label "1"

Case of Dependency material with hop

* With material named "hg-first" in pipeline "fourth"
* Checkin file "abc.txt" as user "user" with message "Comment user"
* Commit file "new_artifact.txt" to directory "baz"

* Trigger pipelines "fourth" and wait for labels "2" to pass

* For pipeline "fifth" - Using pipeline api
* Using "${runtime_name:fourth}/1/defaultStage/1" revision of "${runtime_name:fourth}"
* Schedule should return code "202"

* Looking at pipeline "fifth"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Trigger pipelines "sixth" and wait for labels "2" to pass
* Looking at pipeline "last-sixth"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "last-sixth"
* Open changes section for counter "2"

* Looking at material of type "Pipeline" named "${runtime_name:fourth}" for pipeline "last-sixth" with counter "2"
* Verify has only "1" modifications
* Verify modification "0" has revision "${runtime_name:fourth}/1/defaultStage/1"
* Navigate to stage "defaultStage" of run "2" having counter "1"

* Navigate to job "job-of-last"




Teardown of contexts
* Capture go state "PipelineDependencyWithDependencyMaterialAtHop" - teardown
* With "2" live agents in directory "StageDetails" - teardown
* Using pipeline "fourth, fifth, sixth, last-sixth" - teardown
* Basic configuration - teardown


