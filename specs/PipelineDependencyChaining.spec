PipelineDependencyChaining
==========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "autoFirst, child-of-autoFirst, grandchild-of-autoFirst" - setup
* With "2" live agents in directory "StageDetails" - setup
* Capture go state "PipelineDependencyChaining" - setup

PipelineDependencyChaining
--------------------------

tags: dependency pipeline, automate, 3742


* Looking at pipeline "autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "child-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "grandchild-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"

SCM Trigger

* With material "hg-first" for pipeline "autoFirst"
* Checkin file "hg-new-file" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-new1"

Verify dependency chaining after scm triggers autoFirst pipeline

* Looking at pipeline "autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "child-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Pipeline" named "${runtime_name:autoFirst}" for pipeline "child-of-autoFirst" with counter "2"
* Verify modification "0" has revision "${runtime_name:autoFirst}/2/defaultStage/1"
* Verify material has changed

* Looking at pipeline "grandchild-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Pipeline" named "${runtime_name:child-of-autoFirst}" for pipeline "grandchild-of-autoFirst" with counter "2"
* Verify modification "0" has revision "${runtime_name:child-of-autoFirst}/2/defaultStage/1"
* Verify material has changed




Teardown of contexts 
* Capture go state "PipelineDependencyChaining" - teardown
* With "2" live agents in directory "StageDetails" - teardown
* Using pipeline "autoFirst, child-of-autoFirst, grandchild-of-autoFirst" - teardown
* Basic configuration - teardown


