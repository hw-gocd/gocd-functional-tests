NewStageCancellation
====================

Setup of contexts
* Pipeline "test" with cancel tasks - setup
* Capture go state "NewStageCancellation" - setup

NewStageCancellation
--------------------

tags: 2511, diagnostics messages, ant support, cancel, 2511, in-progress, personal notification, svn support, scheduling, manual


Possibly use - http://quintanasoft.com/dumbster

Old twist tests: CancellingStageRunsOnCancelTask, CancellingAStageSendsAnEmailWithUserInformation

* configure cruise with email notification and stage "test" with on cancel task
* open pipeline dashboard
* trigger build
* verify job is assigned to an agent
* cancel stage on pipeline "test"
* verify job is cancelled
* Wait for console to contain "Start to execute cancel task:"
* verify email contains "The stage was cancelled by "






Teardown of contexts
* Capture go state "NewStageCancellation" - teardown
* Pipeline "test" with cancel tasks - teardown


