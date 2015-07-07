CardActivityPage
================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "mingle-config-parent, pipeline-with-mingle-config" - setup
* With "1" live agents in directory "card_activity" - setup
* Capture go state "CardActivityPage" - setup

CardActivityPage
----------------

tags: 4521, card_activity, automate, 4520, mingle

* Looking at pipeline "mingle-config-parent"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "hello-world-1"
* Looking at pipeline "pipeline-with-mingle-config"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Cancel "secondStage" - Already On Stage Detail Page

* Looking at pipeline "pipeline-with-mingle-config"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "2"
* Verify stage "2" is "Building" on pipeline with label "2"
* Click compare link

* Verify that page has gadget for url "https://some.mingle.machine:1000/mingle/gadgets/card_activity.xml" project named "some-go-branch" and criteria "foo != not(foo)"
* Verify that page displays stages "defaultStage (Passed),secondStage (Cancelled)" in pipeline dropdown "from" with pipeline counter "1"
* Verify that page displays stages "defaultStage (Passed),secondStage (Building)" in pipeline dropdown "to" with pipeline counter "2"
* Click "${runtime_name:pipeline-with-mingle-config}" in breadcrumbs

* Verify on pipeline history page for "pipeline-with-mingle-config"








Teardown of contexts 
* Capture go state "CardActivityPage" - teardown
* With "1" live agents in directory "card_activity" - teardown
* Using pipeline "mingle-config-parent, pipeline-with-mingle-config" - teardown
* Basic configuration - teardown


