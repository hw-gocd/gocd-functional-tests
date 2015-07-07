CruiseErrorMessages
===================

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline-with-all-materials" - setup
* With "1" live agents in directory "CruiseErrorMessages" - setup
* Capture go state "CruiseErrorMessages" - setup

CruiseErrorMessages
-------------------

tags: 1996, svn support, diagnostics messages, timer, 2272, automate, failing, linux

* Looking at pipeline "basic-pipeline-with-all-materials"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"

* Save config by name "LastValid"
* Make pipeline "basic-pipeline-with-all-materials" use all non existant material
* Using timer with invalid spec "* ? ? ? * ? 2012"

* Looking at pipeline "basic-pipeline-with-all-materials"
* Trigger pipeline
* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Navigate to pipeline dependencies for "basic-pipeline-with-all-materials" "1" "defaultStage" "1"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Navigate to stage "defaultStage" of run "1"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "description" contains "Failed to run git clone command"
* Verify error "description" contains "Failed to run hg clone command"
* Verify error "description" contains "Error performing command: --- Command --- svn log"
* Verify error "description" contains "Error performing command: --- Command --- p4 login"
* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "Invalid cron syntax"

* Using timer with spec "* * * * * ? 2012"

* Verify there are at least "4" errors
* Open error and warning messages popup

* Verify error "message" does not contain "Invalid Configuration"
* Verify error "description" does not contain "Invalid cron syntax"

* Looking at pipeline "basic-pipeline-with-all-materials"

* Make cruise config file invalid

* Verify there are at least "5" errors
* Open error and warning messages popup

* Verify error "message" contains "Invalid Configuration"
* Verify error "description" contains "XML document structures must start and end within the same entity"

* Looking at pipeline "basic-pipeline-with-all-materials"

* Restore config by name "LastValid"

* Verify there are no error messages

* Verify there are no error messages

* Verify there are no error messages

* Verify there are no error messages

* Verify there are no error messages

* Navigate to pipeline dependencies for "basic-pipeline-with-all-materials" "1" "defaultStage" "1"

* Verify there are no error messages

* Navigate to stage "defaultStage" of run "1"

* Verify there are no error messages

* Verify there are no error messages









Teardown of contexts 
* Capture go state "CruiseErrorMessages" - teardown
* With "1" live agents in directory "CruiseErrorMessages" - teardown
* Using pipeline "basic-pipeline-with-all-materials" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


