OAuthCRUDOperations
===================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Capture go state "OAuthCRUDOperations" - setup

OAuthCRUDOperations
-------------------

tags: 4248, oAuth, only_this

This tests the CRUD operations on an OAuth client. Only an admin can perform these operations

* Adding "http://localhost:8253" as site uRL
* Adding "https://localhost:8254" as secure site uRL

* Logout - On any page over localhost ssl

* Login as "admin" - On Login Page Over Localhost Ssl

* Open "OAuth Clients" tab

* Delete all client entries
* Navigate to new client form

* Using client name "twist-client"
* Using redirect url "http://bar.quux"
* Add new auth client

* Verify table shows "http://bar.quux" as redirect uri for "twist-client"
* Edit client named "twist-client"

* Change redirect url to "http://something.changed"
* Update this client

* Verify table shows "http://something.changed" as redirect uri for "twist-client"
* Delete "twist-client" entry
* Verify "twist-client" does not show

* Logout - On Any Page

* Login as "view"

* Verify "/go/admin/oauth/clients" returns "403"

* Logout - On Any Page Over Hostname Ssl





Teardown of contexts 
* Capture go state "OAuthCRUDOperations" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


