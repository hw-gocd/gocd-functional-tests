ComparePipelinesWithDifferentPermissions
========================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "first-pipeline,down-pipeline" - setup
* With "1" live agents in directory "compare_pipelines" - setup
* Capture go state "ComparePipelinesWithDifferentPermissions" - setup

ComparePipelinesWithDifferentPermissions
----------------------------------------

tags: 4643, automate, compare_pipeline, dependency_walk, 4687, 6786

* With material "hg-for-down-pipeline" for pipeline "down-pipeline"
* Checkin file "hg-new-file" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-new"
* With material "git-for-first-pipeline" for pipeline "first-pipeline"
* Checkin file "git-new-file" as user "go <go@thoughtworks.com>" with message "Added git-new-file"
* Remember current version as "git-new"

* Trigger pipelines "first-pipeline" and wait for labels "1" to pass
* Trigger pipelines "down-pipeline" and wait for labels "1" to pass


* Looking at pipeline "down-pipeline"
* Click compare link

* Verify that there are "3" materials
* Verify displays revision "${runtime_name:first-pipeline}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:first-pipeline}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline" for pipeline "down-pipeline"
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-first-pipeline" for pipeline "first-pipeline"
* Click on upstream pipeline revision "${runtime_name:first-pipeline}/1/defaultStage/1"

* Verify that "${runtime_name:first-pipeline}/1/defaultStage/1" stage is displayed
* Click compare link - Already on stage Detail Page

* Verify that there are "1" materials
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-first-pipeline" for pipeline "first-pipeline"


* Logout and login as "raghu"

* Verify pipeline "first-pipeline" is not visible
* Looking at pipeline "down-pipeline"
* Click compare link

* Verify that there are "2" materials
* Verify displays revision "${runtime_name:first-pipeline}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:first-pipeline}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline" for pipeline "down-pipeline"
* Verify "Git" material with name is not displayed
* Click on upstream pipeline revision "${runtime_name:first-pipeline}/1/defaultStage/1"
* Verify that unauthorized access message is shown

* Logout and login as "pavan"

* Verify pipeline "first-pipeline" is visible
* Looking at pipeline "down-pipeline"
* Click compare link

* Verify that there are "3" materials
* Verify displays revision "${runtime_name:first-pipeline}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:first-pipeline}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline" for pipeline "down-pipeline"
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-first-pipeline" for pipeline "first-pipeline"
* Click on upstream pipeline revision "${runtime_name:first-pipeline}/1/defaultStage/1"

* Verify that "${runtime_name:first-pipeline}/1/defaultStage/1" stage is displayed
* Click compare link - Already on stage Detail Page

* Verify that there are "1" materials
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-first-pipeline" for pipeline "first-pipeline"

* Logout and login as "operatorUser"

* Verify pipeline "first-pipeline" is not visible
* Looking at pipeline "down-pipeline"
* Click compare link

* Verify that there are "2" materials
* Verify displays revision "${runtime_name:first-pipeline}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:first-pipeline}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline" for pipeline "down-pipeline"
* Verify "Git" material with name is not displayed
* Click on upstream pipeline revision "${runtime_name:first-pipeline}/1/defaultStage/1"
* Verify that unauthorized access message is shown

* Logout and login as "group1view"

* Verify pipeline "first-pipeline" is visible
* Looking at pipeline "down-pipeline"
* Click compare link

* Verify that there are "3" materials
* Verify displays revision "${runtime_name:first-pipeline}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:first-pipeline}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline" for pipeline "down-pipeline"
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-first-pipeline" for pipeline "first-pipeline"
* Click on upstream pipeline revision "${runtime_name:first-pipeline}/1/defaultStage/1"

* Verify that "${runtime_name:first-pipeline}/1/defaultStage/1" stage is displayed
* Click compare link - Already on stage Detail Page

* Verify that there are "1" materials
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-first-pipeline" for pipeline "first-pipeline"





Teardown of contexts
* Capture go state "ComparePipelinesWithDifferentPermissions" - teardown
* With "1" live agents in directory "compare_pipelines" - teardown
* Using pipeline "first-pipeline,down-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


