TaskReordering
==============

Setup of contexts 
* Basic configuration - setup
* Using pipeline "edit-pipeline-with-tasks" - setup
* Capture go state "TaskReordering" - setup

TaskReordering
--------------

tags: Clicky Admin, 4894

* Click on pipeline "edit-pipeline-with-tasks" for editing

* Open stage listing page

* Open stage "defaultStage"

* Open jobs

* Open job "defaultJob"

* Open tasks

* Verify task "1" is "Ant" task without on cancel and properties "Target: longsleep, Working Directory: hg/dev" that runs if state is "Passed"
* Verify task "2" is "Rake" task without on cancel and properties "Target: all, Working Directory: hg/dev" that runs if state is "Passed"
* Verify task "3" is "NAnt" task without on cancel and properties "Target: all, Working Directory: hg/dev" that runs if state is "Passed"
* Move down task "1"
* Verify task "1" is "Rake" task without on cancel and properties "Target: all, Working Directory: hg/dev" that runs if state is "Passed"
* Verify task "2" is "Ant" task without on cancel and properties "Target: longsleep, Working Directory: hg/dev" that runs if state is "Passed"
* Move up task "3"
* Verify task "2" is "NAnt" task without on cancel and properties "Target: all, Working Directory: hg/dev" that runs if state is "Passed"
* Verify task "3" is "Ant" task without on cancel and properties "Target: longsleep, Working Directory: hg/dev" that runs if state is "Passed"





Teardown of contexts 
* Capture go state "TaskReordering" - teardown
* Using pipeline "edit-pipeline-with-tasks" - teardown
* Basic configuration - teardown


