FanInWithAllAutoPipelines
=========================

Setup of contexts
* Fanin configuration - setup
* Using pipeline "grandparent-fast, parent-fast, parent-slow, child-fast" - setup
* With "4" live agents in directory "StageDetails" - setup
* Capture go state "FanInWithAllAutoPipelines" - setup

FanInWithAllAutoPipelines
-------------------------

tags: diamond dependency, auto, fanin, flaky_fanin_test

* Looking at pipeline "grandparent-fast"
* Verify stage "1" is "Passed" on pipeline with label "1"


* Looking at pipeline "parent-fast"
* Verify stage "1" is "Passed" on pipeline with label "1"


* With material "git-five" for pipeline "grandparent-fast"
* Checkin file "new-file-2" as user "go <go@po.com>" with message "Added new-file 2"
* Remember current version as "g2"


* Looking at pipeline "grandparent-fast"
* Verify stage "1" is "Passed" on pipeline with label "2"


* Looking at pipeline "parent-fast"
* Verify stage "1" is "Passed" on pipeline with label "2"


* With material "git-five" for pipeline "grandparent-fast"
* Checkin file "new-file-3" as user "go <go@po.com>" with message "Added new-file 3"
* Remember current version as "g3"



* Looking at pipeline "grandparent-fast"
* Verify stage "1" is "Passed" on pipeline with label "3"


* Looking at pipeline "parent-fast"
* Verify stage "1" is "Passed" on pipeline with label "3"


* Looking at pipeline "parent-slow"
* Verify stage "1" is "Passed" on pipeline with label "2"


* Looking at pipeline "child-fast"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"


* Looking at material of type "Pipeline" named "${runtime_name:grandparent-fast}" for pipeline "child-fast" with counter "2"
* Verify modification "0" has revision "${runtime_name:grandparent-fast}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:parent-fast}" for pipeline "child-fast" with counter "2"
* Verify modification "0" has revision "${runtime_name:parent-fast}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:parent-slow}" for pipeline "child-fast" with counter "2"
* Verify modification "0" has revision "${runtime_name:parent-slow}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Git" named "git-five" for pipeline "child-fast" with counter "2"
* Verify modification "0" has revision "g2"
* Verify material has changed

* Looking at pipeline "parent-slow"
* Verify stage "1" is "Passed" on pipeline with label "3"


* Looking at pipeline "child-fast"
* Verify stage "1" is "Passed" on pipeline with label "3"
* Open changes section for counter "3"


* Looking at material of type "Pipeline" named "${runtime_name:grandparent-fast}" for pipeline "child-fast" with counter "3"
* Verify modification "0" has revision "${runtime_name:grandparent-fast}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:parent-fast}" for pipeline "child-fast" with counter "3"
* Verify modification "0" has revision "${runtime_name:parent-fast}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:parent-slow}" for pipeline "child-fast" with counter "3"
* Verify modification "0" has revision "${runtime_name:parent-slow}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Git" named "git-five" for pipeline "child-fast" with counter "3"
* Verify modification "0" has revision "g3"
* Verify material has changed




Teardown of contexts
* Capture go state "FanInWithAllAutoPipelines" - teardown
* With "4" live agents in directory "StageDetails" - teardown
* Using pipeline "grandparent-fast, parent-fast, parent-slow, child-fast" - teardown
* Fanin configuration - teardown


