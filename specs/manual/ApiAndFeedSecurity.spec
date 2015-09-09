ApiAndFeedSecurity
==================

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast" - setup
* With "1" live agents in directory "NOT-USED" - setup
* Capture go state "ApiAndFeedSecurity" - setup

ApiAndFeedSecurity
------------------

tags: 3351, 3365, feeds, shine

* looking at pipeline "basic-pipeline-fast"
* trigger pipeline
* verify stage "1" is "Passed" on pipeline with label "1"
* trigger pipeline

* using "HTTP"

* Verify stage link for current pipeline with counter "1" and stage "defaultStage" with stage counter "1" is approved by    "anonymous"

* using "HTTPS"

* Verify stage link for current pipeline with counter "1" and stage "defaultStage" with stage counter "1" is approved by    "anonymous"

* using "BROWSER"

* Verify stage link for current pipeline with counter "1" and stage "defaultStage" with stage counter "1" is approved by    "anonymous"






Teardown of contexts
* Capture go state "ApiAndFeedSecurity" - teardown
* With "1" live agents in directory "NOT-USED" - teardown
* Using pipeline "basic-pipeline-fast" - teardown
* Basic configuration - teardown


