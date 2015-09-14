NewTurnOnSecurity
=================

Setup of contexts
* UserIsLogout - setup
* Capture go state "NewTurnOnSecurity" - setup

NewTurnOnSecurity
-----------------

tags: security, smoke, authentication, passwordfile support, dashboard, manual


Test this using both password file and with LDAP
* user "userA" is visiting pipeline wizard page
* security is turned on by admin
* then user "userA" should be redirected to login page automatically
* login as "userA"
* then user "userA" should be redirected to pipeline wizard page





Teardown of contexts
* Capture go state "NewTurnOnSecurity" - teardown
* UserIsLogout - teardown


