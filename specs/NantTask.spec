NantTask
========

Setup of contexts 
* Basic configuration - setup
* Using pipeline "nant-pipeline" - setup
* With "1" live agents in directory "NantTask" - setup
* Capture go state "NantTask" - setup

NantTask
--------

tags: nant, 1147, diagnostics messages, nant support, dashboard, scheduling, windows, automate


* Trigger pipeline
* Wait for first stage to pass with pipeline label "1"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

open "Tests" tab
verify test contains "All Tests Passed"

* Verify console contains "BUILD SUCCEEDED"




Teardown of contexts 
* Capture go state "NantTask" - teardown
* With "1" live agents in directory "NantTask" - teardown
* Using pipeline "nant-pipeline" - teardown
* Basic configuration - teardown


