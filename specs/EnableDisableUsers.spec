EnableDisableUsers
==================

Setup of contexts
* With no users - setup
* Secure configuration - setup
* Login as "admin" - setup
* Capture go state "EnableDisableUsers" - setup

EnableDisableUsers
------------------

tags: #3238, Admin, Security, stage1

* Open "User Summary" tab

* Search for "pavan" and add user "1" in the search result
* Search for "raghu" and add user "1" in the search result
* Verify users "raghu,pavan" are enabled

* Disable users "pavan"
* Verify users "pavan" are disabled

* Logout - On Any Page

* Login as "pavan" should fail with message "Your account has been disabled by the administrator Help Topic: Authentication"
* Login as "admin"

* Open "User Summary" tab

* Enable users "pavan"
* Verify users "pavan" are enabled

* Logout and login as "pavan"

* Logged in as "pavan"

* Logout and login as "admin"

* Open "User Summary" tab

* Disable users "pavan,raghu"
* Verify users "pavan,raghu" are disabled

* Enable users "pavan,raghu"
* Verify users "pavan,raghu" are enabled

* Making "pavan" an admin user

* Open "User Summary" tab

* Disable users "admin,pavan,raghu"
* Verify error message "Did not disable any of the selected users. Ensure that all configured admins are not being disabled." is displayed





Teardown of contexts
* Capture go state "EnableDisableUsers" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown
* With no users - teardown


