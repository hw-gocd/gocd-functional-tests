PipelineGroupAdminsExtractTemplatePermission
============================================

Setup of contexts
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-with-group-and-stage-security" - setup
* Capture go state "PipelineGroupAdminExtractTemplatePermission" - setup

PipelineGroupAdminsExtractTemplatePermission
--------------------------------------------

tags: group admin, 4138

User pavan is the pipeline Group Admin. He should not see Extract Template.

* Open "Pipelines" tab

* Verify that extract template is visible and enabled for "pipeline-with-group-and-stage-security"

* Logout - On Any Page

* Login as "pavan"

* Open "Pipelines" tab

* Verify that extract template is not visible for "pipeline-with-group-and-stage-security"




Teardown of contexts
* Capture go state "PipelineGroupAdminExtractTemplatePermission" - teardown
* Using pipeline "pipeline-with-group-and-stage-security" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


