AdminTaskListing
================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "pipeline-ls" - setup
* Capture go state "AdminTaskListing" - setup

AdminTaskListing
----------------

tags: 4597, task, clicky, admin, exec, stage1

* Click on pipeline "pipeline-ls" for editing

* Open stage listing page

* Open stage "defaultStage"

* Open jobs

* Open job "defaultJob"

* Open tasks

* Verify task "1" is "Custom Command" task without on cancel and properties "Command: ls" that runs if state is "Passed"
* Open new task form "More..."


* Set "task[command](text_field): cat, task[argListString](text_area): /tmp/foo, task[workingDirectory](text_field): foo_bar" - Already on Task edit popup
* Set "task[runIfConfigsPassed](check_box): true, task[runIfConfigsFailed](check_box): true" - Already on Task edit popup
* Set "task[hasCancelTask](check_box): true" - Already on Task edit popup
* Select task "More..."
* Set "[execOnCancel][command](text_field): echo" - Already on Task edit popup
* Save and verify saved successfully

* Verify task "1" is "Custom Command" task without on cancel and properties "Command: ls" that runs if state is "Passed"
* Verify task "2" is "Custom Command" task with cancel "Custom Command" and properties "Command: cat, Arguments: /tmp/foo, Working Directory: foo_bar" that runs if state is "Failed, Passed"
* Delete task "1"
* Verify no task having "Command: ls" exists

* Verify no "exec" task with "command: ls" exists in "defaultJob" under "defaultStage"




Teardown of contexts 
* Capture go state "AdminTaskListing" - teardown
* Using pipeline "pipeline-ls" - teardown
* Basic configuration - teardown


