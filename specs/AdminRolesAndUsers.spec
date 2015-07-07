AdminRolesAndUsers
==================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "viewable-pipeline" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "AdminRolesAndUsers" - setup

AdminRolesAndUsers
------------------

tags: 1952, security, automate

* Making "pavan" an admin user
* Making "raghu" an admin user

Verify if user is admin
* VerifyIfUserIsAdmin
| login as user | admin | 
| view | false | 
| operate | false | 
| pavan | true | 
| raghu | true | 
| admin | true | 

* Logout - On Any Page

* Login as "admin"

* Removing "raghu" as an admin

* Logout - On Any Page

* VerifyIfUserIsAdmin
| login as user | admin | 
| raghu | false | 

* Login as "raghu"

* Verify pipeline "viewable-pipeline" is not visible

* Logout - On Any Page

* Login as "pavan"

* Looking at pipeline "viewable-pipeline"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"





Teardown of contexts 
* Capture go state "AdminRolesAndUsers" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "viewable-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


