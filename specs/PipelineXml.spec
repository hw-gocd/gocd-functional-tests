PipelineXml
===========

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline-fast, admin-pipeline" - setup
* With "1" live agents in directory "NOT-USED" - setup
* Capture go state "PipelineXml" - setup

PipelineXml
-----------

tags: 3378, 3411, feeds, shine, automate

* With material "basic-pipeline-hg" for pipeline "basic-pipeline-fast"
* Checkin file "new-file-1" as user "go <go@po.com>" with message "Added new-file 1"

* Logged in as "view"

* Verify "basic-pipeline-fast" is shown
* Verify "admin-pipeline" is not shown

* Verify "basic-pipeline-fast" is viewable
* Verify pipeline instance "foo-pipeline" is not found
* Verify "admin-pipeline" is not viewable

* Trigger pipelines "basic-pipeline-fast" and wait for labels "1" to pass
* Trigger pipelines "admin-pipeline" and wait for labels "1" to pass

* Logged in as "admin"

* Verify shows first instance of "defaultStage" of "admin-pipeline"

* Logged in as "view"

* Verify shows first instance of "defaultStage" of "basic-pipeline-fast"

* Verify loads "basic-pipeline-fast" instance with file "new-file-1"
* Verify unauthorized to load "admin-pipeline"
* Verify fails to find "basic-pipeline-fast" with bad id





Teardown of contexts
* Capture go state "PipelineXml" - teardown
* With "1" live agents in directory "NOT-USED" - teardown
* Using pipeline "basic-pipeline-fast, admin-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


