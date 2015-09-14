PermissionsForStageAndJobDetails
================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "first-pipeline,down-pipeline" - setup
* With "1" live agents in directory "stage_details_with_permission" - setup
* Capture go state "PermissionsForStageAndJobDetails" - setup

PermissionsForStageAndJobDetails
--------------------------------

tags: 4643, automate, compare_pipeline, dependency_walk, 4687

* With material "hg-for-down-pipeline" for pipeline "down-pipeline"
* Checkin file "hg-new-file" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-new"
* With material "git-for-first-pipeline" for pipeline "first-pipeline"
* Checkin file "git-new-file" as user "go <go@thoughtworks.com>" with message "Added git-new-file"
* Remember current version as "git-new"

* Trigger pipelines "first-pipeline" and wait for labels "1" to pass
* Trigger pipelines "down-pipeline" and wait for labels "1" to pass

* Logout and login as "raghu"

* Verify pipeline "first-pipeline" is not visible
* Looking at pipeline "down-pipeline"
* Navigate to stage "defaultStage" of run "1"

* Click on revision "${runtime_name:first-pipeline}/1/defaultStage/1"
* Verify that unauthorized access message is shown - Already On Stage Detail Page

* Looking at pipeline "down-pipeline"
* Navigate to stage "defaultStage" of run "1"

* Go to materials tab

* Looking at "${runtime_name:first-pipeline}" of type "Pipeline"
* Looking at revision "${runtime_name:first-pipeline}/1/defaultStage/1"
* Verify has label "1"
* Click on revision "${runtime_name:first-pipeline}/1/defaultStage/1" - Already On Stage Detail Materials Tab
* Verify that unauthorized access message is shown - Already On Stage Detail Materials Tab

* Looking at pipeline "down-pipeline"
* Navigate to pipeline dependencies for "down-pipeline" "1" "defaultStage" "1"

* Click label "1" for upstream pipeline "first-pipeline"
* Verify that unauthorized access message is shown - Already On Stage Detail Pipeline Dependencies Page

* Looking at pipeline "down-pipeline"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

* Click on revision "${runtime_name:first-pipeline}/1/defaultStage/1" on materials tab
* Verify that unauthorized access message is shown - Already On Job Detail Page




Teardown of contexts
* Capture go state "PermissionsForStageAndJobDetails" - teardown
* With "1" live agents in directory "stage_details_with_permission" - teardown
* Using pipeline "first-pipeline,down-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


