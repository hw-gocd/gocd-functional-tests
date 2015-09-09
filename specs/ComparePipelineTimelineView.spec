ComparePipelineTimelineView
===========================

Setup of contexts
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "ComparePipelineTimelineView" - setup

ComparePipelineTimelineView
---------------------------

tags: #4568, compare_pipeline

* Trigger and cancel pipeline "edit-pipeline" "12" times
* Navigate to stage "defaultStage" of run "12" having counter "1"

* Click compare link for pipeline counter "12"

Basic functionality
* Verify that "to" textbox is populated with "12"
* Verify that "from" textbox is populated with "12"
* Click on "from" textbox
* Verify "from" sugggestion box has "Search for a pipeline instance by label, commiter, date, etc. or Browse the timeline"
* Click on "to" textbox
* Verify "to" sugggestion box has "Search for a pipeline instance by label, commiter, date, etc. or Browse the timeline"
* Click to browse the timeline on "to" suggestion box

* Verify selected pipeline is "12"
* Verify that page has pipeline range "12" to "3"
* Click on page "2"
* Verify that page has pipeline range "2" to "1"
* Choose pipeline with label "1"
* Confirm selection

* Verify that "to" textbox is populated with "1"
* Verify that "from" textbox is populated with "12"
* Click on "from" textbox
* Click to browse the timeline on "from" suggestion box

* Verify selected pipeline is "12"
* Choose pipeline with label "3"
* Confirm selection

* Verify that "to" textbox is populated with "1"
* Verify that "from" textbox is populated with "3"




Teardown of contexts
* Capture go state "ComparePipelineTimelineView" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


