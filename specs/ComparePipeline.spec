ComparePipeline
===============

Setup of contexts
* Basic configuration - setup
* Using pipeline "up, down" - setup
* With "1" live agents in directory "card_activity" - setup
* Capture go state "ComparePipeline" - setup

ComparePipeline
---------------

tags: 4688, compare_pipeline, stage1

* Trigger pipelines "up" and wait for labels "1" to pass
* Click compare link

* Verify that "to" textbox is populated with "1"
* Verify that "from" textbox is populated with "1"

* With material named "hg-material" in pipeline "up"
* Checkin file "foo.txt" as user "user" with message "Comment user"
* Remember current version as "FIRST_REVISION"
* Checkin file "bar.txt" as user "luser" with message "Comment loser"
* Remember current version as "SECOND_REVISION"

* Trigger pipelines "up" and wait for labels "2" to pass
* Trigger pipelines "down" and wait for labels "1" to pass
* Looking at pipeline "up"
* Click compare link

* Verify that "from" textbox is populated with "1"
* Verify that "to" textbox is populated with "2"

* With material named "hg-material" in pipeline "up"
* Checkin file "foo1.txt" as user "user" with message "second checkin comment"
* Remember current version as "THIRD_REVISION"

* Trigger pipelines "up" and wait for labels "3" to pass
* Trigger pipelines "down" and wait for labels "2" to pass
* Looking at pipeline "up"
* Click compare link

Exact matching labels
* Verify that "from" textbox is populated with "2"
* Verify that "to" textbox is populated with "3"
* Search for "1" on "from" textbox
* Click on label "1" in the dropdown
* Verify that "from" textbox is populated with "1"
* Verify that "to" textbox is populated with "3"

Match revision
* Search for revision "SECOND_REVISION" on "to" textbox
* Click on label "2" in the dropdown
* Verify that "from" textbox is populated with "1"
* Verify that "to" textbox is populated with "2"

Match partial user
* Search for "user" on "from" textbox
* Verify dropdown has labels "3,2"
* Click on label "2" in the dropdown
* Verify that "from" textbox is populated with "2"
* Verify that "to" textbox is populated with "2"

Match triggered user
* Search for "anony" on "from" textbox
* Verify dropdown has labels "1"
* Click on label "1" in the dropdown

Match partial comment
* Search for "comm" on "to" textbox
* Verify dropdown has labels "3,2"
* Click on label "3" in the dropdown
* Verify that "from" textbox is populated with "1"
* Verify that "to" textbox is populated with "3"

Downstream
* Looking at pipeline "down"
* Click compare link

* Verify that "from" textbox is populated with "1"
* Verify that "to" textbox is populated with "2"
* Search for "2" on "to" textbox
* Click on label "1" in the dropdown




Teardown of contexts
* Capture go state "ComparePipeline" - teardown
* With "1" live agents in directory "card_activity" - teardown
* Using pipeline "up, down" - teardown
* Basic configuration - teardown


