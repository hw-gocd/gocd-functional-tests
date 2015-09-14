ServerConfigurationTabUserManagement
====================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Capture go state "ServerConfigurationTabUserManagement" - setup

ServerConfigurationTabUserManagement
------------------------------------

tags: 4171, clicky ui, admin-page, configuration, ldap

* Open "Server Configuration" tab

Password Settings
* Set password file path to only admin password properties
* Save configuration

* Logout - On Any Page

* Login as "view" should fail with message "User view not found in directory. Help Topic: Authentication"
* Login as "admin"

LDAP Settings
* Open "Server Configuration" tab

* ConfigureMailHost 
     |URI                                      |Ldap Username|Ldap Password|Search Base                                                                |Search  Filter      |message?                         |
     |-----------------------------------------|-------------|-------------|---------------------------------------------------------------------------|--------------------|---------------------------------|
     |ldap://fmtdc02.corporate.thoughtworks.com|foo          |bar          |ou=Employees,ou=Enterprise,ou=Principal,dc=corporate,dc=thoughtworks,dc=com|(sAMAccountName={0})|Saved configuration successfully.|

* Set field "ldap_uri" to "ldap://bad-server"
* Validate ldap should return "Cannot connect to ldap, please check the settings. Reason: bad-server:389; nested exception is javax.naming.CommunicationException: bad-server:389 [Root exception is java.net.UnknownHostException: bad-server]"







Teardown of contexts
* Capture go state "ServerConfigurationTabUserManagement" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


