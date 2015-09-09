HungJobZeroTimeOutForJob
========================

Setup of contexts
* Basic configuration - setup
* Using pipeline "hung-job-zero-timeout-pipeline" - setup
* With "1" live agents in directory "HungJobZeroTimeOutForJob" - setup
* Capture go state "HungJobZeroTimeOutForJob" - setup

HungJobZeroTimeOutForJob
------------------------

tags: #4584, Clicky Admin

* Open "Server Configuration" tab

* Set cancel job after "2" minutes
* Save configuration

* Click on pipeline "hung-job-zero-timeout-pipeline" for editing

* Open stage "defaultStage" - Using Pipeline Navigation

* Open jobs

* Open job "defaultJob"

* Open job settings
* Select never option
* Click save - Already On Job Edit Page
* Verify that job saved sucessfully

* Turn on autoRefresh - On Pipeline Dashboard Page
* Looking at pipeline "hung-job-zero-timeout-pipeline"
* Trigger pipeline

* Wait and verify there are no warnings

* Looking at pipeline "hung-job-zero-timeout-pipeline"
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Wait for stage result to show "Passed"






Teardown of contexts
* Capture go state "HungJobZeroTimeOutForJob" - teardown
* With "1" live agents in directory "HungJobZeroTimeOutForJob" - teardown
* Using pipeline "hung-job-zero-timeout-pipeline" - teardown
* Basic configuration - teardown


