RPMPackageWithFaninOnPausingOfPipeline
======================================

Setup of contexts
* Package configuration - setup
* Using pipeline "fanin_a, fanin_b, fanin_c, fanin_d" - setup
* Setup file system based yum repos "repo3:go-agent-13.1.0-112.noarch.rpm" - setup
* With "2" live agents in directory "RPMPackagesWithFaninAdvanced" - setup
* Capture go state "RPMPackagesWithFaninAdvanced" - setup

RPMPackageWithFaninOnPausingOfPipeline
--------------------------------------

tags: diamond dependency, fanin, #7538, plugins-tests

* Looking at pipeline "fanin_a"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Navigate to stage "stage_1" of run "1" having counter "1"

* Trigger stage "stage_2"

* Looking at pipeline "fanin_a"
* Verify stage "2" is "Passed" on pipeline with label "1"
* Looking at pipeline "fanin_b"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "fanin_c"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "fanin_d"
* Verify stage "1" is "Passed" on pipeline with label "1"

* Looking at pipeline "fanin_d"
* Open changes section for counter "1"

* verify material of type "Pipeline" name "${runtime_name:fanin_b}" for pipeline "fanin_d" with counter "1" and modification "0"  has changed revision "${runtime_name:fanin_b}/1/defaultStage/1"
* verify material of type "Pipeline" name "${runtime_name:fanin_c}" for pipeline "fanin_d" with counter "1" and modification "0"  has changed revision "${runtime_name:fanin_c}/1/defaultStage/1"

* Looking at pipeline "fanin_b"
* Pause pipeline with reason "Pausing Pipeline fanin_b before publication of go-agent-13.1.0-5412.noarch.rpm"

* Publish artifacts "go-agent-13.1.0-5412.noarch.rpm" to "repo3"

* Looking at pipeline "fanin_a"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Navigate to stage "stage_1" of run "2" having counter "1"

* Trigger stage "stage_2"

On Pipeline Dashboard Page
looking at pipeline "faninb"
verify pipeline is at label "1" and does not get triggered

* Looking at pipeline "fanin_a"
* Verify stage "2" is "Passed" on pipeline with label "2"
* Looking at pipeline "fanin_c"
* Verify stage "1" is "Passed" on pipeline with label "2"

On Pipeline Dashboard Page
looking at pipeline "fanind"
verify pipeline is at label "1" and does not get triggered

* Looking at pipeline "fanin_b"
* Unpause pipeline

* Looking at pipeline "fanin_b"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "fanin_d"
* Verify stage "1" is "Passed" on pipeline with label "2"

* Looking at pipeline "fanin_b"
* Open changes section for counter "2"

* verify material of type "Pipeline" name "${runtime_name:fanin_a}" for pipeline "fanin_b" with counter "2" and modification "0"  has changed revision "${runtime_name:fanin_a}/2/stage_1/1"

* Looking at pipeline "fanin_d"
* Open changes section for counter "2"

* verify material of type "Pipeline" name "${runtime_name:fanin_b}" for pipeline "fanin_d" with counter "2" and modification "0"  has changed revision "${runtime_name:fanin_b}/2/defaultStage/1"
* verify material of type "Pipeline" name "${runtime_name:fanin_c}" for pipeline "fanin_d" with counter "2" and modification "0"  has changed revision "${runtime_name:fanin_c}/2/defaultStage/1"





Teardown of contexts
* Capture go state "RPMPackagesWithFaninAdvanced" - teardown
* With "2" live agents in directory "RPMPackagesWithFaninAdvanced" - teardown
* Setup file system based yum repos "repo3:go-agent-13.1.0-112.noarch.rpm" - teardown
* Using pipeline "fanin_a, fanin_b, fanin_c, fanin_d" - teardown
* Package configuration - teardown


