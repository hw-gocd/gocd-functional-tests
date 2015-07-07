HungJobWarning
==============

Setup of contexts 
* Basic configuration - setup
* Using pipeline "hung-job-pipeline" - setup
* With "1" live agents in directory "HungJobWarning" - setup
* Capture go state "HungJobWarning" - setup

HungJobWarning
--------------

tags: #4584, Clicky Admin

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

* Cancel "defaultStage" - Already On Stage Detail Page
* Go to jobs tab

* Verify job "defaultJob" has state "Completed" and result "Cancelled"




Teardown of contexts 
* Capture go state "HungJobWarning" - teardown
* With "1" live agents in directory "HungJobWarning" - teardown
* Using pipeline "hung-job-pipeline" - teardown
* Basic configuration - teardown


