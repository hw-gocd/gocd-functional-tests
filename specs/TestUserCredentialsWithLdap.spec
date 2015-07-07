TestUserCredentialsWithLdap
===========================

Setup of contexts 
* Valid ldap configuration - setup
* Capture go state "TestUserCredentialsWithLdap" - setup

TestUserCredentialsWithLdap
---------------------------

tags: 6441, ldap

user should get logged in if valid ldap credentials are provided
* Login with username "cruise_builder" and password "BXrQ51uhU"
* User should get logged in as "Cruise Builder"


user should see error message when incorrect username is provided
* Login with username "cruise_builder1" and password "BXrQ51uhU"
* Assert login error "User cruise_builder1 not found in directory. Help Topic: Authentication"


user should see error message when incorrect password is provided
* Login with username "cruise_builder" and password "1BXrQ51uhU"
* Assert login error "Bad credentials Help Topic: Authentication"








Teardown of contexts 
* Capture go state "TestUserCredentialsWithLdap" - teardown
* Valid ldap configuration - teardown


