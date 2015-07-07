HungJobServerTagTimeOut
=======================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "hung-job-pipeline" - setup
* With "1" live agents in directory "HungJobServerTagTimeOut" - setup
* Capture go state "HungJobServerTagTimeOut" - setup

HungJobServerTagTimeOut
-----------------------

tags: #4584, admin-page

* Open "Server Configuration" tab

* Set cancel job after "3" minutes
* Save configuration

* Turn on autoRefresh - On Pipeline Dashboard Page
* Looking at pipeline "hung-job-pipeline"
* Trigger pipeline

* Verify there are "1" warnings
* Open error and warning messages popup

* Verify warning "message" contains "is not responding"
* Verify warning "description" contains "This job may be hung."
* Close

* Looking at pipeline "hung-job-pipeline"
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Wait for stage result to show "Cancelled"
* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "Go cancelled this job as it has not generated any console output for more than 3 minute(s)"

* Verify there are no warnings




Teardown of contexts 
* Capture go state "HungJobServerTagTimeOut" - teardown
* With "1" live agents in directory "HungJobServerTagTimeOut" - teardown
* Using pipeline "hung-job-pipeline" - teardown
* Basic configuration - teardown


