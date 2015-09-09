ComparePipelinesWithDifferentTrackingTool
=========================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-with-tracking-tool,down-pipeline-with-tracking-tool" - setup
* With "1" live agents in directory "compare_pipelines" - setup
* Capture go state "ComparePipelinesWithDifferentTrackingTool" - setup

ComparePipelinesWithDifferentTrackingTool
-----------------------------------------

tags: 4643, automate, compare_pipeline, dependency_walk, 4687

* With material "hg-for-down-pipeline-with-tracking-tool" for pipeline "down-pipeline-with-tracking-tool"
* Checkin file "hg-new-file" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-new"
* With material "git-for-pipeline-with-tracking-tool" for pipeline "pipeline-with-tracking-tool"
* Checkin file "git-new-file" as user "go <go@thoughtworks.com>" with message "Added git-new-file"
* Remember current version as "git-new"

* Trigger pipelines "pipeline-with-tracking-tool" and wait for labels "1" to pass
* Trigger pipelines "down-pipeline-with-tracking-tool" and wait for labels "1" to pass

* Looking at pipeline "down-pipeline-with-tracking-tool"
* Click compare link

* Verify that there are "2" materials
* Verify displays revision "${runtime_name:pipeline-with-tracking-tool}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:pipeline-with-tracking-tool}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline-with-tracking-tool" for pipeline "down-pipeline-with-tracking-tool"
* Verify "Git" material with name is not displayed

* Changing "trackingtool" attribute "link" to "http://foo.bar/${ID}" for pipeline "down-pipeline-with-tracking-tool"

* Looking at pipeline "down-pipeline-with-tracking-tool"
* Click compare link

* Verify that there are "3" materials
* Verify displays revision "${runtime_name:pipeline-with-tracking-tool}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:pipeline-with-tracking-tool}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline-with-tracking-tool" for pipeline "down-pipeline-with-tracking-tool"
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-pipeline-with-tracking-tool" for pipeline "pipeline-with-tracking-tool"





Teardown of contexts
* Capture go state "ComparePipelinesWithDifferentTrackingTool" - teardown
* With "1" live agents in directory "compare_pipelines" - teardown
* Using pipeline "pipeline-with-tracking-tool,down-pipeline-with-tracking-tool" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


