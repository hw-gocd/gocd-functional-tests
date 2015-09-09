CommunityEditionFeatures
========================

Setup of contexts
* Community configuration - setup
* Using pipeline "pipeline1" - setup
* Logout on exit - setup
* Capture go state "CommunityEditionFeatures" - setup

CommunityEditionFeatures
------------------------

tags: community, 6316, 6321

* Add security with password file and users "admin" as admin

* Login as "admin"

* Open "Pipelines" tab

* Add new group

* Enter pipeline group name "group_1" - Already On New Pipeline Group Popup
* Save for success - Already On New Pipeline Group Popup

* Click to create a new pipeline to group "group_1"

* Set "pipeline_group[pipeline][name](text_field): some_pipeline_name"
* Go next from settings
* Select material type as "Git"
* Set "pipeline_group[pipeline][materials][GitMaterial][url](text_field): http://git.url"
* Set "pipeline_group[pipeline][materials][GitMaterial][branch](text_field): some_branch"
* Go next from materials
* Set "pipeline_group[pipeline][stage][name](text_field): some_stage"
* Set "pipeline_group[pipeline][stage][jobs][][name](text_field): some_job"
* Select task type as "Ant"
* Save pipeline "some_pipeline_name" successfully

* Verify created successfully

* Open "Pipelines" tab

* Verify "group_1" has pipelines "some_pipeline_name"
* Click to edit pipeline group "group_1"

* Enter user "0" as "view" with permissions "admin"
* Click save - Already On Pipeline Group Edit Page
* Verify that the message "Saved successfully." shows up


* Logout and login as "view"


* Looking at pipeline "some_pipeline_name"
* Verify cannot trigger pipeline
* Logout


* Login as "admin"

* Open "Templates" tab

* Add new template

* Enter template name "template_1"
* Save

* Click add new environment link

* Enter name "environment_1"
* Finish "env-name"


* Verify message "Added environment 'environment_1'" is present






Teardown of contexts
* Capture go state "CommunityEditionFeatures" - teardown
* Logout on exit - teardown
* Using pipeline "pipeline1" - teardown
* Community configuration - teardown


