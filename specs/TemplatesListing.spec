TemplatesListing
================

Setup of contexts
* Template admin configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1,pipeline2,pipeline3,pipeline-down,pipeline-without-template" - setup
* Capture go state "TemplatesViewerAndEditor" - setup

TemplatesListing
----------------

tags: 4600, Clicky Admin

* Open "Templates" tab

* Verify that templates "simple-pass,default.pipeline,unused" are present
* Verify that template "simple-pass" is used by pipelines "pipeline1,pipeline2,pipeline3"
* Verify that template "default.pipeline" is used by pipelines "pipeline-down"
* Verify that template "unused" has message "No pipelines associated with this template"
* Verify that edit pipeline "pipeline1" lands on pipeline edit page
* Verify cannot delete templates "simple-pass,default.pipeline"
* Verify can delete tempates "unused"
* Delete template "unused"
* Verify that templates "simple-pass,default.pipeline" are present
* Verify that templates "unused" are not present

* Logout and login as "group1Admin"

* Verify templates are visible





Teardown of contexts
* Capture go state "TemplatesViewerAndEditor" - teardown
* Using pipeline "pipeline1,pipeline2,pipeline3,pipeline-down,pipeline-without-template" - teardown
* Login as "admin" - teardown
* Template admin configuration - teardown


