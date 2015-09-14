NewCruiseInvalidLicense
=======================

Setup of contexts
* Cruise config without license - setup
* Capture go state "NewCruiseInvalidLicense" - setup

NewCruiseInvalidLicense
-----------------------

tags: licensing, restful api, manual


NO IDEA WHAT THIS MEANS! (Sachin)
With empty license

* RequestsOnInValidLicense 
     |Url                                           |Method|Should Ignore?|Should Pay?|Should Redirect?|
     |----------------------------------------------|------|--------------|-----------|----------------|
     |files/pipeline/LATEST/stage/1/job/1/readme.txt|POST  |true          |false      |false           |
     |files/pipeline/LATEST/stage/1/job/1/readme.txt|PUT   |true          |false      |false           |
     |files/pipeline/LATEST/stage/1/job/1/readme.txt|GET   |false         |false      |true            |
     |admin/agent                                   |GET   |true          |false      |false           |
     |pipelineStatus.json                           |GET   |false         |true       |false           |


With invalid license

* open server details page
* enter license "invalid user" "invalid license"
* verify flash message "The license key you entered is invalid. Please enter a valid license key."





Teardown of contexts
* Capture go state "NewCruiseInvalidLicense" - teardown
* Cruise config without license - teardown


