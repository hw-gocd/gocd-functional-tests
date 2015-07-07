AssociateUsersWithRoles
=======================

Setup of contexts 
* With no users - setup
* Secure configuration - setup
* Login as "admin" - setup
* Capture go state "AssociateUsersWithRoles" - setup

AssociateUsersWithRoles
-----------------------

tags: 4170, admin, role

* Open "User Summary" tab

* Search for "pavan" and add user "1" in the search result
* Search for "raghu" and add user "1" in the search result
* Search for "operate" and add user "1" in the search result

* Toggle selection of users "pavan,raghu"
* Select role states "viewer:add"
* Apply changes to roles and verify message "Role(s)/Admin-Privilege modified for 2 user(s) successfully."
* Verify users "pavan,raghu,operate" are assigned role "viewer"
* Toggle selection of users "operate"
* Select role states "viewer:add"
* Apply changes to roles and verify message "Role(s)/Admin-Privilege modified for 1 user(s) successfully."
* Verify users "pavan,raghu" are assigned role "viewer"

* Toggle selection of users "pavan"
* Add role "new-role"
* Apply changes to roles and verify message "New role assigned"
* Verify users "pavan" are assigned role "new-role"
* Toggle selection of users "pavan"
* Add role ".new*$%role"
* Apply changes to roles and verify message "Failed to add role. Reason - "

Tristate checks
pavan -> new-role, viewer
raghu -> viewer

* Toggle selection of users "pavan,raghu"
* Select role states "operator:add"
* Apply changes to roles and verify message "Role(s)/Admin-Privilege modified for 2 user(s) successfully."
* Verify users "pavan" are assigned role "new-role,viewer,operator"
* Verify users "raghu" are assigned role "viewer,operator"
* Verify users "raghu" does not have the role "new-role"




Teardown of contexts 
* Capture go state "AssociateUsersWithRoles" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown
* With no users - teardown


