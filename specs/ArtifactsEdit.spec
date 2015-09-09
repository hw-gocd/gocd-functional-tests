ArtifactsEdit
=============

Setup of contexts
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "ArtifactsEdit" - setup

ArtifactsEdit
-------------

* Click on pipeline "edit-pipeline" for editing

* Open stage listing page

* Open stage "defaultStage"

* Open jobs

* Open job "defaultJob"

* Open artifacts

* Enter artifact detail "1" "first_source" "first_destination" "Test Artifact"
* Click save - Already on Artifacts Listing Page
* Verify saved successfully - Already on Artifacts Listing Page
* Enter artifact detail "2" "second_source" "second destination" "Build Artifact"
* Click save - Already on Artifacts Listing Page
* Verify saved successfully - Already on Artifacts Listing Page


* For pipeline "edit-pipeline"
* Verify "test" artifact with "@src:first_source, @dest:first_destination" exists for "defaultJob" in "defaultStage"
* Verify "artifact" artifact with "@src:second_source, @dest:second destination" exists for "defaultJob" in "defaultStage"





Teardown of contexts
* Capture go state "ArtifactsEdit" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


