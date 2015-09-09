AgentsWithSameUUID
==================

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast" - setup
* Capture go state "AgentsWithSameUUID" - setup

AgentsWithSameUUID
------------------

tags: agent management, same uuid issue, #3088, linux, 4378

MAKE THIS SCENARIO RUN IN WINDOWS ONCE THE BUG https://mingle05.thoughtworks.com/projects/cruise/cards/4378 is FIXED

* Start "1" agents with uUID "raghu420-4jj2-jake-gogo-pavan840yogi"

* Verify has "1" idle agents

* Start "1" agents with uUID "raghu420-4jj2-jake-gogo-pavan840yogi"

* Verify there are "1" warnings

* Start "1" agents with uUID "raghu420-4jj2-jake-gogo-pavan840yogi"

* Verify there are "2" warnings
* Open error and warning messages popup

* Verify warning "message" contains "has duplicate unique identifier"
* Verify warning "description" contains "Please check the agent installation."

* Verify has "1" idle agents

* Restart agent "0" using a new uUID

* Verify has "2" idle agents

* Verify there are "1" warnings

* Restart agent "1" using a new uUID

* Verify has "3" idle agents

* Wait for warnings to disappear

* Trigger pipelines "basic-pipeline-fast" and wait for labels "1" to pass





Teardown of contexts
* Capture go state "AgentsWithSameUUID" - teardown
* Using pipeline "basic-pipeline-fast" - teardown
* Basic configuration - teardown


