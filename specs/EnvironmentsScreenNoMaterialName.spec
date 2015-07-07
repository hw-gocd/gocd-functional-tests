EnvironmentsScreenNoMaterialName
================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "multiple-same-materials" - setup
* With "1" live agents in directory "UIAutoRefreshForEnvironments" - setup
* Capture go state "EnvironmentsScreenNoMaterialName" - setup

EnvironmentsScreenNoMaterialName
--------------------------------

tags: environment, 3737, automate, deployment lightbox

Verify that all materials can be deployed.

* Assigning "1" agents to environment "uat"
* Adding pipeline "multiple-same-materials" to "uat" environment

* For pipeline "multiple-same-materials" - Using pipeline api
* Schedule should return code "202"

* Looking at pipeline "multiple-same-materials" of "uat" environment
* Wait for the pipeline to have label "1"
* Stop "1" jobs waiting for file to exist
* Wait for status "Passed: defaultStage" to show up for the pipeline

* With material named "first-material" in pipeline "multiple-same-materials"
* Checkin file "foo.txt" as user "twist" with message "Added foo.txt"
* Remember current version as "2"
* Checkin file "bar.txt" as user "twist" with message "Added bar.txt"
* Remember current version as "3"

* Verify material "first-material" has new revisions
* Change materials

* Using material number "1"
* Search for "Added"
* Verify search box is displayed with "3" matches
* Search for "Added foo.txt"
* Select revision "1" in search box
* Verify material summary contains selected revision
* Verify material summary is marked as modified
* Using material number "2"
* Verify search box is displayed with "3" matches
* Search for "Added bar.txt"
* Select revision "1" in search box
* Verify material summary contains selected revision
* Verify material summary is marked as modified
* Deploy

* Looking at pipeline "multiple-same-materials" of "uat" environment
* Wait for the pipeline to have label "2"
* Stop "1" jobs waiting for file to exist
* Wait for status "Passed: defaultStage" to show up for the pipeline
* Expand materials
* Verify material number "1" has name "first-material"
* Verify material number "1" has revision "2" deployed
* Verify material number "2" has a url for a name
* Verify material number "2" has revision "3" deployed




Teardown of contexts 
* Capture go state "EnvironmentsScreenNoMaterialName" - teardown
* With "1" live agents in directory "UIAutoRefreshForEnvironments" - teardown
* Using pipeline "multiple-same-materials" - teardown
* Basic configuration - teardown


