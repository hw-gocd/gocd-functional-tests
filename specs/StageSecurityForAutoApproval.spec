StageSecurityForAutoApproval
============================

     |userName    |
     |------------|
     |operate     |
     |operatorUser|
Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-with-auto-stage-security" - setup
* With "1" live agents in directory "StageSecurity" - setup
* Capture go state "StageSecurityForAutoApproval" - setup

StageSecurityForAutoApproval
----------------------------

tags: 2400, passwordfile support, authorisation, authentication, svn support, 1547, security, restful api, automate

* Looking at pipeline "pipeline-with-auto-stage-security"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"

* Stop "1" jobs that are waiting for file to exist

* Looking at pipeline "pipeline-with-auto-stage-security" - Already On Pipeline Dashboard Page
* Verify stage "1" is "Passed" on pipeline with label "1" - Already On Pipeline Dashboard Page

* Logout - On Any Page

* Login as "view"

* Logged in as "view"

* Looking at pipeline "pipeline-with-auto-stage-security"
* Verify cannot trigger pipeline
* Verify trigger with option is disabled
* Navigate to stage "first" of run "1"

* Verify stage "first" does not have any action

* Logout - On Any Page

* Login as <userName>

* Logged in as <userName>

* Looking at pipeline "pipeline-with-auto-stage-security"
* Verify can trigger pipeline
* Verify trigger with option is enabled
* Navigate to stage "first" of run "1"

* Verify stage "first" has action "Rerun"
* Rerun stage "first"
* Verify stage "first" has action "Cancel"
* Cancel "first" - Already On Stage Detail Page




Teardown of contexts
* Capture go state "StageSecurityForAutoApproval" - teardown
* With "1" live agents in directory "StageSecurity" - teardown
* Using pipeline "pipeline-with-auto-stage-security" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


