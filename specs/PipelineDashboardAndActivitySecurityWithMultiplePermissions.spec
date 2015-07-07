PipelineDashboardAndActivitySecurityWithMultiplePermissions
===========================================================

Setup of contexts 
* Permissions configuration - setup
* Login as "admin" - setup
* Using pipeline "P8, p9" - setup
* With "1" live agents in directory "Pipeline dashboard" - setup
* Capture go state "PipelineDashboardAndActivitySecurityWithMultiplePermissions" - setup

PipelineDashboardAndActivitySecurityWithMultiplePermissions
-----------------------------------------------------------

tags: 6786, Permissions

Verify that user 'group1view' gets union of the different permissions specified to him 

* Trigger pipelines "P8" and wait for labels "1" to pass
* Trigger pipelines "P9" and wait for labels "1" to pass


* Logout - On Any Page

* Login as "group1view"


Pipeline Visibility
* PipelineVisibility
| Pipeline Name | Is Visible? | Can Operate Using Ui? | Can Operate? | Can Pause Using Ui? | Can Pause Using Api? | 
| P8 | true | true | true | true | true | 
| P9 | true | true | true | true | true | 


* verify user has operate permissions on "defaultStage" for pipeline "P8" on Pipeline Activity Page

* verify user has operate permissions on "defaultStage" for pipeline "P9" on Pipeline Activity Page


* verify user can operate stage "defaultStage" for pipeline "P8" from stage details page


* verify user can operate stage "defaultStage" for pipeline "P9" from stage details page




Teardown of contexts 
* Capture go state "PipelineDashboardAndActivitySecurityWithMultiplePermissions" - teardown
* With "1" live agents in directory "Pipeline dashboard" - teardown
* Using pipeline "P8, p9" - teardown
* Login as "admin" - teardown
* Permissions configuration - teardown


