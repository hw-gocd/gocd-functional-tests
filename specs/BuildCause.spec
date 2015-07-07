BuildCause
==========

Setup of contexts 
* Basic configuration - setup
* Using pipeline "up, down" - setup
* With "1" live agents in directory "BuildCause" - setup
* Capture go state "BuildCause" - setup

BuildCause
----------

tags: 3915, pipeline, automate, failing, stage1

* Trigger pipelines "up" and wait for labels "1" to pass
* Verify pipeline "up" is triggered by "anonymous"
* Navigate to materials for "up" "1" "defaultStage" "1"

* Looking at material of type "Mercurial" named "hg-material"
* Verify modification "0" has latest revision
* Verify material has changed - Already On Build Cause Section

* Trigger pipelines "down" and wait for labels "1" to pass
* Navigate to materials for "down" "1" "defaultStage" "1"

* Looking at material of type "Pipeline" named "${runtime_name:up}"
* Verify modification "0" has revision "${runtime_name:up}/1/defaultStage/1" - Already On Build Cause Section
* Verify material has changed - Already On Build Cause Section

* Looking at pipeline "down"
* Open changes section for counter "1"

* Looking at material of type "Pipeline" named "${runtime_name:up}" for pipeline "down" with counter "1"
* Verify modification "0" has revision "${runtime_name:up}/1/defaultStage/1"
* Verify material has changed

* With material named "hg-material" in pipeline "up"
* Checkin file "foo.txt" as user "user" with message "Comment user"
* Checkin file "bar.txt" as user "loser" with message "Comment loser"

* Trigger pipelines "up" and wait for labels "2" to pass
* Navigate to materials for "up" "2" "defaultStage" "1"

* Looking at material of type "Mercurial" named "hg-material"
* Verify modification "0" is checked in by "loser" with comment "Comment loser"
* Verify modification "1" is checked in by "user" with comment "Comment user"
* Verify material has changed - Already On Build Cause Section

* Trigger pipelines "up" and wait for labels "3" to pass
* Navigate to materials for "up" "3" "defaultStage" "1"

* Looking at material of type "Mercurial" named "hg-material"
* Verify modification "0" is checked in by "loser" with comment "Comment loser"
* Verify material has not changed - Already On Build Cause Section

* Trigger pipelines "down" and wait for labels "2" to pass
* Navigate to materials for "down" "2" "defaultStage" "1"

* Looking at material of type "Pipeline" named "${runtime_name:up}"
* Verify modification "0" has revision "${runtime_name:up}/3/defaultStage/1" - Already On Build Cause Section
* Verify material has changed - Already On Build Cause Section

* Trigger pipelines "down" and wait for labels "3" to pass
* Navigate to materials for "down" "3" "defaultStage" "1"

* Looking at material of type "Pipeline" named "${runtime_name:up}"
* Verify modification "0" has revision "${runtime_name:up}/3/defaultStage/1" - Already On Build Cause Section
* Verify material has not changed - Already On Build Cause Section





Teardown of contexts 
* Capture go state "BuildCause" - teardown
* With "1" live agents in directory "BuildCause" - teardown
* Using pipeline "up, down" - teardown
* Basic configuration - teardown


