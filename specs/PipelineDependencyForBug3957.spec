PipelineDependencyForBug3957
============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "fourth, fifth, another-sixth" - setup
* With "2" live agents in directory "StageDetails" - setup
* Capture go state "PipelineDependencyForBug3957" - setup

PipelineDependencyForBug3957
----------------------------

tags: dependency pipeline, 3695, 3957, automate

* Looking at pipeline "fourth"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "fifth"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "another-sixth"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "fourth"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "fifth"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "another-sixth"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "fifth"
* Open trigger with options

* Select revision "2" in search box for material number "1"
* Deploy

* Looking at pipeline "fifth"
* Verify stage "1" is "Passed" on pipeline with label "3"
* Looking at pipeline "another-sixth"
* Verify stage "1" is "Passed" on pipeline with label "3"

* Looking at pipeline "another-sixth"
* Wait for first stage to pass with pipeline label "3"
* Verify pipeline is not getting triggered and stays at run "3"
* Wait for first stage to pass with pipeline label "3"







Teardown of contexts
* Capture go state "PipelineDependencyForBug3957" - teardown
* With "2" live agents in directory "StageDetails" - teardown
* Using pipeline "fourth, fifth, another-sixth" - teardown
* Basic configuration - teardown


