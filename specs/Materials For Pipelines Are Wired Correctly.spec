Materials For Pipelines Are Wired Correctly
===========================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "junit-tests" - setup
* With "1" live agents in directory "StageDetailsShineIntegration" - setup
* Capture go state "Materials for pipelines are wired correctly" - setup

Materials For Pipelines Are Wired Correctly
-------------------------------------------

tags: materials, shine

Smoke test to check if the query to get the users on the changesets that triggered pipelines are returned correctly.

* With material named "junit-tests-material" in pipeline "junit-tests"
* Commit file "junit-failures/fail-a-fail-b/TEST-cruise.testing.JUnit.xml" to directory "junit-output" as user "ted"
* Commit file "junit-failures/fail-a-pass-b/TEST-cruise.testing.JUnit.xml" to directory "junit-output" as user "bill"

* Looking at pipeline "junit-tests"
* Trigger pipeline

* Fail "1" jobs that are waiting for file to exist

* Looking at pipeline "junit-tests"
* Wait for first stage to fail with pipeline label "1"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Go to tests tab
* Wait for shine feed to update
* Verify total runs "2" failures "1" errors "0"
* Verfy pipeline "1" modified by "bill"







Teardown of contexts
* Capture go state "Materials for pipelines are wired correctly" - teardown
* With "1" live agents in directory "StageDetailsShineIntegration" - teardown
* Using pipeline "junit-tests" - teardown
* Basic configuration - teardown


