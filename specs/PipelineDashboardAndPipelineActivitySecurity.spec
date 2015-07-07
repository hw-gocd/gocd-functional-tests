PipelineDashboardAndPipelineActivitySecurity
============================================

Setup of contexts 
* Permissions configuration - setup
* Login as "admin" - setup
* Using pipeline "P1, p2, p3, p4" - setup
* With "2" live agents in directory "PipelineDashboardSecurity" - setup
* Capture go state "PipelineDashboardAndPipelineActivitySecurity" - setup

PipelineDashboardAndPipelineActivitySecurity
--------------------------------------------

tags: 6786, Permissions

Verify that super-admin has all view and operate permissions

* Trigger pipelines "P1" and wait for labels "1" to pass
* Trigger pipelines "P2" and wait for labels "1" to pass
* Trigger pipelines "P3" and wait for labels "1" to pass
* Trigger pipelines "P4" and wait for labels "1" to pass



Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate Using Ui? | Can Operate? | Can Pause Using Ui? | Can Pause Using Api? | 
| P1 | true | true | true | true | true | 
| P2 | true | true | true | true | true | 
| P3 | true | true | true | true | true | 
| P4 | true | true | true | true | true | 



* verify user has operate permissions on "defaultStage" for pipeline "P1" on Pipeline Activity Page
* Verify pipeline is triggered by "admin"


* verify user has operate permissions on "defaultStage" for pipeline "P2" on Pipeline Activity Page

* verify user has operate permissions on "defaultStage" for pipeline "P3" on Pipeline Activity Page

* verify user has operate permissions on "defaultStage" for pipeline "P4" on Pipeline Activity Page


* Logout - On Any Page

* Login as "raghu"


Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate Using Ui? | Can Operate? | Can Pause Using Ui? | Can Pause Using Api? | 
| P1 | true | false | false | false | false | 
| P2 | true | true | true | true | true | 
| P3 | true | true | true | true | true | 
| P4 | false | false | true | false | true | 



* verify user does not have operate permissions on "defaultStage" for pipleine "P1" on pipeline activity page

* verify user has operate permissions on "defaultStage" for pipeline "P2" on Pipeline Activity Page

* verify user has operate permissions on "defaultStage" for pipeline "P3" on Pipeline Activity Page


* Logout - On Any Page

* Login as "pavan"


Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate Using Ui? | Can Operate? | Can Pause Using Ui? | Can Pause Using Api? | 
| P1 | true | false | false | false | false | 
| P2 | false | false | false | false | false | 
| P3 | true | true | true | true | true | 
| P4 | false | false | false | false | false | 



* verify user does not have operate permissions on "defaultStage" for pipleine "P1" on pipeline activity page


* verify user has operate permissions on "defaultStage" for pipeline "P3" on Pipeline Activity Page


* Logout - On Any Page

* Login as "group1view"


Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate Using Ui? | Can Operate? | Can Pause Using Ui? | Can Pause Using Api? | 
| P1 | false | false | true | false | true | 
| P2 | true | true | true | true | true | 
| P3 | true | false | false | true | true | 
| P4 | true | false | false | false | false | 



* verify user has operate permissions on "defaultStage" for pipeline "P2" on Pipeline Activity Page

* verify user does not have operate permissions on "defaultStage" for pipleine "P4" on pipeline activity page

* verify user does not have stage "defaultStage" operate permissions for pipleine "P3" on pipeline activity page






Teardown of contexts 
* Capture go state "PipelineDashboardAndPipelineActivitySecurity" - teardown
* With "2" live agents in directory "PipelineDashboardSecurity" - teardown
* Using pipeline "P1, p2, p3, p4" - teardown
* Login as "admin" - teardown
* Permissions configuration - teardown


