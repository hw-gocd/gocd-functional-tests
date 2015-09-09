ArtifactMD5VerificationFailure
==============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "artifact-md5-mismatch" - setup
* Capture go state "ArtifactMD5VerificationFailure" - setup
* With "1" live agents in directory "ArtifactsMD5Failure" - setup

ArtifactMD5VerificationFailure
------------------------------

tags: #2408, Agent, Artifacts, MD5

Failure Scenario - MD5 Mismatch
* With material named "junit-failures-material" in pipeline "artifact-md5-mismatch"
* Checkin file "new_artifact.txt" as user "user" with message "Comment user"

* Trigger pipelines "artifact-md5-mismatch" and wait for labels "1" to pass
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Go to jobs tab
* Navigate to job "defaultJob"

* Open console tab
* Verify in console that artifact "new_artifact.txt" was uploaded to ""
* Verify artifacts tab contains file "new_artifact.txt"
* Verify artifacts tab contains file "md5.checksum" in dir "cruise-output"

* For pipeline "artifact-md5-mismatch" label "1" stage "defaultStage" counter "1" job "defaultJob"
* Append "foo bar baz" to artifact "new_artifact.txt"
* Verify return code is "200" - Using Artifact Api

* Navigate to stage "defaultStage" of run "1" having counter "1"

* Trigger stage "secondStage"

* Looking at pipeline "artifact-md5-mismatch"
* Verify stage "2" is "Failed" on pipeline with label "1"
* Navigate to stage "secondStage" of run "1" having counter "1"

* Go to jobs tab
* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "[ERROR] Verification of the integrity of the artifact [new_artifact.txt] failed. The artifact file on the server may have changed since its original upload."









Teardown of contexts
* With "1" live agents in directory "ArtifactsMD5Failure" - teardown
* Capture go state "ArtifactMD5VerificationFailure" - teardown
* Using pipeline "artifact-md5-mismatch" - teardown
* Basic configuration - teardown


