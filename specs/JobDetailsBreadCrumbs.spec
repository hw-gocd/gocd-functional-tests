JobDetailsBreadCrumbs
=====================

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast" - setup
* Capture go state "JobDetailsBreadCrumbs" - setup

JobDetailsBreadCrumbs
---------------------

tags: 4147, breadcrumbs, job-detail

* Looking at pipeline "basic-pipeline-fast"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

* Verify breadcrumb contains pipeline "basic-pipeline-fast"
* Verify breadcrumb contains pipeline label "1"
* Verify breadcrumb contains stage run "defaultStage / 1"
* Click on bread crumb "defaultStage / 1"

* Verify that "${runtime_name:basic-pipeline-fast}/1/defaultStage/1" stage is displayed
* Cancel "defaultStage" - Already On Stage Detail Page
* Rerun stage "defaultStage"
* Click on stage bar run "2" of "2"
* Navigate to job "defaultJob"

* Verify breadcrumb contains pipeline "basic-pipeline-fast"
* Verify breadcrumb contains pipeline label "1"
* Verify breadcrumb contains stage run "defaultStage / 2"
* Verify breadcrumb contains link to value stream map on pipeline label "1" for pipeline "basic-pipeline-fast" for counter "1"
* Click on bread crumb "defaultStage / 2"

* Verify that "${runtime_name:basic-pipeline-fast}/1/defaultStage/2" stage is displayed
* Cancel "defaultStage" - Already On Stage Detail Page
* Go to jobs tab
* Navigate to job "defaultJob"

* Click on pipeline bread crumb "basic-pipeline-fast"

* Verify on pipeline history page for "basic-pipeline-fast"





Teardown of contexts
* Capture go state "JobDetailsBreadCrumbs" - teardown
* Using pipeline "basic-pipeline-fast" - teardown
* Basic configuration - teardown


