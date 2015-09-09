ApiPausePipeline
================

Setup of contexts
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1" - setup
* Capture go state "ApiPausePipeline" - setup

ApiPausePipeline
----------------

tags: #5839, api, pipeline

Pipeline Groups - group 1
						  group 2
Role: group1AdminRole
Group Admins: group1Admin
Group Users: group1View
Admins: admin

* Attempt to pause pipline "pipeline1" with cause "twist testing it" and should return with http status "200"

* Looking at pipeline "pipeline1"
* Verify pipeline is paused with reason "twist testing it" by "admin"

* Attempt to unpause pipeline "pipeline1" and should return with http status "200"

* Looking at pipeline "pipeline1"
* Verify pipeline is unpaused

* Attempt to pause pipline "pipeline1" with cause "twist testing it - second pause to test with view only user" and should return with http status "200"

* Logout - On Any Page

* Login as "group1View"

* Attempt to pause pipline "pipeline1" with cause "twist testing it - user has view only" and should return with http status "401"
* Attempt to unpause pipeline "pipeline1" and should return with http status "401"
* Attempt to pause non existent pipline "non-existent-pipeline" with cause "twist testing it" and should return with http status "404"
* Attempt to unpause non existent pipline "non-existent-pipeline" and should return with http status "404"





Teardown of contexts
* Capture go state "ApiPausePipeline" - teardown
* Using pipeline "pipeline1" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


