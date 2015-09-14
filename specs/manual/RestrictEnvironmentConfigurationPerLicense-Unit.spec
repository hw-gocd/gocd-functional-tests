RestrictEnvironmentConfigurationPerLicense-Unit
===============================================

Setup of contexts
* Capture go state "RestrictEnvironmentConfigurationPerLicense-Unit" - setup

RestrictEnvironmentConfigurationPerLicense-Unit
-----------------------------------------------

tags: 3347, unit, license, config, manual

Need to repeat the following tests for environments, pipeline groups, operate permission and view permission

* Community

* verify that Environments tab says "Environments is a Go Enterprise feature. Go is currently running in Community mode. Request an Enterprise license "
* verify that on adding environments via cruise config xml it errors out with flash "You have configured the feature, Environments, that is not available in Go Community Edition. Help Topic: Configuration"

* verify that Pipelines tab says "Multiple Pipeline Groups is a Go Enterprise feature. Go is currently running in Community mode. Request an Enterprise license"
* verify that on adding a new pipeline group via cruise config xml it errors out with flash "You cannot have more than one Pipeline group in Go Community Edition. Help Topic: Configuration"

* verify that on editing a pipeline group "Permissions is a Go Enterprise feature. Go is currently running in Community mode. Request an Enterprise license "
* verify that on adding permissions via cruise config xml it errors out with flash "You cannot configure security permissions in Go Community Edition. Help Topic: Configuration"





Teardown of contexts
* Capture go state "RestrictEnvironmentConfigurationPerLicense-Unit" - teardown


