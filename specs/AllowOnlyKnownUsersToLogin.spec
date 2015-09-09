AllowOnlyKnownUsersToLogin
==========================

Setup of contexts
* With no users - setup
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Capture go state "AllowOnlyKnownUsersToLogin" - setup

AllowOnlyKnownUsersToLogin
--------------------------

tags: 4168

* Allow only known users to login

* Logout - On Any Page

* Login as "view" should fail with message "Please ask the administrator to add you to Go Help Topic: Authentication"
* Login as "admin"

* Allow unknown users to login

* Logout and login as "view"





Teardown of contexts
* Capture go state "AllowOnlyKnownUsersToLogin" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown
* With no users - teardown


