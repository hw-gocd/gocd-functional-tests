UploadAndFetchArtifactOfVariableSizes
=====================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "pipeline_uploading_large_artifact, pipeline_downloading_large_artifact" - setup
* With "1" live agents in directory "UploadAndFetchArtifactOfVariableSizes" - setup
* Capture go state "UploadAndFetchArtifactOfVariableSizes" - setup

UploadAndFetchArtifactOfVariableSizes
-------------------------------------

tags: #6350, Fetch Artifact, jre7, manual

* looking at pipeline "pipeline_uploading_large_artifact"
* trigger pipeline
* verify stage "1" is "Passed" on pipeline with label "1"
* looking at pipeline "pipeline_downloading_large_artifact"
* trigger pipeline
* verify stage "1" is "Passed" on pipeline with label "1"




Teardown of contexts
* Capture go state "UploadAndFetchArtifactOfVariableSizes" - teardown
* With "1" live agents in directory "UploadAndFetchArtifactOfVariableSizes" - teardown
* Using pipeline "pipeline_uploading_large_artifact, pipeline_downloading_large_artifact" - teardown
* Basic configuration - teardown


