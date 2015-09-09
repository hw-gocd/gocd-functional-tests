CreatePipelineApiSecurity
=========================

Setup of contexts
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2" - setup
* Capture go state "CreatePipelineApiSecurity" - setup

CreatePipelineApiSecurity
-------------------------

tags: 4141, group admin, api

The users in the system

Pipeline Groups - group 1
						  group 2

Role: group1AdminRole
Group Admins: group1Admin
Group Users: group1View

Admins: admin

* Logout - On Any Page

* Login as "group1Admin"

* For pipeline group "group1"
* Create pipeline "newpipeline" using template "simple-pass"

* Verify pipeline "newpipeline" is visible

* For pipeline group "group1"
* Delete pipeline "newpipeline" - Configure cruise using api

* Verify pipeline "newpipeline" is not visible

* For pipeline group "group2"
* Create pipeline "newpipeline" using template "simple-pass"
* Response should return code "401"

* Logout - On Any Page

* Login as "group1View"

* For pipeline group "group1"
* Create pipeline "newpipeline" using template "simple-pass"
response should return code "401" (currently returning "403")





Teardown of contexts
* Capture go state "CreatePipelineApiSecurity" - teardown
* Using pipeline "pipeline1, pipeline2" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


