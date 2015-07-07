AssociatingMultiplePipelinesWithAnEnvironment
=============================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "environment-pipeline, basic-pipeline" - setup
* With "2" live agents in directory "AssociatingMultiplePipelinesWithAnEnvironment" - setup
* Capture go state "AssociatingMultiplePipelinesWithAnEnvironment" - setup

AssociatingMultiplePipelinesWithAnEnvironment
---------------------------------------------

tags: 3216, automate, environment, pipeline

This is to verify that only the agents associated with an evironment are used to build the pipeline
* Assigning "2" agents to environment "uat"
* Adding pipeline "basic-pipeline" to "uat" environment

* Looking at pipeline "environment-pipeline"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Looking at pipeline "basic-pipeline"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"






Teardown of contexts 
* Capture go state "AssociatingMultiplePipelinesWithAnEnvironment" - teardown
* With "2" live agents in directory "AssociatingMultiplePipelinesWithAnEnvironment" - teardown
* Using pipeline "environment-pipeline, basic-pipeline" - teardown
* Basic configuration - teardown


