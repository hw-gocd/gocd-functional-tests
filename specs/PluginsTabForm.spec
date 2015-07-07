PluginsTabForm
==============

Setup of contexts 
* Setup http based yum repo - setup
* Group admin security configuration - setup
* Login as "admin" - setup
* Capture go state "PluginsTabForm" - setup

PluginsTabForm
--------------

tags: 7735, 7777, admin-page, configuration, plugins-tests

* Open "Plugins" tab

* Verify plugin named "Yum plugin" with id "yum" is valid
* Verify plugin with id "yum" has version "2.0.0" name "Yum plugin" description "Plugin that polls a yum repository" author "ThoughtWorks Go Team" with enabled link to "http://www.thoughtworks.com/"
* Verify more information for plugin with id "yum" has path "/plugins/bundled/yum-repo-exec-poller.jar" target os "Linux" target go version "14.4.0" and bundled status as "Yes"
* Verify plugin named "test-donothing-plugin.jar" with id "test-donothing-plugin.jar" is valid
* Verify plugin with id "test-donothing-plugin.jar" has version "" name "test-donothing-plugin.jar" description "No description available." author "Unknown" with disabled link
* Verify more information for plugin with id "test-donothing-plugin.jar" has path "/test-donothing-plugin.jar" target os "No restrictions" target go version "Unknown" and bundled status as "Yes"
* Verify plugin named "test-plugin-xml" with id "test-plugin-xml" is marked as invalid with message "Plugin with ID (test-plugin-xml) is not valid: Incompatible with current operating system 'Linux'. Valid operating systems are: [Windows]."
* Verify plugin with id "test-plugin-xml" has version "1.0.0" name "test-plugin-xml" description "Plugin that has only some fields in its plugin.xml" author "Unknown" with enabled link to "http://www.mdaliejaz.com/"
* Verify more information for plugin with id "test-plugin-xml" has path "test-with-some-plugin-xml-values.jar" target os "Windows" target go version "Unknown" and bundled status as "Yes"

* Logout and login as "group1Admin"

* Open "Plugins" tab

* Verify plugin named "Yum plugin" with id "yum" is valid
* Verify plugin with id "yum" has version "2.0.0" name "Yum plugin" description "Plugin that polls a yum repository" author "ThoughtWorks Go Team" with enabled link to "http://www.thoughtworks.com/"
* Verify more information for plugin with id "yum" has path "/plugins/bundled/yum-repo-exec-poller.jar" target os "Linux" target go version "14.4.0" and bundled status as "Yes"
* Verify plugin named "test-donothing-plugin.jar" with id "test-donothing-plugin.jar" is valid
* Verify plugin with id "test-donothing-plugin.jar" has version "" name "test-donothing-plugin.jar" description "No description available." author "Unknown" with disabled link
* Verify more information for plugin with id "test-donothing-plugin.jar" has path "/test-donothing-plugin.jar" target os "No restrictions" target go version "Unknown" and bundled status as "Yes"
* Verify plugin named "test-plugin-xml" with id "test-plugin-xml" is marked as invalid with message "Plugin with ID (test-plugin-xml) is not valid: Incompatible with current operating system 'Linux'. Valid operating systems are: [Windows]."
* Verify plugin with id "test-plugin-xml" has version "1.0.0" name "test-plugin-xml" description "Plugin that has only some fields in its plugin.xml" author "Unknown" with enabled link to "http://www.mdaliejaz.com/"
* Verify more information for plugin with id "test-plugin-xml" has path "/test-with-some-plugin-xml-values.jar" target os "Windows" target go version "Unknown" and bundled status as "Yes"





Teardown of contexts 
* Capture go state "PluginsTabForm" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown
* Setup http based yum repo - teardown


