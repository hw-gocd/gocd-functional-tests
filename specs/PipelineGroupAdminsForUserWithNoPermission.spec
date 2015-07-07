PipelineGroupAdminsForUserWithNoPermission
==========================================

Setup of contexts 
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2, pipeline3" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "PipelineGroupAdminsForUserWithNoPermission" - setup

PipelineGroupAdminsForUserWithNoPermission
------------------------------------------

tags: 4138, group admin

This scenario tests the system for a user "notInAnyRoleC" who has No Permissions on any Group
		
* Logout - On Any Page

* Login as "notInAnyRoleC"


Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate? | 
| pipeline1 | false | false | 
| pipeline2 | false | false | 
| pipeline3 | false | false | 


* Verify "cannot" operate on agents

* Verify admin link is disabled

* Verify pipeline is not visible "pipeline1"
* Verify pipeline is not visible "pipeline2"
* Verify pipeline is not visible "pipeline3"




Teardown of contexts 
* Capture go state "PipelineGroupAdminsForUserWithNoPermission" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "pipeline1, pipeline2, pipeline3" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


