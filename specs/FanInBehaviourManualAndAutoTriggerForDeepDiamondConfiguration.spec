FanInBehaviourManualAndAutoTriggerForDeepDiamondConfiguration
=============================================================

Setup of contexts 
* Fanin configuration - setup
* Using pipeline "P1,P2,P3,P4" - setup
* With "2" live agents in directory "StageDetails" - setup
* Capture go state "FanInManualAndAutoTriggerForDeepDiamondConfiguration" - setup

FanInBehaviourManualAndAutoTriggerForDeepDiamondConfiguration
-------------------------------------------------------------

tags: Deep Diamond, Fanin, #6434, 6434

* Trigger pipelines "P1" and wait for labels "1" to pass
* Trigger pipelines "P2" and wait for labels "1" to pass
* Trigger pipelines "P3" and wait for labels "1" to pass
* Looking at pipeline "P4"
* Verify stage "1" is "Passed" on pipeline with label "1"

* With material "git-one" for pipeline "P1"
* Checkin file "new-file-1" as user "go <go@po.com>" with message "Added new-file 1"
* Remember current version as "git-one-c2"

* Trigger pipelines "P3" and wait for labels "2" to pass
* Looking at pipeline "P4"
* Verify pipeline is at label "1" and does not get triggered

* With material "git-two" for pipeline "P4"
* Checkin file "new-file-1" as user "go <go@po.com>" with message "Added new-file 1"
* Remember current version as "git-two-c2"

* Looking at pipeline "P4"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Git" named "git-one" for pipeline "P4" with counter "2"
* Verify material has not changed
* Looking at material of type "Git" named "git-two" for pipeline "P4" with counter "2"
* Verify modification "0" has revision "git-two-c2"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:P2}" for pipeline "P4" with counter "2"
* Verify modification "0" has revision "${runtime_name:P2}/1/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:P3}" for pipeline "P4" with counter "2"
* Verify modification "0" has revision "${runtime_name:P3}/1/defaultStage/1"
* Verify material has not changed

* Trigger pipelines "P1" and wait for labels "2" to pass
* Looking at pipeline "P4"
* Verify pipeline is at label "2" and does not get triggered
* Trigger pipelines "P2" and wait for labels "2" to pass
* Looking at pipeline "P4"
* Verify stage "1" is "Passed" on pipeline with label "3"
* Open changes section for counter "3"

* Looking at material of type "Git" named "git-one" for pipeline "P4" with counter "3"
* Verify modification "0" has revision "git-one-c2"
* Verify material has changed
* Looking at material of type "Git" named "git-two" for pipeline "P4" with counter "3"
* Verify modification "0" has revision "git-two-c2"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:P2}" for pipeline "P4" with counter "3"
* Verify modification "0" has revision "${runtime_name:P2}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:P3}" for pipeline "P4" with counter "3"
* Verify modification "0" has revision "${runtime_name:P3}/2/defaultStage/1"
* Verify material has changed






Teardown of contexts 
* Capture go state "FanInManualAndAutoTriggerForDeepDiamondConfiguration" - teardown
* With "2" live agents in directory "StageDetails" - teardown
* Using pipeline "P1,P2,P3,P4" - teardown
* Fanin configuration - teardown


