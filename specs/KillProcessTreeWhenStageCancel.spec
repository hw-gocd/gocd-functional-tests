KillProcessTreeWhenStageCancel
==============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "process-tree" - setup
* With "1" live agents in directory "kill_process_tree" - setup
* Capture go state "KillProcessTreeWhenStageCancel" - setup

KillProcessTreeWhenStageCancel
------------------------------

tags: 3544, automate, cancel, kill-process

* Commit file "fork_self.rake"

* Looking at pipeline "process-tree"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

* Wait for log "Current counter 1"

* Looking at pipeline "process-tree"
* Navigate to stage "defaultStage" of run "1"

* Cancel "defaultStage" - Already On Stage Detail Page

* Wait for agent to show status "idle"

* Looking at pipeline "process-tree"
* Navigate to stage "defaultStage" of run "1"

* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "Current counter 10"
* Verify console contains "Current counter 2"
* Verify console contains "Current counter 1"
* Verify console does not contain "Process was not killed, it returned."




Teardown of contexts
* Capture go state "KillProcessTreeWhenStageCancel" - teardown
* With "1" live agents in directory "kill_process_tree" - teardown
* Using pipeline "process-tree" - teardown
* Basic configuration - teardown


