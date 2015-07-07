SeeWhatActuallyChangedSinceTheLastPipelineRun
=============================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "svn-pipeline" - setup
* With "1" live agents in directory "SeeWhatActuallyChangedSinceLastPipelineRun" - setup
* Capture go state "SeeWhatActuallyChangedSinceTheLastPipelineRun" - setup

SeeWhatActuallyChangedSinceTheLastPipelineRun
---------------------------------------------

tags: 2414, 3032, svn support, scheduling, dashboard, diagnostics messages, automate

* Looking at pipeline "svn-pipeline"
* Trigger pipeline "svn-pipeline"
* Wait for first stage to pass with pipeline label "1"

* With material named "svn" in pipeline "svn-pipeline"
* Checkin file "foo.txt" as user "twist" with message "Added foo.txt"

* Looking at pipeline "svn-pipeline"
* Trigger pipeline "svn-pipeline"
* Wait for first stage to pass with pipeline label "2"
* Navigate to stage "defaultStage" of run "2"

* Navigate to job "svn-pipeline-job"

* Verify material tab contains revision "Revision: 4, modified by twist"
* Verify revision "Revision: 4, modified by twist" is marked as changed
* Verify latest revision for material with name "hg" and destination folder "hg" is not marked as changed

Marked as changed is verified by looking at the css class "highlight-true"




Teardown of contexts 
* Capture go state "SeeWhatActuallyChangedSinceTheLastPipelineRun" - teardown
* With "1" live agents in directory "SeeWhatActuallyChangedSinceLastPipelineRun" - teardown
* Using pipeline "svn-pipeline" - teardown
* Basic configuration - teardown


