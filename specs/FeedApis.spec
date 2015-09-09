FeedApis
========

Setup of contexts
* Basic configuration - setup
* Using pipeline "mingle-config-parent, two-stage-pipeline-with-mingle-config" - setup
* With "1" live agents in directory "NOT-USED" - setup
* Logout on exit - setup
* Capture go state "FeedApis" - setup

FeedApis
--------

tags: 3351, automate, 3365, feeds, shine

* Looking at pipeline "mingle-config-parent"
* Trigger pipelines "mingle-config-parent" and wait for labels "hello-world-1" to pass

* Trigger pipelines "two-stage-pipeline-with-mingle-config" and wait for labels "1" to pass
* Trigger pipelines "two-stage-pipeline-with-mingle-config" and wait for labels "2" to pass
* Navigate to stage "defaultStage" of run "2"

* Rerun stage "defaultStage"

* Looking at pipeline "two-stage-pipeline-with-mingle-config"
* Verify stage "1" is "Passed" on pipeline with label "2"

* For pipeline "two-stage-pipeline-with-mingle-config" - Stages Feed Xml
* Verify stage link for current pipeline with counter "1" and stage "defaultStage" with stage counter "1" is approved by "anonymous"
* Verify stage link for current pipeline with counter "2" and stage "defaultStage" with stage counter "1" is approved by "anonymous"
* Verify stage link for current pipeline with counter "2" and stage "defaultStage" with stage counter "2" is approved by "anonymous"
* Verify stage named "defaultStage" having pipeline counter "1" and stage counter "1" is triggered by "anonymous"
* Verify stage named "defaultStage" having pipeline counter "1" and stage counter "1" has commit author from latest commit of material with name "pipeline-hg"

* With material named "pipeline-hg" in pipeline "two-stage-pipeline-with-mingle-config"
* Checkin file "foo.txt" as user "user" with message "User's Story #300"
* Checkin file "bar.txt" as user "loser" with message "Loser's Story #4000"
* With material named "pipeline-git" in pipeline "two-stage-pipeline-with-mingle-config"
* Checkin file "baz.txt" as user "git-user <foo@bar.com>" with message "User's story #6000"
* Checkin file "quux.txt" as user "git-loser <foo@bar.com>" with message "Loser's story #300"

* Trigger pipelines "two-stage-pipeline-with-mingle-config" and wait for labels "3" to pass

* For pipeline "two-stage-pipeline-with-mingle-config" - Stages Feed Xml
* Verify stage link for current pipeline with counter "3" and stage "defaultStage" with stage counter "1" is approved by "anonymous"
* Verify stage named "defaultStage" having pipeline counter "3" and stage counter "1" has commit author "user, loser, git-user <foo@bar.com>, git-loser <foo@bar.com>"
* Verify stage named "defaultStage" having pipeline counter "3" and stage counter "1" having cards "#300, #4000, #6000" linked to "https://some.mingle.machine:1000/mingle" project "some-go-branch"

* Add security with password file and users "admin" as admin

* Logout and login as "admin"

* Trigger pipelines "two-stage-pipeline-with-mingle-config" and wait for labels "4" to pass

* For pipeline "two-stage-pipeline-with-mingle-config" - Stages Feed Xml
* Verify stage link for current pipeline with counter "4" and stage "defaultStage" with stage counter "1" is approved by "admin"

* Logout and login as "view"

* For pipeline "two-stage-pipeline-with-mingle-config" - Stages Feed Xml
* Verify stage link for current pipeline with counter "4" and stage "defaultStage" with stage counter "1" is approved by "admin"





Teardown of contexts
* Capture go state "FeedApis" - teardown
* Logout on exit - teardown
* With "1" live agents in directory "NOT-USED" - teardown
* Using pipeline "mingle-config-parent, two-stage-pipeline-with-mingle-config" - teardown
* Basic configuration - teardown


