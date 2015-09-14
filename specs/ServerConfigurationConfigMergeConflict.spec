ServerConfigurationConfigMergeConflict
======================================

Setup of contexts
* Secure configuration - setup
* Login as "Admin" - setup
* Capture go state "ServerConfigurationConfigMergeConflict" - setup

ServerConfigurationConfigMergeConflict
--------------------------------------

tags: 7294, enterprise

* Open "Server Configuration" tab

* Open "Server Configuration" tab

* Reload page - Already on Server Configuration Tab
* Remember current tab - Already on Server Configuration Tab
* Remember md5 - Already on Server Configuration Tab
* Set field "hostName" to "chimisc01.thoughtworks.com"
* Set field "port" to "25"
* Set field "username" to "pavan"
* Set field "from" to "ccedev@thoughtworks.com"
* Set field "adminMail" to "admin@thoughtworks.com"

* For template "simple-pass"
* For stage "defaultStage"
* For job "defaultJob"
* Add custom command "ls"

* Save configuration
* Verify message contains "Saved configuration successfully. The configuration was modified by someone else, but your changes were merged successfully."








Teardown of contexts
* Capture go state "ServerConfigurationConfigMergeConflict" - teardown
* Login as "Admin" - teardown
* Secure configuration - teardown


