DependencyWalkInPipelineCompareWithSameScm
==========================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "first, child-of-first,grandchild-of-first" - setup
* With "1" live agents in directory "dependency_walk" - setup
* Capture go state "DependencyWalkInPipelineCompareWithSameScm" - setup

DependencyWalkInPipelineCompareWithSameScm
------------------------------------------

tags: 4643, automate, compare_pipeline, dependency_walk

* With material "hg-first" for pipeline "first"
* Checkin file "hg-new-file" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-new1"

* Trigger pipelines "first" and wait for labels "1" to pass
* Trigger pipelines "child-of-first" and wait for labels "1" to pass
* Trigger pipelines "grandchild-of-first" and wait for labels "1" to pass

* With material "hg-first" for pipeline "first"
* Checkin file "hg-another-new-file" as user "go" with message "Added hg-another-new-file"
* Remember current version as "hg-new2"

* Trigger pipelines "first" and wait for labels "2" to pass
* Trigger pipelines "child-of-first" and wait for labels "2" to pass
* Trigger pipelines "grandchild-of-first" and wait for labels "2" to pass
* Click compare link

* Verify displays revision "${runtime_name:first}/2/defaultStage/1" having label "2" under pipeline named "${runtime_name:first}"
* Verify displays revision "${runtime_name:child-of-first}/2/defaultStage/1" having label "2" under pipeline named "${runtime_name:child-of-first}"
* Verify displays revision "hg-new2" having comment "Added hg-another-new-file" under "Mercurial" named "hg-first" for pipeline "first"
* Search for "1" on "to" textbox
* Click on label "1" in the dropdown
* Verify displays revision "${runtime_name:first}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:first}"
* Verify displays revision "${runtime_name:child-of-first}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:child-of-first}"
* Verify displays revision "hg-new1" having comment "Added hg-new-file" under "Mercurial" named "hg-first" for pipeline "first"




Teardown of contexts 
* Capture go state "DependencyWalkInPipelineCompareWithSameScm" - teardown
* With "1" live agents in directory "dependency_walk" - teardown
* Using pipeline "first, child-of-first,grandchild-of-first" - teardown
* Basic configuration - teardown


