EncryptPasswords
================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Capture go state "EncryptPasswords" - setup

EncryptPasswords
----------------

tags: 3560, Encrypt Passwords, stage1

Encryption of Svn and P4 passwords taken care of in relavent tests

* Open "Server Configuration" tab

* For field "ldap_uri" "ldap://fmtdc02.corporate.thoughtworks.com"
* For field "ldap_username" "cn=Active Directory Ldap User,ou=InformationSystems,ou=SharedAccounts,ou=Principal,dc=corporate,dc=thoughtworks,dc=com"
* Verify "ldap_password" password field is "disabled" and contains "**********"
* Check change password for "ldap_password"
* Verify "ldap_password" password field is "enabled" and contains ""
* For field "ldap_password" "password"
* Verify "ldap_password" password field is "enabled" and contains "password"
* For text area field "ldap_search_base" "ou=Employees,ou=Enterprise,ou=Principal,dc=corporate,dc=thoughtworks,dc=com"
* For field "ldap_search_filter" "(sAMAccountName={0})"
* For field "hostName" "10.18.3.171"
* For field "port" "42"
* For field "username" "someone"
* Verify "password" password field is "disabled" and contains "**********"
* Check change password for "password"
* Verify "password" password field is "enabled" and contains ""
* For field "password" "password"
* Verify "password" password field is "enabled" and contains "password"
* For field "from" "crusie@cruise.com"
* For field "adminMail" "admin@cruise.com"
* Save configuration

* Open "Config XML" tab

* Verify ldap manager password as "pVyuW5ny9I6YT4Ou+KLZhQ=="
* Verify mail host password as "pVyuW5ny9I6YT4Ou+KLZhQ=="




Teardown of contexts 
* Capture go state "EncryptPasswords" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


