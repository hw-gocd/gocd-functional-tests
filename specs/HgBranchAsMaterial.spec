HgBranchAsMaterial
==================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "pipeline-using-hg-default-branch,pipeline-using-hg-branch" - setup
* With "1" live agents in directory "HgBranchAsMaterial" - setup
* Capture go state "HgBranchAsMaterial" - setup

HgBranchAsMaterial
------------------

tags: #7089, Hg branch

* Looking at pipeline "pipeline-using-hg-default-branch"
* Verify stage "1" is "Passed" on pipeline with label "1"
* Looking at pipeline "pipeline-using-hg-branch"
* Verify stage "1" is "Passed" on pipeline with label "1"

* With material named "hg-material" in pipeline "pipeline-using-hg-branch"
* Commit file "new_artifact.txt" to directory "baz"

* Looking at pipeline "pipeline-using-hg-branch"
* Verify stage "1" is "Passed" on pipeline with label "2"
* Looking at pipeline "pipeline-using-hg-default-branch"
* Verify pipeline is at label "1" and does not get triggered





Teardown of contexts 
* Capture go state "HgBranchAsMaterial" - teardown
* With "1" live agents in directory "HgBranchAsMaterial" - teardown
* Using pipeline "pipeline-using-hg-default-branch,pipeline-using-hg-branch" - teardown
* Basic configuration - teardown


