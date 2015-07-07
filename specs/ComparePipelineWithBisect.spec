ComparePipelineWithBisect
=========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "up" - setup
* Capture go state "ComparePipelineWithBisect" - setup

ComparePipelineWithBisect
-------------------------

tags: 4688, compare_pipeline, 5789

* Trigger and cancel pipeline "up" "1" times

* With material named "hg-material" in pipeline "up"
* Checkin file "foo.txt" as user "user" with message "#10 - Comment user"
* Remember current version as "FIRST_REV"
* Sleep for "5" seconds
* Checkin file "bar.txt" as user "luser" with message "#15 - Another comment loser"
* Remember current version as "SECOND_REV"

* Trigger and cancel "up" pipeline "1" times starting with label "1"
* Open trigger with options

* Using material "hg-material"
* Search for "Comment user"
* Select revision "1" in search box
* Trigger

* Looking at pipeline "up"
* Verify stage "1" is "Building" on pipeline with label "3"
* Navigate to stage "defaultStage" of run "3"

* Cancel "defaultStage" - Already On Stage Detail Page

* Looking at pipeline "up"
* Verify stage "1" is "Cancelled" on pipeline with label "3"
* Click compare link

* Verify that "from" textbox is populated with "2"
* Verify that "to" textbox is populated with "3"
* Verify that there are "0" materials
* Verify that there is message "This comparison involves a pipeline instance that was triggered with a non-sequential material revision."
* Opt to see bisect diff
* Verify that there is a warning message "This comparison involves a pipeline instance that was triggered with a non-sequential material revision."
* Verify that there are "1" materials
* Verify displays revision "SECOND_REV" having comment "#15 - Another comment loser" under "Mercurial" named "hg-material" for pipeline "up"

* Verify card activity between pipeline "up" counters "2" and "3" is "" with show _ bisect "false"
* Verify card activity between pipeline "up" counters "2" and "3" is "15,10" with show _ bisect "true"




Teardown of contexts 
* Capture go state "ComparePipelineWithBisect" - teardown
* Using pipeline "up" - teardown
* Basic configuration - teardown


