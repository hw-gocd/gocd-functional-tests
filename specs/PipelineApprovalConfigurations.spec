PipelineApprovalConfigurations
==============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "edit-pipeline, autoFirst" - setup
* Capture go state "PipelineApprovalConfigurations" - setup

PipelineApprovalConfigurations
------------------------------

tags: 7078

Automatic pipeline scheduling for general pipelines
* Click on pipeline "edit-pipeline" for editing

* Verify auto scheduling is set to "false"
* Update auto scheduling to "true"
* Click save - Already On General Options Page
* Verify saved successfully - Already On General Options Page
* Open stage listing page

* Open stage "defaultStage"

* Verify aproval type is set to "auto"
* Change approval type to "manual"
* Click save - Already on Edit Stage Page
* Verify that stage saved successfully - Already on edit stage page

* Click on pipeline "edit-pipeline" for editing

* Verify auto scheduling is set to "false"

Automatic pipeline scheduling for pipeline using template

* Click on pipeline "autoFirst" for editing

* Verify auto scheduling is set to "true"
* Verify auto scheduling checkbox is disabled

* Open "Templates" tab

* Edit template "autoStagePipelineTemplate"

* Open stages tab

* Open stage "defaultStage"

* Verify aproval type is set to "auto"
* Change approval type to "manual"
* Click save - Already on Edit Stage Page
* Verify that stage saved successfully - Already on edit stage page

* Click on pipeline "autoFirst" for editing

* Verify auto scheduling is set to "false"
* Verify auto scheduling checkbox is disabled




Teardown of contexts
* Capture go state "PipelineApprovalConfigurations" - teardown
* Using pipeline "edit-pipeline, autoFirst" - teardown
* Basic configuration - teardown


