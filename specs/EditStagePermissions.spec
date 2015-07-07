EditStagePermissions
====================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "EditStagePermissions" - setup

EditStagePermissions
--------------------

tags: Clicky Admin, 4690

* Click on pipeline "edit-pipeline" for editing

* Open stage listing page

Verify the happy path of authorizing a user and role to operate on a stage

* Open stage "defaultStage"

* Navigate to "Permissions" tab
* Verify that "Inherit from the pipeline group" is selected
* Verify that the message "There are no operate permissions configured for this stage nor its pipeline group. All Go users can operate on this stage." shows up - Already On Edit Stage Page
* Verify that the message "All system administrators and pipeline group administrators can operate on this stage (this cannot be overridden)." shows up - Already On Edit Stage Page
* Select "Specify locally"
* Enter "a" as user name
* Auto complete should show up "admin"
* Select option "admin"
* Save - Already On Edit Stage Page
* Verify that user "admin" is authorized to operate on the stage
* Navigate to "Permissions" tab
* Enter "ope" as role name
* Auto complete should show up "operator"
* Select option "operator"
* Save - Already On Edit Stage Page
* Verify that role "operator" is authorized to operate on the stage






Teardown of contexts 
* Capture go state "EditStagePermissions" - teardown
* Using pipeline "edit-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


