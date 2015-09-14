PropertiesSecurityWithStageOverriding
=====================================

Setup of contexts
* Permissions configuration - setup
* Login as "admin" - setup
* Using pipeline "P3,P5,P6" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "PropertiesSecurityWithStagOverriding" - setup

PropertiesSecurityWithStageOverriding
-------------------------------------

tags: 6786, Permissions

* Trigger pipelines "P3" and wait for labels "1" to pass
* Trigger pipelines "P5" and wait for labels "1" to pass
* Trigger pipelines "P6" and wait for labels "1" to pass
* Click on pipeline name
* Looking at pipeline with label "1"
* Approve stage "secondStage"


verify raghu can add properties on all stages of all pipelines
* Logout and login as "raghu"

* verify property "prop_name_api_1" with value "prop_value_api_1" for pipeline "P3" stage "defaultStage" label "1" counter "1" job "defaultJob" can be added

* verify property "prop_name_api_2" with value "prop_value_api_2" for pipeline "P6" stage "firstStage" label "1" counter "1" job "defaultJob" can be added

* verify property "prop_name_api_3" with value "prop_value_api_3" for pipeline "P6" stage "secondStage" label "1" counter "1" job "secondJob" can be added


verify pavan cannot add property for secondstage of pipeline P6
* Logout and login as "pavan"

* Looking at pipeline "P3"
* Navigate to stage "defaultStage" of run "1" having counter "1"
* Navigate to job "defaultJob"
* Verify properties tab shows value "prop_value_api_1" for property "prop_name_api_1"

* Looking at pipeline "P6"
* Navigate to stage "firstStage" of run "1" having counter "1"
* Navigate to job "defaultJob"
* Verify properties tab shows value "prop_value_api_2" for property "prop_name_api_2"

commented line verification to be put back after #6827 or #6809 is fixed
* Looking at pipeline "P6"
* Navigate to stage "secondStage" of run "1" having counter "1"
* Navigate to job "secondJob"
* Verify properties tab shows value "prop_value_api_3" for property "prop_name_api_3"

* verify property "prop_name_api_4" with value "prop_value_api_4" for pipeline "P3" stage "defaultStage" label "1" counter "1" job "defaultJob" can be added

* verify property "prop_name_api_5" with value "prop_value_api_5" for pipeline "P6" stage "firstStage" label "1" counter "1" job "defaultJob" can be added

* verify property "prop_name_api_6" with value "prop_value_api_6" for pipeline "P6" stage "secondStage" label "1" counter "1" job "secondJob" cannot be added


* Logout and login as "group1view"

* Looking at pipeline "P6"
* Navigate to stage "firstStage" of run "1" having counter "1"
* Navigate to job "defaultJob"
* Verify properties tab shows value "prop_value_api_2" for property "prop_name_api_2"
* Verify properties tab shows value "prop_value_api_5" for property "prop_name_api_5"

commented line verification to be put back after #6827 or #6809 is fixed
* Looking at pipeline "P6"
* Navigate to stage "secondStage" of run "1" having counter "1"
* Navigate to job "secondJob"
* Verify properties tab shows value "prop_value_api_3" for property "prop_name_api_3"

* verify property "prop_name_api_5" with value "prop_value_api_5" for pipeline "P5" stage "defaultStage" label "1" counter "1" job "defaultJob" can be added

* verify property "prop_name_api_6" with value "prop_value_api_6" for pipeline "P6" stage "firstStage" label "1" counter "1" job "defaultJob" can be added

* verify property "prop_name_api_61" with value "prop_value_api_61" for pipeline "P6" stage "secondStage" label "1" counter "1" job "secondJob" cannot be added






Teardown of contexts
* Capture go state "PropertiesSecurityWithStagOverriding" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "P3,P5,P6" - teardown
* Login as "admin" - teardown
* Permissions configuration - teardown


