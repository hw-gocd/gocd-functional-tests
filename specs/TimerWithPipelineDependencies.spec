TimerWithPipelineDependencies
=============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast, downstream-pipeline" - setup
* With "1" live agents in directory "TimerWithPipelineDependencies" - setup
* Capture go state "TimerWithPipelineDependencies" - setup

TimerWithPipelineDependencies
-----------------------------

tags: 2272, timer, automate


* Setting first stage of "downstream-pipeline" to auto approval

verify that if uptream pipeline has  a timer it triggers the downstream pipeline when upstream finishes

Upstream pipeline completed
* Looking at pipeline "basic-pipeline-fast"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "downstream-pipeline"
* Verify stage "1" is "Passed" on pipeline with label "1"

* Looking at pipeline "basic-pipeline-fast" - Configure Pipeline
* Configure timer to trigger pipeline "2" minutes from now

* Verify stage "1" is "Passed" on pipeline with label "2"

* Looking at pipeline "basic-pipeline-fast" - Configure Pipeline
* Remove timer

* Looking at pipeline "downstream-pipeline"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Pipeline" named "upstream-material" for pipeline "downstream-pipeline" with counter "2"
* Verify modification "0" has revision "${runtime_name:basic-pipeline-fast}/2/defaultStage/1"

verify that if downstream pipeline has a timer it get triggered seperately

* Looking at pipeline "downstream-pipeline" - Configure Pipeline
* Configure timer to trigger pipeline "2" minutes from now

* Looking at pipeline "downstream-pipeline"
* Verify stage "1" is "Passed" on pipeline with label "3"
* Verify pipeline "downstream-pipeline" is triggered by "timer"




Teardown of contexts
* Capture go state "TimerWithPipelineDependencies" - teardown
* With "1" live agents in directory "TimerWithPipelineDependencies" - teardown
* Using pipeline "basic-pipeline-fast, downstream-pipeline" - teardown
* Basic configuration - teardown


