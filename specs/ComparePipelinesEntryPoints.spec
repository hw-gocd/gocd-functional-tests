ComparePipelinesEntryPoints
===========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "basic-environment-pipeline" - setup
* With "1" live agents in directory "card_activity" - setup
* Capture go state "ComparePipelinesEntryPoints" - setup

ComparePipelinesEntryPoints
---------------------------

tags: 4521, automate, 4520, mingle, 4649, compare_pipeline

* Trigger and cancel pipeline "basic-environment-pipeline" "2" times
* Navigate to stage "defaultStage" of run "2" having counter "1"

* Verify stage history has "2, 1"
* Click compare link for pipeline counter "1"

* Verify that "to" textbox is populated with "1"
* Verify that "from" textbox is populated with "2"

* Looking at pipeline "basic-environment-pipeline"
* Click compare link

Simple case of comparison
* Verify that "to" textbox is populated with "2"
* Verify that "from" textbox is populated with "1"

* Looking at pipeline "basic-environment-pipeline" of "prod" environment
* Click compare link - On Environment Page

* Verify that "to" textbox is populated with "2"
* Verify that "from" textbox is populated with "1"

* Looking at pipeline "basic-environment-pipeline"
* Navigate to stage "defaultStage" of run "2" having counter "1"

* Click compare link - Already on stage Detail Page

* Verify that "to" textbox is populated with "2"
* Verify that "from" textbox is populated with "1"




Teardown of contexts 
* Capture go state "ComparePipelinesEntryPoints" - teardown
* With "1" live agents in directory "card_activity" - teardown
* Using pipeline "basic-environment-pipeline" - teardown
* Basic configuration - teardown


