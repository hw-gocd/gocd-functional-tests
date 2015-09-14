StageDetailsViewAndOperatePermissions
=====================================

Setup of contexts
* Stage security configuration - setup
* Login as "admin" - setup
* Using pipeline "p1, p2, p3, p4" - setup
* Capture go state "StageDetailsViewAndOperatePermissions" - setup

StageDetailsViewAndOperatePermissions
-------------------------------------

tags: 6786, stage-details

* trigger pipeline "p1" and cancel it
* trigger pipeline "p2" and cancel it
* trigger pipeline "p3" and cancel it
* trigger pipeline "p4" and cancel it
* Looking at pipeline "p4"
* Navigate to stage "defaultStage" of run "1"

* Verify user can view config tab contents
* Trigger stage "stage2"
* Cancel "stage2" - Already On Stage Detail Page

//User - view

* Logout and login as "view"


* Looking at pipeline "p1"
* Navigate to stage "defaultStage" of run "1"
* Verify user cannot view config tab contents
* Verify rerun is disabled for stage "defaultStage"
* Go to jobs tab
* Verify rerun button is disabled

* verify user can operate stage "defaultStage" for pipeline "p2" from stage details page


* verify user can operate stage "defaultStage" for pipeline "p3" from stage details page


* verify user can operate stage "defaultStage" for pipeline "p4" from stage details page


* verify user cannot operate stage "stage2" for pipeline "p4" from stage details page


//User - operate

* Logout and login as "operate"


* Looking at pipeline "p1"
* Navigate to stage "defaultStage" of run "1"
* Verify user cannot view config tab contents
* Verify rerun is enabled for stage "defaultStage"
* Go to jobs tab
* Verify rerun button is enabled


* verify user can operate stage "defaultStage" for pipeline "p2" from stage details page


* verify user cannot operate stage "defaultStage" for pipeline "p4" from stage details page


* verify user can operate stage "stage2" for pipeline "p4" from stage details page


* Logout and login as "group1view"

* verify user cannot operate stage "defaultStage" for pipeline "p1" from stage details page

* verify user cannot operate stage "defaultStage" for pipeline "p2" from stage details page


* Looking at pipeline "p3"
* Navigate to stage "defaultStage" of run "1"
* Verify user cannot view config tab contents
* Verify rerun is enabled for stage "defaultStage"
* Go to jobs tab
* Verify rerun button is enabled


* verify user can operate stage "defaultStage" for pipeline "p4" from stage details page

* verify user cannot operate stage "stage2" for pipeline "p4" from stage details page




Teardown of contexts
* Capture go state "StageDetailsViewAndOperatePermissions" - teardown
* Using pipeline "p1, p2, p3, p4" - teardown
* Login as "admin" - teardown
* Stage security configuration - teardown


