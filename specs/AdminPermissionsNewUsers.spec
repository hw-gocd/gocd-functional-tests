AdminPermissionsNewUsers
========================

Setup of contexts 
* Basic configuration - setup
* Logout on exit - setup
* Capture go state "AdminPermissionsNewUsers" - setup

AdminPermissionsNewUsers
------------------------

tags: 6785, Admin


* Add security with password file only

Verify if user is admin
* VerifyIfUserIsAdmin
| login as user | admin | 
| pavan | true | 
| raghu | true | 
| admin | true | 


* Logout - On Any Page

* Login as "admin"

* Open "User Summary" tab

* Verify users "raghu,pavan,admin" are enabled









Teardown of contexts 
* Capture go state "AdminPermissionsNewUsers" - teardown
* Logout on exit - teardown
* Basic configuration - teardown


