FanInBehaviorOnAdditionAndDeletionOfMaterial
============================================

Setup of contexts 
* Fanin configuration - setup
* Using pipeline "basic-auto-pipeline, grandparent, parent-left, parent-right, child-down" - setup
* With "1" live agents in directory "StageDetails" - setup
* Capture go state "FanInBehaviorOnAdditionAndDeletionOfMaterials" - setup

FanInBehaviorOnAdditionAndDeletionOfMaterial
--------------------------------------------

tags: diamond dependency, fanin, material-change

* Trigger pipelines "grandparent" and wait for labels "1" to pass
* Trigger pipelines "parent-left" and wait for labels "1" to pass
* Trigger pipelines "parent-right" and wait for labels "1" to pass
* Looking at pipeline "child-down"
* Verify stage "1" is "Passed" on pipeline with label "1"


* Click on pipeline "parent-right" for editing

* Open material listing page

* Open new git material creation popup

* Copy over material url from material named "git" in pipeline "${runtime_name:basic-auto-pipeline}" to current pipeline
* Check connectivity should be successful - Already on Git Material Creation Popup
* Click save - Already on git material creation popup
* Verify saved successfully - Already on Git Material Creation Popup


* With material "git" for pipeline "basic-auto-pipeline"
* Checkin file "new-file-2" as user "go <go@po.com>" with message "Added new-file 2"
* Remember current version as "g2"


* Trigger pipelines "parent-left" and wait for labels "2" to pass
* Looking at pipeline "child-down"
* Verify pipeline is at label "1" and does not get triggered


* Trigger pipelines "parent-right" and wait for labels "2" to pass
* Looking at pipeline "child-down"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Open changes section for counter "2"


* Looking at material of type "Pipeline" named "${runtime_name:parent-left}" for pipeline "child-down" with counter "2"
* Verify modification "0" has revision "${runtime_name:parent-left}/2/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:parent-right}" for pipeline "child-down" with counter "2"
* Verify modification "0" has revision "${runtime_name:parent-right}/2/defaultStage/1"
* Verify material has changed


* Click on pipeline "parent-left" for editing

* Open material listing page


* Delete material with name "git"


* With material "git" for pipeline "basic-auto-pipeline"
* Checkin file "new-file-3" as user "go <go@po.com>" with message "Added new-file 3"
* Remember current version as "g3"

* Trigger pipelines "parent-right" and wait for labels "3" to pass
* Looking at pipeline "child-down"
* Verify pipeline is at label "2" and does not get triggered


* Trigger pipelines "parent-left" and wait for labels "3" to pass
* Looking at pipeline "child-down"
* Verify stage "1" is "Passed" on pipeline with label "3"
* Open changes section for counter "3"

* Looking at material of type "Pipeline" named "${runtime_name:parent-left}" for pipeline "child-down" with counter "3"
* Verify modification "0" has revision "${runtime_name:parent-left}/3/defaultStage/1"
* Verify material has changed
* Looking at material of type "Pipeline" named "${runtime_name:parent-right}" for pipeline "child-down" with counter "3"
* Verify modification "0" has revision "${runtime_name:parent-right}/3/defaultStage/1"
* Verify material has changed






Teardown of contexts 
* Capture go state "FanInBehaviorOnAdditionAndDeletionOfMaterials" - teardown
* With "1" live agents in directory "StageDetails" - teardown
* Using pipeline "basic-auto-pipeline, grandparent, parent-left, parent-right, child-down" - teardown
* Fanin configuration - teardown


