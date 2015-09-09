AssociatingAPipelineWithAnEnvironmentWithNoAgents
=================================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "environment-pipeline" - setup
* With "2" live agents in directory "AssociatingAPipelineWithAnEnvironmentWithNoAgents" - setup
* Capture go state "AssociatingAPipelineWithAnEnvironmentWithNoAgents" - setup

AssociatingAPipelineWithAnEnvironmentWithNoAgents
-------------------------------------------------

tags: 3216, automate, environment, pipeline

This is to verify that only the agents associated with an evironment are used to build the pipeline
* Add resource "linux" to all agents

* Adding resource "linux" to the job "short"

* Trigger pipeline "environment-pipeline"

* Verify none of the agents are building





Teardown of contexts
* Capture go state "AssociatingAPipelineWithAnEnvironmentWithNoAgents" - teardown
* With "2" live agents in directory "AssociatingAPipelineWithAnEnvironmentWithNoAgents" - teardown
* Using pipeline "environment-pipeline" - teardown
* Basic configuration - teardown


