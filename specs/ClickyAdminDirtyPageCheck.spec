ClickyAdminDirtyPageCheck
=========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "ClickyAdminDirtyPageCheck" - setup

ClickyAdminDirtyPageCheck
-------------------------

tags: Clicky Admin, 4661

* Click on pipeline "edit-pipeline" for editing

Checking for textbox and checkbox
* Enter "${COUNT}-pipelinename" for label template
* Open parameters page
* Verify that dirty check is invoked
* Cancel dirty check prompt
* Click reset
* Check automatic pipeline locking
* Open stage listing page
* Verify that dirty check is invoked
* Proceed with dirty check prompt

* Open stage "defaultStage"

Checking for radio group
* Select stage type as "auto"
* Click reset - Already on edit stage page
* Select stage type as "auto"
* Select stage type as "manual"
* Go to environment variables page - Already on edit stage page
* Proceed with dirty check prompt - Already on edit stage page

* Verify heading "Environment Variables"




Teardown of contexts 
* Capture go state "ClickyAdminDirtyPageCheck" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


