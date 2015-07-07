EditExistingTemplateAndViewTemplate
===================================

Setup of contexts 
* Template admin configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1,pipeline2,pipeline3,pipeline4,pipeline5,pipeline-without-template" - setup
* Capture go state "TemplatesViewerAndEditor" - setup

EditExistingTemplateAndViewTemplate
-----------------------------------

tags: 4600, Clicky Admin, 7862

* Open "Templates" tab

* Verify that templates "simple-pass" are present
* Verify that template "simple-pass" is used by pipelines "pipeline1,pipeline2,pipeline3"
* Edit template "simple-pass"

* Verify template being edited is "simple-pass"
* Verify template name "simple-pass" cannot be edited
* Open stages tab

* Open new add stage details page

* Enter for stage name "defaultStage2"
* Enter for job name "defaultJob2"
* Select "Ant" as task type
* Add stage

* Open new add stage details page

* Enter for stage name "defaultStage3"
* Enter for job name "defaultJob3"
* Select "Ant" as task type
* Add stage

* Verify the stages are "defaultStage,defaultStage2,defaultStage3"
* Delete stage "defaultStage2" and confirm deletion
* Delete stage "defaultStage"
* Verify global error message "Stage with name 'defaultStage' does not exist on pipeline " for pipeline "'${runtime_name:pipeline1}'" shows up

* Open stage "defaultStage3"

* Set stage name as "another Stage"
* Click save - Already on Edit Stage Page
* Verify save failed
* Verify error message "Invalid stage name 'another Stage'. This must be alphanumeric and can contain underscores and periods (however, it cannot start with a period). The maximum allowed length is 255 characters." is shown

* Logout and login as "group1Admin"

* Open "Pipelines" tab

* Edit pipeline "pipeline1"

* Verify template "simple-pass" used by pipeline is not editable
* Open view template popup

* Verify template name is "simple-pass"
* Verify clicking on stage "defaultStage" which is stage "1" of the template shows the correct stage on right pane
* Verify clicking on job "defaultJob" which is job "1" in stage "defaultStage" which is stage "1" of the template shows the correct job on the right pane
* Verfiy clicking on breadcrumb for job number "1" for stage "defaultStage" which is stage "1" of template goes back to stage details
* Verify clicking on stage "defaultStage3" which is stage "2" of the template shows the correct stage on right pane
* Close popup - Already on view template popup

* Open "Pipelines" tab

* Edit pipeline "pipeline5"

* Verify pipeline uses template "template-admin-pipeline"

* Open "Templates" tab


* Verify that templates "unused-template" are present
* Verify cannot delete templates "unused-template"
* Verify cannot add new template for template admin
* Verify that template "unused-template" has message "No pipelines associated with this template"


* Verify that templates "simple-pass" are not present
* Verify that templates "template-admin-pipeline" are present
* Verify cannot delete templates "template-admin-pipeline"
* Verify message "This template is used in 2 pipelines" for template "template-admin-pipeline"
* Edit template "template-admin-pipeline"

* Verify template being edited is "template-admin-pipeline"
* Open stages tab

* Open new add stage details page

* Enter for stage name "defaultStage2"
* Enter for job name "defaultJob2"
* Select "Ant" as task type
* Add stage

* Logout and login as "view"

* Navigate to admin templates tab

* Verify that templates "unused-template" are present
* Verify cannot delete templates "unused-template"
* Verify cannot add new template for template admin
* Verify that template "unused-template" has message "No pipelines associated with this template"


* Logout and login as "admin"

* Open "Templates" tab

* Edit template "template-admin-pipeline"

* Open stages tab

* Verify the stages are "default.stage, defaultStage2"

* Open "Templates" tab

* Delete template "unused-template"


* Logout and login as "group1Admin"

* Verify templates are visible

* Logout and login as "view"

* Verify templates tab is not visible




Teardown of contexts 
* Capture go state "TemplatesViewerAndEditor" - teardown
* Using pipeline "pipeline1,pipeline2,pipeline3,pipeline4,pipeline5,pipeline-without-template" - teardown
* Login as "admin" - teardown
* Template admin configuration - teardown


