EnvironmentsScreenPermissions
=============================

Setup of contexts
* SecureConfiguration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline,admin-pipeline,environment-pipeline,basic-pipeline-slow" - setup
* Capture go state "EnvironmentsScreenPermissions" - setup

EnvironmentsScreenPermissions
-----------------------------

tags: 2808, environment, UI, automate


* Adding pipeline "basic-pipeline" to "uat" environment
* Adding pipeline "admin-pipeline" to "uat" environment

* Looking at "uat" environment
* Verify pipeline is visible "basic-pipeline"
* Verify pipeline is visible "admin-pipeline"
* Verify pipeline is visible "environment-pipeline"
* Verify pipeline is not visible "basic-pipeline-slow"
* Verify "basic-pipeline" status is "No historical data"

* Remove pipeline "basic-pipeline" from environment

* Looking at "uat" environment
* Verify pipeline is not visible "basic-pipeline"

* Logout - On Any Page

* Login as "view"

* Looking at "uat" environment
* Verify pipeline is visible "environment-pipeline"
* Verify pipeline is not visible "admin-pipeline"






Teardown of contexts
* Capture go state "EnvironmentsScreenPermissions" - teardown
* Using pipeline "basic-pipeline,admin-pipeline,environment-pipeline,basic-pipeline-slow" - teardown
* Login as "admin" - teardown
* SecureConfiguration - teardown


