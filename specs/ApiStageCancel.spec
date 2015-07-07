ApiStageCancel
==============

Setup of contexts 
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1" - setup
* Capture go state "ApiStageCancel" - setup

ApiStageCancel
--------------

tags: api, stage, 5849

Pipeline Groups - group 1 
						  group 2
Role: group1AdminRole
Group Admins: group1Admin
Group Users: group1View
Admins: admin

* Looking at pipeline "pipeline1"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "first" of run "1"

* Attempt to cancel running stage "first" of the current running pipeline should return with status "200"

* Verify stage "first" has action "Rerun"


* Attempt to cancel stage "first" of the given pipeline "pipeline1" should return with status "200"

* Looking at pipeline "pipeline1"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "2"
* Navigate to stage "first" of run "2"

* Attempt to cancel running stage "second" of the current running pipeline should return with status "404"
* Attempt to cancel stage of a non existing pipeline should return with status "404"

* Logout - On Any Page

* Login as "group1View"

* Attempt to cancel running stage "first" of the current running pipeline should return with status "401"




Teardown of contexts 
* Capture go state "ApiStageCancel" - teardown
* Using pipeline "pipeline1" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


