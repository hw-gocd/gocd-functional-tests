FanInBehavior
=============

Setup of contexts
* Fanin configuration - setup
* Using pipeline "C1, c2, c3, c4-auto, c5, c6-auto, c7, c8, c9, c10-auto, c11-auto" - setup
* With "2" live agents in directory "StageDetails" - setup
* Capture go state "FanInBehavior" - setup

FanInBehavior
-------------

tags: diamond dependency, fanin, auto

* With material "git-four" for pipeline "C6-auto"
* Checkin file "new-file-2" as user "go <go@po.com>" with message "Added new-file 2"
* Remember current version as "git-four-g2"


* With material "git-one" for pipeline "C1"
* Checkin file "new-file-2" as user "go <go@po.com>" with message "Added new-file 2"
* Remember current version as "git-one-g2"


* With material "git-three" for pipeline "C7"
* Checkin file "new-file-2" as user "go <go@po.com>" with message "Added new-file 2"
* Remember current version as "git-three-g2"

* Trigger pipelines "C1" and wait for labels "1" to pass
* Trigger pipelines "C2" and wait for labels "1" to pass
* Trigger pipelines "C8" and wait for labels "1" to pass


On Pipeline Dashboard Page
looking at pipeline "C4-auto"
verify pipeline does not get triggered even once

* With material "git-one" for pipeline "C1"
* Checkin file "new-file-3" as user "go <go@po.com>" with message "Added new-file 3"
* Remember current version as "git-one-g3"


* Trigger pipelines "C1" and wait for labels "2" to pass
* Trigger pipelines "C3" and wait for labels "1" to pass

On Pipeline Dashboard Page
looking at pipeline "C4-auto"
verify pipeline does not get triggered even once


* Trigger pipelines "C2" and wait for labels "2" to pass


* Looking at pipeline "C4-auto"
* Verify pipeline does not get triggered even once


* Trigger pipelines "C3" and wait for labels "2" to pass
* Verify stage "1" is "Passed" on pipeline with label "2"


* Looking at pipeline "C4-auto"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Open changes section for counter "1"

* Looking at material of type "Pipeline" named "${runtime_name:C1}" for pipeline "C4-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C1}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C2}" for pipeline "C4-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C2}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C3}" for pipeline "C4-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C3}/2/defaultStage/1"
* Verify material has changed

* With material "git-two" for pipeline "C1"
* Checkin file "file-2" as user "go <go@po.com>" with message "Added file 2"
* Remember current version as "git-two-g2"

* Trigger pipelines "C5" and wait for labels "1" to pass
* Trigger pipelines "C7" and wait for labels "1" to pass

On Pipeline Dashboard Page
looking at pipeline "C6-auto"
verify pipeline does not get triggered even once

* With material "git-three" for pipeline "C7"
* Checkin file "file-3" as user "go <go@po.com>" with message "Added file 3"
* Remember current version as "git-three-g3"

* Trigger pipelines "C8" and wait for labels "2" to pass

* Trigger pipelines "C1" and wait for labels "3" to pass
* Trigger pipelines "C3" and wait for labels "3" to pass
* Looking at pipeline "C4-auto"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"


* Looking at material of type "Pipeline" named "${runtime_name:C1}" for pipeline "C4-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C1}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C2}" for pipeline "C4-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C2}/2/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C3}" for pipeline "C4-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C3}/3/defaultStage/1"
* Verify material has changed


* Looking at pipeline "C6-auto"
* Verify pipeline does not get triggered even once


* Trigger pipelines "C7" and wait for labels "2" to pass

* Looking at pipeline "C6-auto"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Open changes section for counter "1"

* Looking at material of type "Pipeline" named "${runtime_name:C4-auto}" for pipeline "C6-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C4-auto}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C1}" for pipeline "C6-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C1}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C5}" for pipeline "C6-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C5}/1/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C7}" for pipeline "C6-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C7}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C8}" for pipeline "C6-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C8}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Git" named "git-one" for pipeline "C6-auto" with counter "1"
* Verify modification "0" has revision "git-one-g3"
* Verify material has changed
* Looking at material of type "Git" named "git-four" for pipeline "C6-auto" with counter "1"
* Verify modification "0" has revision "git-four-g2"
* Verify material has changed

* Looking at pipeline "C10-auto"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Open changes section for counter "1"

