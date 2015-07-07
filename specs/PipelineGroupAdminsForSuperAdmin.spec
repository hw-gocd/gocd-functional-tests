PipelineGroupAdminsForSuperAdmin
================================

Setup of contexts 
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2, pipeline3" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "PipelineGroupAdminsForSuperAdmin" - setup

PipelineGroupAdminsForSuperAdmin
--------------------------------

tags: 4138, group admin

This scenario tests the system for a Super Admin.


Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate? | 
| pipeline1 | true | true | 
| pipeline2 | true | true | 
| pipeline3 | true | true | 


* Verify source xml is visible
* Verify server configuration is visible
* Verify user summary is visible
* Verify templates are visible
* Open "Pipelines" tab

* Verify groups "group1, group2, group3" are visible
* Verify "group1" has pipelines "pipeline1"
* Verify "group2" has pipelines "pipeline2"
* Verify "group3" has pipelines "pipeline3"

* Verify "can" operate on agents

* Verify pipeline is visible "pipeline1"
* Verify pipeline is visible "pipeline2"
* Verify pipeline is visible "pipeline3"




Teardown of contexts 
* Capture go state "PipelineGroupAdminsForSuperAdmin" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "pipeline1, pipeline2, pipeline3" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


