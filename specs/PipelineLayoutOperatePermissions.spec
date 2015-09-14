PipelineLayoutOperatePermissions
================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "2-stage-viewable" - setup
* With "1" live agents in directory "PipelineLayout" - setup
* Capture go state "PipelineLayoutOperatePermissions" - setup

PipelineLayoutOperatePermissions
--------------------------------

tags: 3657, pipeline layout, automate

* Looking at pipeline "2-stage-viewable"
* Trigger pipeline "2-stage-viewable"
* Wait for first stage to pass with pipeline label "1"
* Navigate to stage "first" of run "1" having counter "1"

* Wait for jobs to show "Passed: 1" with jobs "defaultJob"
* Verify stage "first" has action "Rerun"
* Verify stage "second" has action "Trigger"

* Logout - On Any Page

* Login as "view"

* Looking at pipeline "2-stage-viewable"
* Navigate to stage "first" of run "1" having counter "1"

* Verify stage "first" does not have any action
* Verify stage "second" does not have any action

* Logout - On Any Page

* Login as "operate"

* Looking at pipeline "2-stage-viewable"
* Navigate to stage "first" of run "1" having counter "1"

* Verify stage "first" has action "Rerun"
* Verify stage "second" does not have actions link





Teardown of contexts
* Capture go state "PipelineLayoutOperatePermissions" - teardown
* With "1" live agents in directory "PipelineLayout" - teardown
* Using pipeline "2-stage-viewable" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


