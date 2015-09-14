PageFooterAndHelp
=================

     |user name|
     |---------|
     |admin    |
     |view     |
Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Capture go state "PageFooterAndHelp" - setup

PageFooterAndHelp
-----------------

tags: 3246, automate

* Logout - On Any Page

* Login as <user name>

* Looking at pipeline "basic-pipeline"
* Trigger pipeline
* Wait for stage "defaultStage" status to be "Building" with label "1"
* Navigate to stage "defaultStage" of run "1"

* Wait for jobs to show "In Progress: 1" with jobs "defaultJob"

* Verify cruise footer

* Verify cruise footer - On Agents Page

* Verify cruise footer - On preferences page

* Verify cruise footer

* Verify cruise footer - On Server Detail Page

* Navigate to pipeline dependencies for "basic-pipeline" "1" "defaultStage" "1"

* Verify cruise footer - Already On Stage Detail Pipeline Dependencies Page

* Navigate to stage "defaultStage" of run "1"

* Verify cruise footer - Already On Stage Detail Page

* Verify cruise footer - On Environment Page




Teardown of contexts
* Capture go state "PageFooterAndHelp" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


