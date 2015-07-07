PipelineDashboard
=================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-2-manual-stages-that-run-till-file-exists, admin-pipeline" - setup
* With "4" live agents in directory "PipelineDashboard" - setup
* Capture go state "PipelineDashboard" - setup

PipelineDashboard
-----------------

tags: UI, automate, pipeline-dashboard, #3700, 3820, failing, stage1

* Remove lock from pipeline "pipeline-2-manual-stages-that-run-till-file-exists"

* Add environment "uat" to agents "3, 4"

* Logout - On Any Page

* Login as "view"

* Verify user "view" is logged in
* Verify pipeline "admin-pipeline" is not visible
* Verify group "admin-only" is not visible
* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Verify pipeline is in group "basic"
* Verify pipeline has no history
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Verify stage "1" is "Passed" on pipeline with label "1"
* Verify pipeline "pipeline-2-manual-stages-that-run-till-file-exists" is triggered by "view"
* Pause pipeline with reason "twist testing it"
* Verify pipeline is paused with reason "twist testing it" by "view"
* Verify cannot trigger pipeline
* Unpause pipeline
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "2"
* Click on pipeline name

* Approve stage "secondStage" with label "1"

* Verify stage "1" is "Building" on pipeline with label "2"
* Verify stage "2" is "Building" on pipeline with label "1"
* Verify that pipeline with label "2" was previously "Passed"
* Click on previous result for pipeline with label "2"

* Verify that "${runtime_name:pipeline-2-manual-stages-that-run-till-file-exists}/1/defaultStage/1" stage is displayed
* Verify stage result shows "Passed"
* Verify stage bar is displaying run "1" of "1"

* Stop "2" jobs waiting for file to exist - On Pipeline Dashboard Page
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Mercurial" named "hgMaterial" for pipeline "pipeline-2-manual-stages-that-run-till-file-exists" with counter "2"
* Verify modification "0" has latest revision - Already On Build Cause Popup

* Click on pipeline name

* Open changes section for counter "2" - Already on pipeline history page

* Looking at material of type "Mercurial" named "hgMaterial" for pipeline "pipeline-2-manual-stages-that-run-till-file-exists" with counter "2"
* Verify latest revision exists

* With material "hgMaterial" for pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Checkin file "something" as user "twist" with message "Added something"
* Remember current version as "hg-commit1"
* With material "hgMaterial" for pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Checkin file "another file" as user "twist" with message "Added another file"

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "3"
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Verify stage "1" is "Passed" on pipeline with label "3"
* Open trigger with options

* Using material "hgMaterial"
* Search for "something"
* Select revision "1" in search box
* Trigger

* Looking at pipeline "pipeline-2-manual-stages-that-run-till-file-exists"
* Verify trigger with option is disabled
* Verify stage "1" is "Building" on pipeline with label "4"
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Verify stage "1" is "Passed" on pipeline with label "4"
* Open trigger with options

* Verify last run revision is "hg-commit1"
* Close - Already on deployment light box

* Logout - On Any Page

* Login as "admin"

* Looking at pipeline "admin-pipeline"
* Verify pipeline is in group "admin-only"






Teardown of contexts 
* Capture go state "PipelineDashboard" - teardown
* With "4" live agents in directory "PipelineDashboard" - teardown
* Using pipeline "pipeline-2-manual-stages-that-run-till-file-exists, admin-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


