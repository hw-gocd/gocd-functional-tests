JobsOnMatchingAgents-Unit
=========================

Setup of contexts 
* Capture go state "JobsOnMatchingAgents-Unit" - setup

JobsOnMatchingAgents-Unit
-------------------------

tags: 3102, job template, unit

* verify that a stage can contain jobs with run-on tag along with a job with no run-on tag
* verify that tasks and resources are not mandatory for a job run-on
* verify that a stage can contain multiple job run-ons
* verify that if no resources are specified within a job with run-on jobs are run on all enabled agents
* verify that if there are 5 matching agents there are 5 jobs created with different agent uuid name in job name





Teardown of contexts 
* Capture go state "JobsOnMatchingAgents-Unit" - teardown


