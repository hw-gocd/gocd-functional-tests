TfsMaterialSchedulingAndMaterialModification
============================================

Setup of contexts 
* Tfs configuration - setup
* Using pipeline "tfs-pipeline-with-multiple-stages" - setup
* With "1" live agents in directory "TfsMaterialSchedulingAndMaterialModification" - setup
* Capture go state "TfsMaterialSchedulingAndMaterialModification" - setup

TfsMaterialSchedulingAndMaterialModification
--------------------------------------------

tags: tfs, regression

* With material named "tfs_mat" in pipeline "tfs-pipeline-with-multiple-stages"
* Modify file "AnotherHelloWorld.txt" as "luser"
* Checkin as "luser" with message "interesting comment by luser"

* Looking at pipeline "tfs-pipeline-with-multiple-stages"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Navigate to stage "stage1" of run "1"

* Trigger stage "stage2"

* Click on pipeline "tfs-pipeline-with-multiple-stages" for editing

* Open material listing page

* Edit material "tfs_mat"

* Enter url "integration_tests" - Already on tfs material creation popup
* Enter project path as "$/for_tests"
* Click save - Already on tfs material creation popup

now trigger pipeline again with new material change
* Looking at pipeline "tfs-pipeline-with-multiple-stages"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "2"

verify first instance built with older material
* Navigate to materials for "tfs-pipeline-with-multiple-stages" "1" "stage1" "1"

* Looking at material of type "Tfs" named "tfs_mat"
* Verify material has changed - Already On Build Cause Section
* Verify modification "0" is checked in by "CORPORATE\\cruise_builder" with comment "interesting comment by luser"

verify second instance built with newer material
* Navigate to materials for "tfs-pipeline-with-multiple-stages" "2" "stage1" "1"

* Looking at material of type "Tfs" named "tfs_mat"
* Verify material has changed - Already On Build Cause Section
* Verify modification "0" is checked in by "Modified by: CORPORATE\\sriniup on 2013-08-07T14:14:02+05:30" with comment "Comment: Changes Added"




Teardown of contexts 
* Capture go state "TfsMaterialSchedulingAndMaterialModification" - teardown
* With "1" live agents in directory "TfsMaterialSchedulingAndMaterialModification" - teardown
* Using pipeline "tfs-pipeline-with-multiple-stages" - teardown
* Tfs configuration - teardown


