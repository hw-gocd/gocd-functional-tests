EnvironmentsScreen
==================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "basic-environment-pipeline, basic-pipeline-run-till-file-exists" - setup
* With "2" live agents in directory "AgentsUIScreen" - setup
* Capture go state "EnvironmentsScreen" - setup

EnvironmentsScreen
------------------

tags: 2808, environment, UI, automate, 3574, 3513

* Assigning "2" agents to environment "prod"

* Adding pipeline "basic-pipeline-run-till-file-exists" to "prod" environment
* Making pipeline "basic-environment-pipeline" auto update

* Looking at "prod" environment
* Looking at pipeline "basic-environment-pipeline" - On Environment Page
* Verify has new revisions
* Verify status is "No historical data"
* Deploy latest
* Verify does not have new revisions
* Verify has "1" materials
* Expand materials
* Verify material "1" with name "hg-material" has latest revision
* Wait for status "Passed: defaultStage" to show up for the pipeline





Teardown of contexts 
* Capture go state "EnvironmentsScreen" - teardown
* With "2" live agents in directory "AgentsUIScreen" - teardown
* Using pipeline "basic-environment-pipeline, basic-pipeline-run-till-file-exists" - teardown
* Basic configuration - teardown


