OAuthScenariosWhenClientIsRemoved
=================================

Setup of contexts 
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2" - setup
* Capture go state "OAuthScenariosWhenClientIsRemoved" - setup

OAuthScenariosWhenClientIsRemoved
---------------------------------

tags: 4248, oAuth

* Add site uRL
* Add secure site uRL

* Logout - On any page over localhost ssl

* Login as "admin" - On Login Page Over Localhost Ssl

* Open "OAuth Clients" tab

* Delete all client entries
* Navigate to new client form

Populate OAuth Clients
* PopulateOAuthClients
| Client Name | Redirect Url | 
| group1-client | /help/Agent_API.html | 


* Open "OAuth Clients" tab

The case where the client is deleted before authenticating

* Remember client entries for "group1-client"
* Delete "group1-client" entry

* Using "HTTPS"

* For client "group1-client"
* Verify requesting approval redirects to "/help/Agent_API.html" and returns with error "invalid-client-id"

Populate OAuth Clients
* PopulateOAuthClients
| Client Name | Redirect Url | 
| group1-client | /help/Agent_API.html | 

* Remember client entries for "group1-client"

* For client "group1-client"
* Request approval
* Approve pending request
* Save authorization code

* Open "OAuth Clients" tab

* Delete "group1-client" entry

* For client "group1-client"
* Verify obtaining access token returns error message "invalid-client-credentials" and status "400"

* Logout - On any page over localhost ssl

* Logout - On Any Page Over Hostname Ssl




Teardown of contexts 
* Capture go state "OAuthScenariosWhenClientIsRemoved" - teardown
* Using pipeline "pipeline1, pipeline2" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