* Looking at material of type "Pipeline" named "${runtime_name:C8}" for pipeline "C10-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C8}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C6-auto}" for pipeline "C10-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C6-auto}/1/defaultStage/1"
* Verify material has changed

* With material "git-three" for pipeline "C7"
* Checkin file "file-4" as user "go <go@po.com>" with message "Added file 4"
* Remember current version as "git-three-g4"

* With material "git-four" for pipeline "C6-auto"
* Checkin file "file-3" as user "go <go@po.com>" with message "Added file 3"
* Remember current version as "git-four-g3"

* Looking at pipeline "C6-auto"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Pipeline" named "${runtime_name:C4-auto}" for pipeline "C6-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C4-auto}/2/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C1}" for pipeline "C6-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C1}/3/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C5}" for pipeline "C6-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C5}/1/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C7}" for pipeline "C6-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C7}/2/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C8}" for pipeline "C6-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C8}/2/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Git" named "git-one" for pipeline "C6-auto" with counter "2"
* Verify modification "0" has revision "git-one-g3"
* Verify material has not changed
* Looking at material of type "Git" named "git-four" for pipeline "C6-auto" with counter "2"
* Verify modification "0" has revision "git-four-g3"
* Verify material has changed

* Trigger pipelines "C9" and wait for labels "1" to pass


* Looking at pipeline "C10-auto"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"

* Looking at material of type "Pipeline" named "${runtime_name:C8}" for pipeline "C10-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C8}/2/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C6-auto}" for pipeline "C10-auto" with counter "2"
* Verify modification "0" has revision "${runtime_name:C6-auto}/2/defaultStage/1"
* Verify material has changed

* Looking at pipeline "C11-auto"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Open changes section for counter "1"


* Looking at material of type "Pipeline" named "${runtime_name:C9}" for pipeline "C11-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C9}/1/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C10-auto}" for pipeline "C11-auto" with counter "1"
* Verify modification "0" has revision "${runtime_name:C10-auto}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Git" named "git-three" for pipeline "C11-auto" with counter "1"
* Verify modification "0" has revision "git-three-g3"
* Verify material has changed

* With material "git-one" for pipeline "C1"
* Checkin file "file-4" as user "go <go@po.com>" with message "Added file 4"
* Remember current version as "git-one-g4"

* Trigger pipelines "C2" and wait for labels "3" to pass
* Trigger pipelines "C8" and wait for labels "3" to pass


* Looking at pipeline "C10-auto"
* Verify pipeline is at label "2" and does not get triggered


* With material "git-two" for pipeline "C1"
* Checkin file "file-3" as user "go <go@po.com>" with message "Added file 3"
* Remember current version as "git-two-g3"


* Trigger pipelines "C1" and wait for labels "4" to pass

* Trigger pipelines "C4-auto" and wait for labels "3" to pass
* Open changes section for counter "3"


* Looking at material of type "Pipeline" named "${runtime_name:C1}" for pipeline "C4-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C1}/4/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C2}" for pipeline "C4-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C2}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C3}" for pipeline "C4-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C3}/3/defaultStage/1"
* Verify material has not changed

* Trigger pipelines "C6-auto" and wait for labels "3" to pass
* Open changes section for counter "3"


* Looking at material of type "Pipeline" named "${runtime_name:C4-auto}" for pipeline "C6-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C4-auto}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C1}" for pipeline "C6-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C1}/4/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:C5}" for pipeline "C6-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C5}/1/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C7}" for pipeline "C6-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C7}/2/defaultStage/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:C8}" for pipeline "C6-auto" with counter "3"
* Verify modification "0" has revision "${runtime_name:C8}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Git" named "git-one" for pipeline "C6-auto" with counter "3"
* Verify modification "0" has revision "git-one-g4"
* Verify material has changed
* Looking at material of type "Git" named "git-four" for pipeline "C6-auto" with counter "3"
* Verify modification "0" has revision "git-four-g3"
* Verify material has not changed





Teardown of contexts
* Capture go state "FanInBehavior" - teardown
* With "2" live agents in directory "StageDetails" - teardown
* Using pipeline "C1, c2, c3, c4-auto, c5, c6-auto, c7, c8, c9, c10-auto, c11-auto" - teardown
* Fanin configuration - teardown


