SearchAndAddUser
================

Setup of contexts
* With no users - setup
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* With "0" live agents in directory "null" - setup
* Capture go state "SearchAndAddUser" - setup

SearchAndAddUser
----------------

tags: 4169, security, Admin, linux, ldap


* Open "User Summary" tab

* Goto add users
* Search for user "ps"
* Wait for search to return results
* Add first user in results
* Verify added user successfully

Add user with dot in its name
* Goto add users
* Search for user "user."
* Wait for search to return results
* Add first user in results
* Verify added user successfully

User already existing
* Goto add users
* Search for user "ps"
* Wait for search to return results
* Add first user in results
* Verify user addition failed

User search text length limit
* Goto add users
* Search for user "p"
* Wait for search to return results
* Verify message on search popup is "Please use a search string that has at least two (2) letters."

User search result limit
* Goto add users
* Search for user "thoughtworks"
* Wait for search to return results
* Verify message on search popup is "Too many matches found, not all results are being shown."

User under both ldap and password file must be shown
* Goto add users
* Search for user "admin"
* Wait for search to return results
* Verify "LDAP" results are displayed
* Verify "Password File" results are displayed

* Moving password file to tmp

* Goto add users
* Search for user "admin"
* Wait for search to return results
* Verify message on search popup is "Password file search failed, please contact the administrator."

YOU NEED TO RESTORE PASSWORD FILE PATH NOW, IF YOU WANT TO CONTINUE AFTER THIS. DO THAT THROUGH THE UI





Teardown of contexts
* Capture go state "SearchAndAddUser" - teardown
* With "0" live agents in directory "null" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown
* With no users - teardown


