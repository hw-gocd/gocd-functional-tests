PipelineDashboardAndPipelineActivitySecurityAtStageLevel
========================================================

Setup of contexts 
* Permissions configuration - setup
* Login as "admin" - setup
* Using pipeline "P5, p6,P7" - setup
* With "2" live agents in directory "PipelineDashboardSecurity" - setup
* Capture go state "PipelineDashboardAndPipelineActivitySecurityAtStageLevel" - setup

PipelineDashboardAndPipelineActivitySecurityAtStageLevel
--------------------------------------------------------

tags: 6786, Permissions

* Trigger pipelines "P5" and wait for labels "1" to pass
* Trigger pipelines "P6" and wait for labels "1" to pass
* Trigger pipelines "P7" and wait for labels "1" to pass


* Logout - On Any Page

* Login as "raghu"

Pipeline Visibility
* PipelineVisibility
| pipeline name | is visible? | can operate using ui? | can operate? | can pause using ui? | can pause using api? | 
| P5 | true | true | true | true | true | 
| P6 | true | true | true | true | true | 
| P7 | true | false | false | true | true | 



* verify user has operate permissions on "defaultStage" for pipeline "P5" on Pipeline Activity Page


* verify user has operate permissions on "firstStage" for pipeline "P6" on Pipeline Activity Page
* Verify "secondStage" can be approved
* Approve stage "secondStage"


* verify user does not have stage "firstStage" operate permissions for pipleine "P7" on pipeline activity page
* Verify "secondStage" can be approved
* Approve stage "secondStage"

* Logout - On Any Page

* Login as "pavan"


Behavior of P7 is similar for user 'pavan' and 'raghu', hence not verified
Pipeline Visibility
* PipelineVisibility
| pipeline name | is visible? | can operate using ui? | can operate? | can pause using ui? | can pause using api? | 
| P5 | true | false | false | true | true | 
| P6 | true | true | true | true | true | 



* Looking at pipeline "P5"
* Click on pipeline name
* Looking at pipeline with label "1"
* Verify stage "defaultStage" of pipeline cannot be rerun
* Pause pipeline on activity page


* Verify pipeline is paused by "pavan"
* Unpause pipeline
* verify user has operate permissions on "firstStage" for pipeline "P6" on Pipeline Activity Page


* Looking at pipeline "P6"
* Click on pipeline name
* Looking at pipeline with label "1"
* Verify stage "secondStage" of pipeline cannot be rerun


* Looking at pipeline "P6"
* Click on pipeline name

* Looking at pipeline with label "2"
* Verify "secondStage" cannot be approved

* Logout - On Any Page

* Login as "group1view"

Pipeline Visibility
* PipelineVisibility
| pipeline name | is visible? | can operate using ui? | can operate? | can pause using ui? | can pause using api? | 
| P5 | true | true | true | true | true | 
| P6 | true | true | true | true | true | 
| P7 | true | true | true | true | true | 


* verify user has operate permissions on "defaultStage" for pipeline "P5" on Pipeline Activity Page

* verify user does not have stage "secondStage" operate permissions for pipleine "P6" on pipeline activity page


* Looking at pipeline "P6"
* Click on pipeline name

* Looking at pipeline with label "2"
* Verify "secondStage" cannot be approved

* verify user has operate permissions on "firstStage" for pipeline "P7" on Pipeline Activity Page
* Verify stage "secondStage" of pipeline can be rerun
* Rerun stage "secondStage" - Already On Pipeline History Page
* Verify "secondStage" stage can be cancelled






Teardown of contexts 
* Capture go state "PipelineDashboardAndPipelineActivitySecurityAtStageLevel" - teardown
* With "2" live agents in directory "PipelineDashboardSecurity" - teardown
* Using pipeline "P5, p6,P7" - teardown
* Login as "admin" - teardown
* Permissions configuration - teardown


