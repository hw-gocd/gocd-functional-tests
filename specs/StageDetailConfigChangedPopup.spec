StageDetailConfigChangedPopup
=============================

Setup of contexts 
* Secure configuration - setup
* Login as "Admin" - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "StageDetailConfigChangedPopup" - setup

StageDetailConfigChangedPopup
-----------------------------

tags: 6715

* trigger pipeline "edit-pipeline" and cancel it

//Make A Config Change
* Click on pipeline "edit-pipeline" for editing

* Open stage listing page

* Open stage "defaultStage"

* Open jobs

* Open job "defaultJob"

* Open job settings
* Set job name as "new_job_name"
* Click save - Already On Job Edit Page
* Verify that job saved sucessfully
* Verify that job is named "new_job_name"

* Looking at pipeline "edit-pipeline"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "2"
* Navigate to stage "defaultStage" of run "2" having counter "1"

* Cancel "defaultStage" - Already On Stage Detail Page
* Reload page - Already On Stage Detail Page
* Verify config changed marker after pipeline counter "1" stage counter "1" is a link
* Click on config changed link after pipeline counter "1" stage counter "1"

* Verify added changes contains lines "+ <job name=\"new_job_name\""
* Verify removed changes contains lines "- <job name=\"defaultJob\""

* Logout - On Any Page

* Login as "operate"

* Looking at pipeline "edit-pipeline"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "3"
* Navigate to stage "defaultStage" of run "3" having counter "1"

* Cancel "defaultStage" - Already On Stage Detail Page
* Reload page - Already On Stage Detail Page
* Verify config changed marker after pipeline counter "1" stage counter "1" is not a link





Teardown of contexts 
* Capture go state "StageDetailConfigChangedPopup" - teardown
* Using pipeline "edit-pipeline" - teardown
* Login as "Admin" - teardown
* Secure configuration - teardown


