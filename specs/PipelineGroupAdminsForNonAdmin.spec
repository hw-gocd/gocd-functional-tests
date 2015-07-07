PipelineGroupAdminsForNonAdmin
==============================

Setup of contexts 
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2,pipeline3" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "PipelineGroupAdminsForNonAdmin" - setup

PipelineGroupAdminsForNonAdmin
------------------------------

tags: 4138, group admin

The user "notInAnyRoleA" does not have admin permissions anywhere in config.
He has view permission for group2 and operate permission for group3.

* Logout - On Any Page


* Login as "notInAnyRoleA"

Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate? | 
| pipeline1 | false | false | 
| pipeline2 | true | false | 
| pipeline3 | false | true | 


* Verify admin link is disabled

* Verify "cannot" operate on agents

* Verify pipeline is not visible "pipeline1"
* Verify pipeline is visible "pipeline2"
* Verify pipeline is not visible "pipeline3"





Teardown of contexts 
* Capture go state "PipelineGroupAdminsForNonAdmin" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "pipeline1, pipeline2,pipeline3" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


