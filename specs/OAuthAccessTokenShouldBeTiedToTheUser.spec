OAuthAccessTokenShouldBeTiedToTheUser
=====================================

Setup of contexts 
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1, pipeline2" - setup
* Capture go state "OAuthAccessTokenShouldBeTiedToTheUser" - setup

OAuthAccessTokenShouldBeTiedToTheUser
-------------------------------------

tags: 4248, oAuth

This scenario tests that access token should be tied to the user who approved 

* Adding "http://localhost:8253" as site uRL
* Adding "https://localhost:8254" as secure site uRL

* Logout - On any page over localhost ssl

* Login as "admin" - On Login Page Over Localhost Ssl

* Open "OAuth Clients" tab

* Delete all client entries
* Navigate to new client form

Populate OAuth Clients
* PopulateOAuthClients
| Client Name | Redirect Url | 
| client | /help/Agent_API.html | 


* Open "OAuth Clients" tab

* Remember client entries for "client"

* Logout - On Any Page

* Login as "group1Admin" - On Login Page Over Localhost Ssl

* Using "HTTPS"

* For client "client"
* Request approval
* Approve pending request
* Save authorization code
* Obtain access token

* Logout

* Login as "group2Admin" - On Login Page Over Localhost Ssl

* For client "client"
* Request approval
* Approve pending request
* Save authorization code
* Obtain access token

* Verify token "client" exists

* Logout - On Any Page

* For client "client"
* For user "group1Admin"
* Using "HTTPS"
* Gadget page for pipeline "pipeline1" should contain "pipeline_pipeline1"

* For client "client"
* For user "group2Admin"
* Using "HTTPS"
* Gadget page for pipeline "pipeline2" should contain "pipeline_pipeline2"

* Logout - On Any Page Over Hostname Ssl




Teardown of contexts 
* Capture go state "OAuthAccessTokenShouldBeTiedToTheUser" - teardown
* Using pipeline "pipeline1, pipeline2" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


