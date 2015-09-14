ServerConfigurationTabMailHost
==============================

Setup of contexts
* Basic configuration - setup
* Capture go state "ServerConfigurationTabMailHost" - setup

ServerConfigurationTabMailHost
------------------------------

tags: 4171, clicky ui, admin-page, configuration


* ConfigureMailHost 
     |Hostname                  |Port|Username|Password|TLS  |From Email             |Admin Email           |Message?                                                                                                                |
     |--------------------------|----|--------|--------|-----|-----------------------|----------------------|------------------------------------------------------------------------------------------------------------------------|
     |b+ve                      |25  |        |        |true |ccedev@thoughtworks.com|admin@thoughtworks.com|Invalid hostname. A valid hostname can only contain letters (A-z) digits (0-9) hyphens (-) dots (.) and underscores (_).|
     |chimisc01.thoughtworks.com|-1  |        |        |false|ccedev@thoughtworks.com|admin@thoughtworks.com|Invalid port.                                                                                                           |
     |chimisc01.thoughtworks.com|25  |        |        |true |ccedev                 |admin@thoughtworks.com|From address is not a valid email address.                                                                              |
     |chimisc01.thoughtworks.com|25  |        |        |true |ccedev@thoughtworks.com|admin                 |Admin address is not a valid email address.                                                                             |
     |chimisc01.thoughtworks.com|25  |pavan   |awesome |true |ccedev@thoughtworks.com|admin@thoughtworks.com|Saved configuration successfully.                                                                                       |






Teardown of contexts
* Capture go state "ServerConfigurationTabMailHost" - teardown
* Basic configuration - teardown


