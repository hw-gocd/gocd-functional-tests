EnvironmentsScreenNavigation
============================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "environment-pipeline" - setup
* With "2" live agents in directory "UINavigationForEnvironments" - setup
* Capture go state "EnvironmentsScreenNavigation" - setup

EnvironmentsScreenNavigation
----------------------------

tags: 2808, environment, UI, 3216, pipeline, automate, 3493

Tests navigation from Environment page to different pages.

* Looking at "uat" environment
* Looking at pipeline "environment-pipeline" - On Environment Page
* Verify stage bar is not visible for pipeline "environment-pipeline"

* Add resource "linux" to all agents

* Assigning "1" agents with resource "linux" to environment "uat"
* Adding resource "linux" to the job "short"

* Looking at pipeline "environment-pipeline"
* Trigger pipeline "environment-pipeline"

* Verify the pipeline is building only on agents in "uat"

* Looking at pipeline "environment-pipeline"
* Verify stage "1" is "Passed" on pipeline with label "1"

* Looking at "uat" environment
* Looking at pipeline "environment-pipeline" - On Environment Page
* Verify the pipeline has label "1"
* Verify stage status "Passed: defaultStage" shows up for the pipeline
* Click on stage "defaultStage" of pipeline "environment-pipeline"
* Verify on stage details page for "environment-pipeline" stage "defaultStage"







Teardown of contexts 
* Capture go state "EnvironmentsScreenNavigation" - teardown
* With "2" live agents in directory "UINavigationForEnvironments" - teardown
* Using pipeline "environment-pipeline" - teardown
* Basic configuration - teardown


