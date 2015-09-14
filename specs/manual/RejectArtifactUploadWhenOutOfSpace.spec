RejectArtifactUploadWhenOutOfSpace
==================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "artifact-reject-pipeline" - setup
* With "1" live agents in directory "ArtifactsReject" - setup
* Unmount artifacts directory - setup

RejectArtifactUploadWhenOutOfSpace
----------------------------------

tags: 5131, artifact reject, manual


* commit file "create_file.rake"
* commit file "kilo-file"

* looking at pipeline "artifact-reject-pipeline"
* trigger pipeline
* verify stage "1" is "Passed" on pipeline with label "1"
* navigate to stage "defaultStage" of run "1" having counter "1"

* navigate to job "defaultJob"

* verify console does not contain "Artifact upload for file big_file.txt was denied by the server. This usually happens when server runs out of disk space."

* click on pipeline "artifact-reject-pipeline" for editing

* go to environment variables page

* delete variable
* click save
* enter environment variable "1" name "SIZE" and value "6"
* click save

* point the artifact repository to a partition of size "116" MB

* looking at pipeline "artifact-reject-pipeline"
* trigger pipeline
* verify stage "1" is "Failed" on pipeline with label "2"
* navigate to stage "defaultStage" of run "2" having counter "1"

* navigate to job "defaultJob"

* verify console contains "Artifact upload for file /home/cruise/projects/cruise_qa/target/twist-agents/scn-01-01/pipelines/${runtime_name:artifact-reject-pipeline}/hg/big_file.txt was denied by the server. This usually happens when server runs out of disk space."







Teardown of contexts
* Unmount artifacts directory - teardown
* With "1" live agents in directory "ArtifactsReject" - teardown
* Using pipeline "artifact-reject-pipeline" - teardown
* Basic configuration - teardown


