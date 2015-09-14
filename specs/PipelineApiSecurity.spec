PipelineApiSecurity
===================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline-fast, viewable-pipeline, admin-pipeline" - setup
* With "1" live agents in directory "pipeline_api_security" - setup
* Capture go state "PipelineApiSecurity" - setup

PipelineApiSecurity
-------------------

tags: 3351, automate, 3086, schedule, trigger, restful api, 3453

* Enable auto update for pipeline "basic-pipeline-fast"
* Enable auto update for pipeline "viewable-pipeline"
* Enable auto update for pipeline "admin-pipeline"

* Logged in as "admin"

* For pipeline "basic-pipeline-fast" - Using pipeline api
* Schedule should return code "202"
* For pipeline "viewable-pipeline" - Using pipeline api
* Schedule should return code "202"
* For pipeline "admin-pipeline" - Using pipeline api
* Schedule should return code "202"

* Looking at pipeline "basic-pipeline-fast"
* Wait for stage "defaultStage" status to be "Passed" with label "1"
* Looking at pipeline "viewable-pipeline"
* Wait for stage "defaultStage" status to be "Passed" with label "1"
* Looking at pipeline "admin-pipeline"
* Wait for stage "defaultStage" status to be "Passed" with label "1"

* With material named "basic-pipeline-hg" in pipeline "basic-pipeline-fast"
* Checkin file "file1" as user "user" with message "commiting file1"
* Checkin file "file2" as user "user2" with message "commiting file2"
* With material named "viewable-pipeline-hg" in pipeline "viewable-pipeline"
* Checkin file "file1" as user "user" with message "commiting file1"
* Checkin file "file2" as user "user2" with message "commiting file2"
* With material named "admin-pipeline-hg" in pipeline "admin-pipeline"
* Checkin file "file1" as user "user" with message "commiting file1"
* Checkin file "file2" as user "user2" with message "commiting file2"

* For pipeline "basic-pipeline-fast" - Using pipeline api
* Using "2nd" last revision of "basic-pipeline-hg"
* Schedule should return code "202"
* For pipeline "viewable-pipeline" - Using pipeline api
* Using "2nd" last revision of "viewable-pipeline-hg"
* Schedule should return code "202"
* For pipeline "admin-pipeline" - Using pipeline api
* Using "2nd" last revision of "admin-pipeline-hg"
* Schedule should return code "202"

* Looking at pipeline "basic-pipeline-fast"
* Wait for stage "defaultStage" status to be "Passed" with label "2"
* Navigate to stage "defaultStage" of run "2"

* Navigate to job "defaultJob"

* Open console tab
* Verify console shows "2nd" commit for material "basic-pipeline-hg" for "basic-pipeline-fast"

* Looking at pipeline "viewable-pipeline"
* Wait for stage "defaultStage" status to be "Passed" with label "2"
* Navigate to stage "defaultStage" of run "2"

* Navigate to job "defaultJob"

* Open console tab
* Verify console shows "2nd" commit for material "viewable-pipeline-hg" for "viewable-pipeline"

* Looking at pipeline "admin-pipeline"
* Wait for stage "defaultStage" status to be "Passed" with label "2"
* Navigate to stage "defaultStage" of run "2"

* Navigate to job "defaultJob"

* Open console tab
* Verify console shows "2nd" commit for material "admin-pipeline-hg" for "admin-pipeline"

* Logged in as "view"

* For pipeline "basic-pipeline-fast" - Using pipeline api
* Schedule should return code "202"
* For pipeline "viewable-pipeline" - Using pipeline api
* Schedule should return code "401"
* For pipeline "admin-pipeline" - Using pipeline api
* Schedule should return code "401"

* Looking at pipeline "basic-pipeline-fast"
* Wait for stage "defaultStage" status to be "Passed" with label "3"

* For pipeline "basic-pipeline-fast" - Using pipeline api
* Using "2nd" last revision of "basic-pipeline-hg"
* Schedule should return code "202"
* For pipeline "viewable-pipeline" - Using pipeline api
* Using "2nd" last revision of "viewable-pipeline-hg"
* Schedule should return code "401"
* For pipeline "admin-pipeline" - Using pipeline api
* Using "2nd" last revision of "admin-pipeline-hg"
* Schedule should return code "401"

* Looking at pipeline "basic-pipeline-fast"
* Wait for stage "defaultStage" status to be "Passed" with label "4"
* Navigate to stage "defaultStage" of run "4"

* Navigate to job "defaultJob"

* Open console tab
* Verify console shows "2nd" commit for material "basic-pipeline-hg" for "basic-pipeline-fast"

* Logged in as "operate"

* For pipeline "basic-pipeline-fast" - Using pipeline api
* Schedule should return code "202"
* For pipeline "viewable-pipeline" - Using pipeline api
* Schedule should return code "202"
* For pipeline "admin-pipeline" - Using pipeline api
* Schedule should return code "401"

* Looking at pipeline "basic-pipeline-fast"
* Wait for stage "defaultStage" status to be "Passed" with label "5"
* Looking at pipeline "viewable-pipeline"
* Wait for stage "defaultStage" status to be "Passed" with label "3"

* For pipeline "basic-pipeline-fast" - Using pipeline api
* Using "2nd" last revision of "basic-pipeline-hg"
* Schedule should return code "202"
* For pipeline "viewable-pipeline" - Using pipeline api
* Using "2nd" last revision of "viewable-pipeline-hg"
* Schedule should return code "202"
* For pipeline "admin-pipeline" - Using pipeline api
* Using "2nd" last revision of "admin-pipeline-hg"
* Schedule should return code "401"

* Looking at pipeline "basic-pipeline-fast"
* Wait for stage "defaultStage" status to be "Passed" with label "6"
* Navigate to stage "defaultStage" of run "6"

* Navigate to job "defaultJob"

* Open console tab
* Verify console shows "2nd" commit for material "basic-pipeline-hg" for "basic-pipeline-fast"

* Looking at pipeline "viewable-pipeline"
* Wait for stage "defaultStage" status to be "Passed" with label "4"
* Navigate to stage "defaultStage" of run "4"

* Navigate to job "defaultJob"

* Open console tab
* Verify console shows "2nd" commit for material "viewable-pipeline-hg" for "viewable-pipeline"





Teardown of contexts
* Capture go state "PipelineApiSecurity" - teardown
* With "1" live agents in directory "pipeline_api_security" - teardown
* Using pipeline "basic-pipeline-fast, viewable-pipeline, admin-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


