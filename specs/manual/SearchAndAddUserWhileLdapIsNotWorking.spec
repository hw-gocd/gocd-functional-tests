SearchAndAddUserWhileLdapIsNotWorking
=====================================

Setup of contexts
* With no users - setup
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Capture go state "SearchAndAddUserWhileLdapIsNotWorking" - setup

SearchAndAddUserWhileLdapIsNotWorking
-------------------------------------

tags: 4169, security, Admin, 4171, manual

* logged in as "admin"

User serach should show a warning when either password search fails.
* changing ldap uri to "ldap://invalid.com"

* Login as "admin"

* open "User Summary" tab

* goto add users
* search for user "admin"
* wait for search to return results
* verify message on search popup is "Ldap search failed, please contact the administrator."





Teardown of contexts
* Capture go state "SearchAndAddUserWhileLdapIsNotWorking" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown
* With no users - teardown


