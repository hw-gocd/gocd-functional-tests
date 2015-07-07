TfsMaterial-DuplicateMaterials
==============================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "tfs-pipeline-with-duplicate-materials" - setup
* With "1" live agents in directory "TfsMaterial-DuplicateMaterials" - setup
* Capture go state "TfsMaterial-DuplicateMaterials" - setup

TfsMaterial-DuplicateMaterials
------------------------------

tags: #5799, 5799, tfs

* Looking at pipeline "tfs-pipeline-with-duplicate-materials"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"

* Click on pipeline "tfs-pipeline-with-duplicate-materials" for editing

* Open material listing page

* Edit material "tfs_mat_1"

* Enter url "integration_tests" - Already on tfs material creation popup
* Enter project path as "$/for_tests"
* Click save - Already on tfs material creation popup

* Looking at pipeline "tfs-pipeline-with-duplicate-materials"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "2"




Teardown of contexts 
* Capture go state "TfsMaterial-DuplicateMaterials" - teardown
* With "1" live agents in directory "TfsMaterial-DuplicateMaterials" - teardown
* Using pipeline "tfs-pipeline-with-duplicate-materials" - teardown
* Basic configuration - teardown


