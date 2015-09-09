GlobalMessages
==============

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast" - setup
* Capture go state "GlobalMessages" - setup

GlobalMessages
--------------

tags: 3540, global messages, automate

* Make pipeline "basic-pipeline-fast" use non existant material
* Changing the artifacts location to "somethingNew"

* Trigger pipeline

* Verify there are at least "1" errors
* Verify there are "1" warnings

* Verify there are at least "1" errors
* Verify there are "1" warnings
* Open error and warning messages popup

* Verify error "message" contains "Could not trigger pipeline"
* Verify warning "message" contains "The change in the artifacts directory location will not take effect until the Go Server is restarted"

* Changing the artifacts location to "artifacts"

* Verify there are at least "1" errors
* Verify there are no warnings

* Verify there are at least "1" errors
* Verify there are no warnings
* Open error and warning messages popup

* Verify warning "message" do not contain "The change in the artifacts directory location will not take effect until the Go Server is restarted"
* Close




Teardown of contexts
* Capture go state "GlobalMessages" - teardown
* Using pipeline "basic-pipeline-fast" - teardown
* Basic configuration - teardown


