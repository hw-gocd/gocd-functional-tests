PipelineDependencyChainingWithIgnoreFilters
===========================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "autoFirst, child-of-autoFirst, grandchild-of-autoFirst" - setup
* With "2" live agents in directory "StageDetails" - setup
* Capture go state "PipelineDependencyChainingWithIgnoreFilters" - setup

PipelineDependencyChainingWithIgnoreFilters
-------------------------------------------

tags: dependency pipeline, automate, 3742


* Looking at pipeline "autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "child-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "grandchild-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"

SCM Trigger

* With material "hg-first" for pipeline "autoFirst"
* Checkin file "hg-file.oneignore" as user "go" with message "Added hg-new-file"
* With material "hg-first" for pipeline "child-of-autoFirst"
* Checkin file "hg-file.oneignore" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-file"

Verify dependency chaining after scm does not trigger autoFirst pipeline (due to the ignore filter) but triggers child-of-autoFirst pipeline

* Looking at pipeline "autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "child-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Mercurial" named "hg-first" for pipeline "child-of-autoFirst" with counter "2"
* Verify modification "0" has revision "hg-file"
* Verify material has changed

* Looking at pipeline "grandchild-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Pipeline" named "${runtime_name:child-of-autoFirst}" for pipeline "grandchild-of-autoFirst" with counter "2"
* Verify modification "0" has revision "${runtime_name:child-of-autoFirst}/2/defaultStage/1"
* Verify material has changed


Verify dependency chaining after scm does not trigger both autoFirst and child-of-autoFirst because both ignore the checked-on files

* With material "hg-first" for pipeline "autoFirst"
* Checkin file "hg-other-file.twoignore" as user "go" with message "Added hg-other-file"
* With material "hg-first" for pipeline "child-of-autoFirst"
* Checkin file "hg-other-file.twoignore" as user "go" with message "Added hg-other-file"
* With material "hg-first" for pipeline "grandchild-of-autoFirst"
* Checkin file "hg-other-file.twoignore" as user "go" with message "Added hg-other-file"
* Remember current version as "hg-other"

* Looking at pipeline "autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "child-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "grandchild-of-autoFirst"
* Verify stage "1" is "Passed" on pipeline with label "3"
* Open changes section for counter "3"

* Looking at material of type "Mercurial" named "hg-first" for pipeline "grandchild-of-autoFirst" with counter "3"
* Verify modification "0" has revision "hg-other"
* Verify material has changed




Teardown of contexts 
* Capture go state "PipelineDependencyChainingWithIgnoreFilters" - teardown
* With "2" live agents in directory "StageDetails" - teardown
* Using pipeline "autoFirst, child-of-autoFirst, grandchild-of-autoFirst" - teardown
* Basic configuration - teardown


