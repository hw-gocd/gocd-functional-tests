ServerConfigurationCommandRepositoryLocation
============================================

Setup of contexts
* Basic configuration - setup
* Capture go state "ServerConfigurationCommandRepositoryLocation" - setup
* Setup command repo - setup

ServerConfigurationCommandRepositoryLocation
--------------------------------------------

tags: 6664, admin-page, configuration, task-repository-location

* Open "Server Configuration" tab

* Verify command repository location is set to "default"

* Using "." as command repository location
* Save configuration
* Verify message contains "Failed to save the server configuration. Reason: Invalid Repository Location, repository should be a subdirectory under"

* Using "custom" as command repository location
* Save configuration
* Verify message "Saved configuration successfully." shows up





Teardown of contexts
* Setup command repo - teardown
* Capture go state "ServerConfigurationCommandRepositoryLocation" - teardown
* Basic configuration - teardown


