EnvironmentsConfigMergeConflict
===============================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Capture go state "EnvironmentsConfigMergeConflict" - setup

EnvironmentsConfigMergeConflict
-------------------------------

tags: 7302

* Click add new environment link

* Enter name "EV1"
* Click "Next" button in "env-name"
* Select pipelines "basic-pipeline"
* Click "Next" button in "env-pipelines"
* Select agent "missing-agent"
* Click "Next" button in "env-agents"
* Click "FINISH" button in "env-vars"

* Verify on environments page
* Looking at "EV1" environment
* Click edit environment link for "EV1"

* Click on edit pipelines

* Verify title of modal box is "Pipelines"
* Remember md5

* Adding pipeline "basic-pipeline-run-till-file-exists" to "EV1" environment - Configure cruise Using Api

* Select pipelines "basic-pipeline-fast"
* UnSelect pipelines "basic-pipeline"
* Click on save - Already on Add Environment Page
* Verify error message "Failed to update environment 'EV1'. Configuration file has been modified by someone else. " is present - Already on Add Environment Page
* Verify md5 is same

* Verify on environments page
* Looking at "EV1" environment
* Click edit environment link for "EV1"

* Verify values "${runtime_name:basic-pipeline-run-till-file-exists}" are shown in section "added_pipelines"
* Click on edit agents

* Verify title of modal box is "Agents"
* Select agent "denied-agent"

* Adding pipeline "downstream-pipeline" to "EV1" environment - Configure cruise Using Api

* Click on save - Already on Add Environment Page

* Verify message "Updated environment 'EV1'. The configuration was modified by someone else, but your changes were merged successfully." is present
* Verify values "${runtime_name:basic-pipeline-run-till-file-exists},${runtime_name:downstream-pipeline}" are shown in section "added_pipelines"
* Verify values "denied-agent (10.232.3.2), missing-agent (10.232.3.1)" are shown in section "added_agents"
* Click on edit pipelines

* Select pipelines "abyss"

* For pipeline group "diamond-dependency"
* Delete pipeline "abyss" - Configure cruise using api

* Click on save - Already on Add Environment Page
* Verify error message is valid "Failed to update environment 'EV1'. Environment 'EV1' refers to an unknown pipeline ${runtime_name:abyss}"











Teardown of contexts 
* Capture go state "EnvironmentsConfigMergeConflict" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


