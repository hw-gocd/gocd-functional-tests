AdministrationApiSecurity
=========================

Setup of contexts
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2, pipeline3" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "AdministrationApiSecurity" - setup

AdministrationApiSecurity
-------------------------

tags: 4141, administration, api, group admin

This scenario ensures that a Pipeline group admin can make another user an admin of the group. Also, ensure that Super user can remove a pipeline group admin.

Setup

The users in the system

Role: group1AdminRole
Group Admins: group1Admin

Admins: admin

Users Not in Roles
		notInAnyRoleA

* Logout - On Any Page

* Login as "group1Admin"

* For pipeline group "group1"
* Making user "notInAnyRoleA" admin

* Logout - On Any Page

* Login as "notInAnyRoleA"

* For pipeline "pipeline1" - Using pipeline api
* Schedule should return code "202"

* Logout - On Any Page

* Login as "admin"

* For pipeline group "group2"
* Removing role "group2AdminRole" from being an admin

* Logout - On Any Page

* Login as "group2Admin"

* For pipeline "pipeline2" - Using pipeline api
* Schedule should return code "401"

* Logout - On Any Page




Teardown of contexts
* Capture go state "AdministrationApiSecurity" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "pipeline1, pipeline2, pipeline3" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


