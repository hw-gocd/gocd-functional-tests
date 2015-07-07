ParamSubstitution
=================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "pipeline-with-wierd-command" - setup
* With "1" live agents in directory "ParamSubstitution" - setup
* Capture go state "ParamSubstitution" - setup

ParamSubstitution
-----------------

tags: 4207, param, params

* Looking at pipeline "pipeline-with-wierd-command"
* Trigger pipeline
* Verify stage "1" is "Failed" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "Start to execute task: <exec command=\"some_command_that_can_never_ever_exist_with_tail\" />."




Teardown of contexts 
* Capture go state "ParamSubstitution" - teardown
* With "1" live agents in directory "ParamSubstitution" - teardown
* Using pipeline "pipeline-with-wierd-command" - teardown
* Basic configuration - teardown


