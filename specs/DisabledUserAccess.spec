DisabledUserAccess
==================

Setup of contexts
* With no users - setup
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* With "1" live agents in directory "disabled_users" - setup
* Capture go state "DisabledUserAccess" - setup

DisabledUserAccess
------------------

tags: #3238, Admin, Security

* Open "User Summary" tab

* Search for "operate" and add user "1" in the search result
* Search for "group1View" and add user "1" in the search result
* Verify users "operate, group1View" are enabled

* Logout and login as "operate"

* For pipeline "basic-pipeline" - Using pipeline api
* Schedule should return code "202"

* Looking at pipeline "basic-pipeline"
* Verify stage "1" is "Passed" on pipeline with label "1"

* Logout and login as "admin"

* Open "User Summary" tab

* Disable users "operate"
* Verify users "operate" are disabled

* Login as "operate" should fail with message "Your account has been disabled by the administrator Help Topic: Authentication"

* Logged in as "operate"

* For pipeline "basic-pipeline" - Using pipeline api
* Schedule should return code "401"






Teardown of contexts
* Capture go state "DisabledUserAccess" - teardown
* With "1" live agents in directory "disabled_users" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown
* With no users - teardown


