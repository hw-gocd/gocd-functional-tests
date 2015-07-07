AgentResources
==============

Setup of contexts 
* Basic configuration - setup
* Using pipeline "basic-pipeline-with-job-resources" - setup
* With "1" live agents in directory "AgentsResources" - setup
* Capture go state "AgentResources" - setup

AgentResources
--------------

tags: agent management, svn support, scheduling, agent auto-discover, agents, automate


* Looking at pipeline "basic-pipeline-with-job-resources"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"

* Verify none of the agents are building
* Add resource "test_resource" to all agents
* Wait for agent to show status "building"




Teardown of contexts 
* Capture go state "AgentResources" - teardown
* With "1" live agents in directory "AgentsResources" - teardown
* Using pipeline "basic-pipeline-with-job-resources" - teardown
* Basic configuration - teardown


