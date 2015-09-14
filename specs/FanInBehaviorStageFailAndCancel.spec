FanInBehaviorStageFailAndCancel
===============================

Setup of contexts
* Fanin configuration - setup
* Using pipeline "FS1, FS2, FS3" - setup
* With "2" live agents in directory "FanInBehaviorStageFailAndCancel" - setup
* Capture go state "FanInBehaviorStageFailAndCancel" - setup

FanInBehaviorStageFailAndCancel
-------------------------------

tags: diamond dependency, fanin, auto, 6437, 6368

* With material "git-one" for pipeline "FS1"
* Checkin file "new-file-1" as user "go <go@po.com>" with message "Added new-file 1"
* Remember current version as "git-one-g1"

* Trigger pipelines "FS1" and wait for labels "1" to pass
* Looking at pipeline "FS1"
* Navigate to stage "stage1" of run "1"

* Trigger stage "stage2-manual"

* Navigate to stage "stage2-manual" of run "1"

* Wait for stage result to show "Passed"

* Looking at pipeline "FS2"
* Wait for labels "1" to pass
* Looking at pipeline "FS3"
* Wait for labels "1" to pass

* Click on pipeline "FS1" for editing

* Open stage listing page

* Open stage "stage2-manual"

* Open jobs

* Open job "job2"

* Open tasks

* Open task "1"

* Set "task[command](text_field): crap" - Already on Task edit popup
* Save and verify saved successfully

* Trigger pipelines "FS1" and wait for labels "2" to pass
* Navigate to stage "stage1" of run "2"

* Trigger stage "stage2-manual"

* Navigate to stage "stage2-manual" of run "1"

* Wait for stage result to show "Failed"

* Looking at pipeline "FS2"
* Verify pipeline is at label "1" and does not get triggered

* Click on pipeline "FS1" for editing

* Open stage listing page

* Open stage "stage2-manual"

* Open jobs

* Open job "job2"

* Open tasks

* Open task "1"

* Set "task[command](text_field): ls" - Already on Task edit popup
* Save and verify saved successfully

* Trigger pipelines "FS1" and wait for labels "3" to pass
* Navigate to stage "stage1" of run "3"

* Trigger stage "stage2-manual"

* Navigate to stage "stage2-manual" of run "3"

* Wait for stage result to show "Passed"

* Looking at pipeline "FS2"
* Trigger pipeline
* Looking at pipeline "FS1"
* Navigate to stage "stage2-manual" of run "3"

* Rerun stage "stage2-manual"
* Cancel "stage2-manual" - Already On Stage Detail Page

* Looking at pipeline "FS2"
* Wait for labels "2" to pass
* Looking at pipeline "FS3"
* Verify stage "1" is "Passed" on pipeline with label "4"
* Open changes section for counter "4"

* Looking at material of type "Pipeline" named "${runtime_name:FS1}" for pipeline "FS3" with counter "4"
* Verify modification "0" has revision "${runtime_name:FS1}/3/stage1/1"
* Verify material has not changed
* Looking at material of type "Pipeline" named "${runtime_name:FS2}" for pipeline "FS3" with counter "4"
* Verify modification "0" has revision "${runtime_name:FS2}/2/stage1/1"
* Verify material has changed




Teardown of contexts
* Capture go state "FanInBehaviorStageFailAndCancel" - teardown
* With "2" live agents in directory "FanInBehaviorStageFailAndCancel" - teardown
* Using pipeline "FS1, fS2, fS3" - teardown
* Fanin configuration - teardown


