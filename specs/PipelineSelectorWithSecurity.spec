PipelineSelectorWithSecurity
============================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using group "basic, admin-only, viewable, group.with.dot,operable" - setup
* Capture go state "PipelineSelectorWithSecurity" - setup

PipelineSelectorWithSecurity
----------------------------

tags: 3843, UI, 5424, linux

* Turn on autoRefresh - On Pipeline Dashboard Page
* Open pipelines selector

* Verify groups "basic, admin-only, viewable, group.with.dot,operable" are visible - Already on pipelines selector section
* Verify all pipelines are selected
* Deselect all pipelines
* Verify no pipelines are selected
* Select all pipelines
* Verify all pipelines are selected
* Deselect group "basic"
* Verify all pipelines in group "basic" are deselected
* Deselect pipeline "run.till.file.exists" and verify "group.with.dot" is deselected
* Select pipeline "run.till.file.exists" and verify "group.with.dot" is selected
* Apply selections

* Turn on autoRefresh - Already On Pipeline Dashboard Page
* Verify group "basic" is not visible - Already On Pipeline Dashboard Page
* Verify pipeline "basic-pipeline-run-till-file-exists" is not visible - Already On Pipeline Dashboard Page
* Verify group "admin-only" is visible
* Verify group "viewable" is visible
* Verify group " group.with.dot" is visible
* Verify group "operable" is visible

* Logout - On Any Page

* Login as "view"

* Turn on autoRefresh - On Pipeline Dashboard Page
* Verify group "basic" is visible - On Pipeline Dashboard Page
* Verify group "viewable" is visible - On Pipeline Dashboard Page
* Verify group "group.with.dot" is visible - On Pipeline Dashboard Page
* Verify group "admin-only" is not visible
* Verify group "operable" is not visible
* Open pipelines selector

* Verify groups "basic, viewable, group.with.dot" are visible - Already on pipelines selector section
* Verify groups "admin-only,operable" are not visible - Already on pipelines selector section
* Deselect group "group.with.dot"
* Apply selections

* Turn on autoRefresh - Already On Pipeline Dashboard Page
* Verify group "basic" is visible
* Verify group "viewable" is visible
* Verify group "group.with.dot" is not visible - Already On Pipeline Dashboard Page
* Verify group "admin-only" is not visible - Already On Pipeline Dashboard Page
* Verify group "operable" is not visible - Already On Pipeline Dashboard Page
* Verify pipeline "basic-pipeline-run-till-file-exists" is visible - Already On Pipeline Dashboard Page
* Verify pipeline "run.till.file.exists" is not visible - Already On Pipeline Dashboard Page

* Logout - On Any Page

* Login as "admin"

* Verify group "basic" is not visible
* Verify group "group.with.dot" is visible - On Pipeline Dashboard Page
* Verify group "viewable" is visible - On Pipeline Dashboard Page
* Verify group "admin-only" is visible - On Pipeline Dashboard Page
* Verify group "operable" is visible - On Pipeline Dashboard Page
* Open pipelines selector


* Verify groups "basic, admin-only, viewable, group.with.dot,operable" are visible - Already on pipelines selector section

* Logout and login as "operate"

* Turn on autoRefresh - On Pipeline Dashboard Page
* Verify group "basic" is visible - On Pipeline Dashboard Page
* Verify group "viewable" is visible - On Pipeline Dashboard Page
* Verify group "group.with.dot" is visible - On Pipeline Dashboard Page
* Verify group "operable" is visible - On Pipeline Dashboard Page
* Verify group "admin-only" is not visible
* Open pipelines selector

* Verify groups "basic, viewable, group.with.dot,operable" are visible - Already on pipelines selector section
* Verify groups "admin-only" are not visible - Already on pipelines selector section

* Logout and login as "operatorUser"

* Turn on autoRefresh - On Pipeline Dashboard Page
* Verify group "basic" is visible - On Pipeline Dashboard Page
* Verify group "viewable" is visible - On Pipeline Dashboard Page
* Verify group "group.with.dot" is visible - On Pipeline Dashboard Page
* Verify group "admin-only" is not visible
* Verify group "operable" is not visible
* Open pipelines selector

* Verify groups "basic, viewable, group.with.dot" are visible - Already on pipelines selector section
* Verify groups "admin-only,operable" are not visible - Already on pipelines selector section





Teardown of contexts
* Capture go state "PipelineSelectorWithSecurity" - teardown
* Using group "basic, admin-only, viewable, group.with.dot,operable" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


