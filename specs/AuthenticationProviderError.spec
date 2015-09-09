AuthenticationProviderError
===========================

Setup of contexts
* Invalid ldap configuration - setup
* Capture go state "AuthenticationProviderError" - setup

AuthenticationProviderError
---------------------------

tags: 6441, #6441

DNS error for Ldap server
* Login as "anything" should fail with message "Failed to authenticate with your authentication provider. Please check if your authentication provider is up and available to serve requests. Help Topic: Authentication"





Teardown of contexts
* Capture go state "AuthenticationProviderError" - teardown
* Invalid ldap configuration - teardown


