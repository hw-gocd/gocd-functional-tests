EditStage
=========

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "EditStage" - setup

EditStage
---------

tags: Clicky Admin, 4595, 5005

* Click on pipeline "edit-pipeline" for editing

* Open stage listing page

* Open stage "defaultStage"

* Set stage name as "some really horrible stage name"
* Click save - Already on Edit Stage Page
* Verify save failed
* Verify error message "Invalid stage name 'some really horrible stage name'. This must be alphanumeric and can contain underscores and periods (however, it cannot start with a period). The maximum allowed length is 255 characters." is shown
* Set stage name as "new-shiny-but-valid-stage-name"
* Click save - Already on Edit Stage Page
* Verify that stage saved successfully - Already on edit stage page
* Verify that stage is named "new-shiny-but-valid-stage-name"

* Click on pipeline "edit-pipeline" for editing

* Open stage listing page

* Open stage "new-shiny-but-valid-stage-name"

* Verify that stage is named "new-shiny-but-valid-stage-name"





Teardown of contexts
* Capture go state "EditStage" - teardown
* Using pipeline "edit-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


