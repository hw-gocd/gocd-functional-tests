UserAPI
=======

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Capture go state "UserAPI" - setup

UserAPI
-------

tags: 7478, api, users

* Open "User Summary" tab

* Add and verify "operate"
* Add and verify "operatorUser"
* Add and verify "notInAnyRoleA"

* Attempt to delete "operate" user and should return "400"
* Attempt to delete "operatorUser" user and should return "400"

* Disable users "operate, operatorUser"
* Verify users "operate, operatorUser" are disabled

* Attempt to delete "operate" user and should return "200"
* Attempt to delete "operatorUser" user and should return "200"
* Attempt to delete "non_existent-user" user and should return "404"

* Logout and login as "view"

* Attempt to delete "notInAnyRoleA" user and should return "401"

* Logout - On Any Page




Teardown of contexts 
* Capture go state "UserAPI" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


