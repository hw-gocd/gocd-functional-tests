EditStagePermissionsWithPipelineGroupAdmins
===========================================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "EditStagePermissionsWithPipelineGroupAdmins" - setup

EditStagePermissionsWithPipelineGroupAdmins
-------------------------------------------

tags: Clicky Admin, 4690

Verify that an admin or a pipeline group admin can be explicitly added as an operate user

* Open "User Summary" tab

* Search for "pavan" and add user "1" in the search result
* Search for "raghu" and add user "1" in the search result

* Adding "pavan" as a group admin of "basic"

* Click on pipeline "edit-pipeline" for editing

* Open stage listing page

* Open stage "defaultStage"

* Navigate to "Permissions" tab
* Select "Specify locally"
* Enter "pavan" as user name
* Save - Already On Edit Stage Page
* Verify that user "pavan" is authorized to operate on the stage
* Enter "admin" as user name
* Save - Already On Edit Stage Page
* Verify that user "admin" is authorized to operate on the stage






Teardown of contexts 
* Capture go state "EditStagePermissionsWithPipelineGroupAdmins" - teardown
* Using pipeline "edit-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


