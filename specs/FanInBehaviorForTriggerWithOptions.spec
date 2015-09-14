FanInBehaviorForTriggerWithOptions
==================================

Setup of contexts
* Fanin configuration - setup
* Using pipeline "FTO1, FTO2, FTO3, FTO4, FTO5" - setup
* With "2" live agents in directory "FanInBehaviorForTriggerWithOptions" - setup
* Capture go state "FanInBehaviorForTriggerWithOptions" - setup

FanInBehaviorForTriggerWithOptions
----------------------------------

tags: diamond dependency, fanin, auto, 6450

* With material "git-one" for pipeline "FTO1"
* Checkin file "new-file-0" as user "go <go@po.com>" with message "Added new-file 0"
* Remember current version as "g0"

* Trigger pipelines "FTO1" and wait for labels "1" to pass
* Trigger pipelines "FTO2" and wait for labels "1" to pass
* Trigger pipelines "FTO3" and wait for labels "1" to pass
* Looking at pipeline "FTO4"
* Wait for labels "1" to pass
* Looking at pipeline "FTO5"
* Wait for labels "1" to pass

* With material "git-one" for pipeline "FTO1"
* Checkin file "new-file-1" as user "go <go@po.com>" with message "Added new-file 1"
* Remember current version as "g1"

* Trigger pipelines "FTO1" and wait for labels "2" to pass

* With material "git-one" for pipeline "FTO1"
* Checkin file "new-file-2" as user "go <go@po.com>" with message "Added new-file 2"
* Remember current version as "g2"

* Trigger pipelines "FTO2" and wait for labels "2" to pass
* Trigger pipelines "FTO3" and wait for labels "2" to pass

* Looking at pipeline "FTO4"
* Verify pipeline is at label "1" and does not get triggered

* With material "git-one" for pipeline "FTO1"
* Checkin file "new-file-3" as user "go <go@po.com>" with message "Added new-file 3"
* Remember current version as "g3"

* Trigger pipelines "FTO1" and wait for labels "3" to pass
* Trigger pipelines "FTO2" and wait for labels "3" to pass
* Trigger pipelines "FTO3" and wait for labels "3" to pass
* Looking at pipeline "FTO4"
* Wait for labels "2" to pass
* Looking at pipeline "FTO5"
* Wait for labels "2" to pass

* Looking at pipeline "FTO4"
* Open trigger with options

* Select revision "${runtime_name:FTO1}/3/stage1/1" for material "${runtime_name:FTO1}"
* Select revision "${runtime_name:FTO3}/3/stage1/1" for material "${runtime_name:FTO3}"
* Select revision "${runtime_name:FTO2}/2/stage1/1" for material "${runtime_name:FTO2}"
* Trigger

* Looking at pipeline "FTO4"
* Wait for labels "3" to pass

* Looking at pipeline "FTO5"
* Verify pipeline is at label "2" and does not get triggered

* Looking at pipeline "FTO3"
* Open trigger with options


* Select revision "Added new-file 3" for material "git-one"
* Select revision "${runtime_name:FTO1}/3/stage1/1" for material "${runtime_name:FTO1}"
* Select revision "${runtime_name:FTO2}/2/stage1/1" for material "${runtime_name:FTO2}"
* Trigger

* Looking at pipeline "FTO4"
* Verify pipeline is at label "3" and does not get triggered

* Looking at pipeline "FTO2"
* Open trigger with options

* Select revision "Added new-file 1" for material "git-one"
* Trigger

* Looking at pipeline "FTO2"
* Wait for labels "4" to pass

* Looking at pipeline "FTO3"
* Open trigger with options

* Select revision "Added new-file 1" for material "git-one"
* Select revision "${runtime_name:FTO1}/2/stage1/1" for material "${runtime_name:FTO1}"
* Select revision "${runtime_name:FTO2}/4/stage1/1" for material "${runtime_name:FTO2}"
* Trigger

* Looking at pipeline "FTO3"
* Wait for labels "5" to pass
* Looking at pipeline "FTO4"
* Wait for labels "4" to pass
* Looking at pipeline "FTO5"
* Wait for labels "3" to pass

* Looking at pipeline "FTO3"
* Open trigger with options

* Select revision "Added new-file 3" for material "git-one"
* Select revision "${runtime_name:FTO1}/3/stage1/1" for material "${runtime_name:FTO1}"
* Select revision "${runtime_name:FTO2}/3/stage1/1" for material "${runtime_name:FTO2}"
* Trigger

* Looking at pipeline "FTO3"
* Wait for labels "6" to pass

* Looking at pipeline "FTO4"
* Verify pipeline is at label "4" and does not get triggered





Teardown of contexts
* Capture go state "FanInBehaviorForTriggerWithOptions" - teardown
* With "2" live agents in directory "FanInBehaviorForTriggerWithOptions" - teardown
* Using pipeline "FTO1, fTO2, fTO3, fTO4, fTO5" - teardown
* Fanin configuration - teardown


