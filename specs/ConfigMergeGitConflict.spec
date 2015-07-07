ConfigMergeGitConflict
======================

Setup of contexts 
* ConflictingConfiguration - setup
* Login as "admin" - setup
* Capture go state "ConfigMergeGitConflict" - setup
* Using pipeline "basic-pipeline, upstream-pipeline,middle-pipeline" - setup

ConfigMergeGitConflict
----------------------

tags: 7303, 7270, 7278

Merge Conflict
* Open "Config XML" tab

* Click edit
* Remember current tab - Already on Source Xml Tab

* For pipeline group "basic"
* Delete pipeline "basic-pipeline" - Configure cruise using api

* Change config to conflict
* Click save - Already on Source Xml Tab
* Verify that split pane appears
* Verify conflict error messages are shown
* Remember current tab - Already on Source Xml Tab

Successfull merge
* For pipeline group "basic"
* Rename pipeline "middle-pipeline" to "middle-pipeline-new"


* Click save - Already on Source Xml Tab
* Verify config gets merged successfully

Post validation failure
* Click edit
* Remember current tab - Already on Source Xml Tab

* For pipeline group "basic"
* Delete pipeline "upstream-pipeline" - Configure cruise using api

* Add downstream pipeline to create post validation conflict
* Click save - Already on Source Xml Tab
* Verify that split pane appears
* Verify post validation error is shown with message "Pipeline \"${runtime_name:upstream-pipeline}\" does not exist. It is used from pipeline \"downstream-pipeline\"."
* Click save - Already on Source Xml Tab
* Verify config gets saved successfully




Teardown of contexts 
* Using pipeline "basic-pipeline, upstream-pipeline,middle-pipeline" - teardown
* Capture go state "ConfigMergeGitConflict" - teardown
* Login as "admin" - teardown
* ConflictingConfiguration - teardown


