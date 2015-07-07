GitPipeline
===========

Setup of contexts 
* Basic configuration - setup
* Using pipeline "git-pipeline" - setup
* With "1" live agents in directory "git_pipeline" - setup
* Capture go state "GitPipeline" - setup

GitPipeline
-----------

tags: git, automate

* With external material of "git-submodule" for pipeline "git-pipeline"
* Checkin file "new_file" as user "twist <twist@thoughtworks.com>" with message "Added new_file"
* With material "git-submodule" for pipeline "git-pipeline"
* Checkin git submodule reference

* Setting first stage to auto approval

* Looking at pipeline "git-pipeline"
* Wait for stage "defaultStage" status to be "Building" with label "1"
* Navigate to stage "defaultStage" of run "1"

* Turn on auto refresh
* Wait for jobs to show "In Progress: 1" with jobs "defaultJob"

* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Navigate to stage "defaultStage" of run "1"

* Turn on auto refresh
* Wait for jobs to show "Passed: 1" with jobs "defaultJob"

* Open changes section for counter "1"

* Looking at material of type "Git" named "git-submodule" for pipeline "git-pipeline" with counter "1"
* Verify modification "0" has comment containing "Updated submodule"
* Verify material has changed

* Looking at pipeline "git-pipeline"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

* Open console tab
* Verify console contains submodule status for dir "referenced-submodule" and ref "heads/master"

* With material "git-submodule" for pipeline "git-pipeline"
* Checkin file "new_file_2" as user "foo <foo@bar.com>" with message "This is a one line description.\n\nThis should be on a new paragraph"

* Looking at pipeline "git-pipeline"
* Wait for stage "defaultStage" status to be "Building" with label "2"
* Navigate to stage "defaultStage" of run "2"

* Turn on auto refresh
* Wait for jobs to show "In Progress: 1" with jobs "defaultJob"

* Looking at pipeline "git-pipeline"
* Stop "1" jobs waiting for file to exist - On Pipeline Dashboard Page
* Navigate to stage "defaultStage" of run "2"

* Turn on auto refresh
* Wait for jobs to show "Passed: 1" with jobs "defaultJob"

* Looking at pipeline "git-pipeline"
* Open changes section for counter "2"





Teardown of contexts 
* Capture go state "GitPipeline" - teardown
* With "1" live agents in directory "git_pipeline" - teardown
* Using pipeline "git-pipeline" - teardown
* Basic configuration - teardown


