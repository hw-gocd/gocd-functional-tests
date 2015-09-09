AddNewEnvironmentValidationsAndShow
===================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline, basic-pipeline-slow, pipeline-with-failing-stage" - setup
* Capture go state "AddNewEnvironmentValidationsAndShow" - setup

AddNewEnvironmentValidationsAndShow
-----------------------------------

tags: environment, 3300, 4348, clicky ui, 3423, stage1

* Click add new environment link

Add environment with only name

* Verify "FINISH" button in "env-name" is disabled
* Verify "Next" button in "env-name" is disabled

* Enter name "first.env.name"
* Finish "env-name"

* For environment "first.env.name"
* Verify breadcrumbs has environment name
* Verify no "added_pipelines" are shown
* Verify no "added_agents" are shown
* Verify no "added_environment_variables" are shown

* Looking at "first.env.name" environment
* Verify environment has "There are no pipelines configured for this environment." in it
* Click add new environment link

Add environment with pipelines, agents and environment variables

* Enter name "first.env.name"
* Finish "env-name"
* Verify error "Failed to add environment. Environment 'first.env.name' already exists." message shows up
* Enter name "First.ENV.namE"
* Finish "env-name"
* Verify error "Failed to add environment. Environment 'First.ENV.namE' already exists." message shows up
* Enter name "first environment"
* Finish "env-name"
* Verify error "Failed to add environment." message shows up
* Enter name "foo_!_bar"

* Select tab "env-pipelines"
* Verify pipelines "basic-pipeline, basic-pipeline-slow, pipeline-with-failing-stage" are present
* Select pipelines "basic-pipeline, basic-pipeline-slow"

* Select tab "env-agents"
* Select agent "missing-agent"
* Select tab "env-vars"

* Add new variable
* For variable "0" name "name" value "value"
* Add new variable
* For variable "1" name "name" value "other-value"
* Finish
* Verify error "Failed to add environment. Environment Variable name 'name' is not unique for environment 'foo_!_bar'." message shows up
* Select tab "env-vars"
* Delete variable "1"
* Add new variable
* For variable "1" name "name with space" value "other-value"
* Finish

* Verify error "Failed to add environment." message shows up
* Verify name is "foo_!_bar"
* Select tab "env-pipelines"
* Verify pipelines "basic-pipeline,basic-pipeline-slow" are selected
* Select tab "env-agents"
* Verify agent "missing-agent" is selected
* Select tab "env-vars"

* Verify variable "0" has name "name" and value "value"
* Verify variable "1" has name "name with space" and value "other-value"

* Select tab "env-name"
* Enter name "second"
* Finish "env-name"

* For environment "second"
* Verify breadcrumbs has environment name
* Verify values "${runtime_name:basic-pipeline},${runtime_name:basic-pipeline-slow}" are shown in section "added_pipelines"
* Verify values "missing-agent (10.232.3.1)" are shown in section "added_agents"
* Verify values "name = value,name with space = other-value" are shown in section "added_environment_variables"

* Verify agent "1" has environments "second"

* Open "Config XML" tab

* Config xml should have an environment "second" with environment variable "name" "value"
* Config xml should have an environment "second" with environment variable "name with space" "other-value"

* Click add new environment link

* Enter name "ignore"
* Select tab "env-pipelines"
* Verify pipelines "pipeline-with-failing-stage" is visible
* Verify pipelines "basic-pipeline,basic-pipeline-slow" are hidden
* Click to see unavailable pipelines
* Verify pipelines "basic-pipeline,basic-pipeline-slow" belongs to environment "second"


Verify non-admin cannot add environments

* Logout and login as "view"

* Verify add new environment link is not visible






Teardown of contexts
* Capture go state "AddNewEnvironmentValidationsAndShow" - teardown
* Using pipeline "basic-pipeline, basic-pipeline-slow, pipeline-with-failing-stage" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


