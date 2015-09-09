AccessingAUrlAsAnOAuthClient
============================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Capture go state "AccessingAUrlAsAnOAuthClient" - setup

AccessingAUrlAsAnOAuthClient
----------------------------

tags: 4248, oAuth, windows

* Logout and login as "view"
* Verify "/go/admin/oauth/clients" returns "403"

* Logout

* Login as "admin"

* Open "Server Configuration" tab

* Verify text field "siteUrl" has value ""
* Verify text field "secureSiteUrl" has value ""
* Set field "siteUrl" to "http://localhost:8253"
* Set field "secureSiteUrl" to "https://localhost:8254"
* Save configuration
* Verify message "Saved configuration successfully." shows up

* Logout - On Any Page

* Login as "admin" - On Login Page Over Localhost Ssl

* Open "OAuth Clients" tab

* Delete all client entries
* Navigate to new client form

Populate OAuth Clients
* PopulateOAuthClients 
     |Client Name |Redirect Url            |
     |------------|------------------------|
     |twist-client|/dummy_not_in_production|


* Open "OAuth Clients" tab

* Remember client entries for "twist-client"

* For client "twist-client"
* Request approval
* Approve pending request
* Save authorization code
* Using "HTTPS"
* Obtain access token
* Gadget page for pipeline "basic-pipeline" should contain "No historical data"
* "/pipelines" Should return code "403"





Teardown of contexts
* Capture go state "AccessingAUrlAsAnOAuthClient" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


