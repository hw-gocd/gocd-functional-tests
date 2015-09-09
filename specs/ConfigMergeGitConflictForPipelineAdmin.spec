ConfigMergeGitConflictForPipelineAdmin
======================================

Setup of contexts
* ConflictingConfigurationForPipelineAdmin - setup
* Login as "group1Admin" - setup
* Capture go state "ConfigMergeGitConflictForPipelineAdmin" - setup

ConfigMergeGitConflictForPipelineAdmin
--------------------------------------

tags: 7342, 7278

Merge Conflict
* Open config tab as group admin

* Click link "Edit"
* Remember current tab - Already on Pipeline Group Xml

* For pipeline group "PG1"
* Rename pipeline "P1" to "P_NEW"

* Rename pipeline "P1" to "P_conflict" - Already On Pipeline Group Xml
* Save changes
* Verify merge conflict error message shows up
* Click link "CANCEL"

Post validation failure
* Click link "Edit"
* Remember current tab - Already on Pipeline Group Xml

* For pipeline group "PG1"
* Rename pipeline "P2" to "P"

* Rename pipeline "P3" to "P" - Already On Pipeline Group Xml
* Save changes
* Verify post validation error occurs with the message "You have defined multiple pipelines called 'P'. Pipeline names must be unique."
* Click link "CANCEL"


Successful Merge
* Click link "Edit"
* Remember current tab - Already on Pipeline Group Xml

* For pipeline group "PG1"
* Rename pipeline "P3" to "P-rename"

* Rename pipeline "P4" to "P-merge" - Already On Pipeline Group Xml
* Save changes
* Verify successful merge message




Teardown of contexts
* Capture go state "ConfigMergeGitConflictForPipelineAdmin" - teardown
* Login as "group1Admin" - teardown
* ConflictingConfigurationForPipelineAdmin - teardown


