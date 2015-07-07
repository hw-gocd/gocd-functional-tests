NewProfessionalLicense
======================

Setup of contexts 
* Trainlines configuration - setup
* Configure professional license - setup
* Trigger "trainlines-connectfour" - setup
* Capture go state "NewProfessionalLicense" - setup

NewProfessionalLicense
----------------------

tags: #2777, licensing, security, professional license

Old twist test - AllowProfessionalLicenseUseFeatures.scn

Test that professional License should enable pipeline group level security

* login as "user-admin"
* configure a pipeline in a group with operate permission
* trigger the pipeline
* verify no error message and pipline triggers





Teardown of contexts 
* Capture go state "NewProfessionalLicense" - teardown
* Trigger "trainlines-connectfour" - teardown
* Configure professional license - teardown
* Trainlines configuration - teardown


