AgentInEnvironmentShouldNotSchedule
===================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast" - setup
* With "1" live agents in directory "AgentInEnvironmentShouldNotSchedule" - setup
* Capture go state "AgentInEnvironmentShouldNotSchedule" - setup

AgentInEnvironmentShouldNotSchedule
-----------------------------------

tags: agent management, svn support, agent auto-discover, 3093, automate

* Add environment "uat" to agents "2"

* Looking at pipeline "basic-pipeline-fast"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"

* Verify none of the agents are building
* Remove environment "uat" from agents "2"

* Looking at pipeline "basic-pipeline-fast"
* Verify stage "1" is "Passed" on pipeline with label "1"




Teardown of contexts 
* Capture go state "AgentInEnvironmentShouldNotSchedule" - teardown
* With "1" live agents in directory "AgentInEnvironmentShouldNotSchedule" - teardown
* Using pipeline "basic-pipeline-fast" - teardown
* Basic configuration - teardown


