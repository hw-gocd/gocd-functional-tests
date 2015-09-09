LogNotificationPlugin
=====================

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast,basic-pipeline-fail,basic-pipeline-run-till-file-exists" - setup
* With "1" live agents in directory "PluginAgents" - setup
* Capture go state "LogNotificationPlugin" - setup

LogNotificationPlugin
---------------------

tags: plugins-tests

* Open "Plugins" tab

* Verify plugin with id "log.notifier" is loaded

* Store current state

* Looking at pipeline "basic-pipeline-fast"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"

* Looking at pipeline "basic-pipeline-fail"
* Trigger pipeline
* Verify stage "1" is "Failed" on pipeline with label "1"

* Looking at pipeline "basic-pipeline-run-till-file-exists"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Navigate to stage "defaultStage" of run "1"

* Cancel "defaultStage" - Already On Stage Detail Page
* Wait for stage result to show "Cancelled"

* Wait a moment
* Verify has "6" new entries
* Verify entry "0" "basic-pipeline-fast" "1" "defaultStage" "1" "Building" "Unknown"
* Verify entry "1" "basic-pipeline-fast" "1" "defaultStage" "1" "Passed" "Passed"
* Verify entry "2" "basic-pipeline-fail" "1" "defaultStage" "1" "Building" "Unknown"
* Verify entry "3" "basic-pipeline-fail" "1" "defaultStage" "1" "Failed" "Failed"
* Verify entry "4" "basic-pipeline-run-till-file-exists" "1" "defaultStage" "1" "Building" "Unknown"
* Verify entry "5" "basic-pipeline-run-till-file-exists" "1" "defaultStage" "1" "Cancelled" "Cancelled"





Teardown of contexts
* Capture go state "LogNotificationPlugin" - teardown
* With "1" live agents in directory "PluginAgents" - teardown
* Using pipeline "basic-pipeline-fast,basic-pipeline-fail,basic-pipeline-run-till-file-exists" - teardown
* Basic configuration - teardown


