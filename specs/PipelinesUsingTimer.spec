PipelinesUsingTimer
===================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast" - setup
* With "1" live agents in directory "PipelinesUsingTimer" - setup
* Capture go state "PipelinesUsingTimer" - setup

PipelinesUsingTimer
-------------------

tags: 2272, timer, automate

Setting a timer that will never actually trigger the pipeline. (Assuming time travel will not happen within this twist test)

* Using timer with spec "* * * * * ? 2021"
* Setting first stage to auto approval

* Looking at pipeline "basic-pipeline-fast"
* Verify stage "1" is "Passed" on pipeline with label "1"

* Checkin file "foo.txt" as user "twist" with message "Added foo.txt"

* Looking at pipeline "basic-pipeline-fast"
* Verify stage "1" is "Passed" on pipeline with label "2"

Setting a timer that will constantly trigger the pipeline.

* Using timer with spec "0/30 * * * * ? *"

* Verify stage "1" is "Passed" on pipeline with label "3"
* Pause pipeline with reason "prevent another timer trigger before verification"
* Verify pipeline is paused with reason "prevent another timer trigger before verification" by "anonymous"
* Verify pipeline "basic-pipeline-fast" is triggered by "timer"




Teardown of contexts 
* Capture go state "PipelinesUsingTimer" - teardown
* With "1" live agents in directory "PipelinesUsingTimer" - teardown
* Using pipeline "basic-pipeline-fast" - teardown
* Basic configuration - teardown


