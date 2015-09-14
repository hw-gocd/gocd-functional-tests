ModificationsBetweenPipelines
=============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "mingle-config-parent, pipeline-with-mingle-config" - setup
* With "1" live agents in directory "card_activity" - setup
* Capture go state "ModificationsBetweenPipelines" - setup

ModificationsBetweenPipelines
-----------------------------

tags: 4521, card_activity, automate, 4520, mingle, 4523, checkins, linux

* Looking at pipeline "mingle-config-parent"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "hello-world-1"
* Looking at pipeline "pipeline-with-mingle-config"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"

* With material named "pipeline-hg" in pipeline "pipeline-with-mingle-config"
* Checkin file "foo.txt" as user "user" with message "Comment user"
* Remember current version as "hg-1-0"
* Checkin file "bar.txt" as user "loser" with message "Comment loser"
* Remember current version as "hg-1-1"
* Checkin file "baz.txt" as user "user-loser" with message "Comment loser-user"
* Remember current version as "hg-1-2"
* With material named "pipeline-git" in pipeline "pipeline-with-mingle-config"
* Checkin file "foo-git.c" as user "dev <dev@thoughtworks.com>" with message "foo added to git"
* Remember current version as "git-1-0"
* Checkin file "bar-git.c" as user "other-dev <other-dev@thoughtworks.com>" with message "bar added to git"
* Remember current version as "git-1-1"

* Looking at pipeline "pipeline-with-mingle-config"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "2"

* With material named "pipeline-hg" in pipeline "pipeline-with-mingle-config"
* Checkin file "hello.txt" as user "world" with message "hello world"
* Remember current version as "hg-2-0"
* Checkin file "world.txt" as user "hello" with message "world hello"
* Remember current version as "hg-2-1"
* With material named "pipeline-git" in pipeline "pipeline-with-mingle-config"
* Checkin file "hello-git.txt" as user "git-user <loser@thoughtworks.com>" with message "said hello to git"
* Remember current version as "git-2-0"

* Looking at pipeline "mingle-config-parent"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "hello-world-2"
* Looking at pipeline "pipeline-with-mingle-config"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "3"
* Click compare link

* Select "Changes" tab
* Verify displays revision "hg-2-0" having comment "hello world" under "Mercurial" named "pipeline-hg" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "hg-2-1" having comment "world hello" under "Mercurial" named "pipeline-hg" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "git-2-0" having comment "said hello to git" under "Git" named "pipeline-git" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "${runtime_name:mingle-config-parent}/2/defaultStage/1" having label "hello-world-2" under pipeline named "${runtime_name:mingle-config-parent}"
* Diff with nth previous pipeline with n being "2"

* Select "Changes" tab
* Verify displays revision "hg-1-0" having comment "Comment user" under "Mercurial" named "pipeline-hg" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "hg-1-1" having comment "Comment loser" under "Mercurial" named "pipeline-hg" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "hg-1-2" having comment "Comment loser-user" under "Mercurial" named "pipeline-hg" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "git-1-0" having comment "foo added to git" under "Git" named "pipeline-git" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "git-1-1" having comment "bar added to git" under "Git" named "pipeline-git" for pipeline "pipeline-with-mingle-config"
* Verify displays revision "${runtime_name:mingle-config-parent}/2/defaultStage/1" having label "hello-world-2" under pipeline named "${runtime_name:mingle-config-parent}"





Teardown of contexts
* Capture go state "ModificationsBetweenPipelines" - teardown
* With "1" live agents in directory "card_activity" - teardown
* Using pipeline "mingle-config-parent, pipeline-with-mingle-config" - teardown
* Basic configuration - teardown


