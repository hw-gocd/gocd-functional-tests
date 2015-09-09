EditAnExistingEnvironment
=========================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "environment-pipeline, environment-pipeline-locked, environment-failing-pipeline,pipeline-with-environment-variables" - setup
* Capture go state "EditAnExistingEnvironment" - setup

EditAnExistingEnvironment
-------------------------

tags: #4189, clicky ui, environment

Positive scenario

* Click edit environment link for "uat"

* Click on edit pipelines
* Verify title of modal box is "Pipelines"
* UnSelect pipelines "environment-pipeline,environment-pipeline-locked"
* Click on save
* Verify message "Updated environment 'uat'" is present
* Verify values "${runtime_name:environment-failing-pipeline},${runtime_name:pipeline-with-environment-variables}" are shown in section "added_pipelines"

* Click on edit agents
* Verify title of modal box is "Agents"
* Select agent "missing-agent"
* Click on save
* Verify message "Updated environment 'uat'" is present
* Verify values "missing-agent (10.232.3.1)" are shown in section "added_agents"

* Click on edit environment variables
* Verify title of modal box is "Environment Variables"
* For variable "0" name "another" value "abc"
* Add new variable
* For variable "4" name "correct_name" value "value"
* Click on save
* Verify message "Updated environment 'uat'" is present
* Verify values "another = abc,correct_name = value" are shown in section "added_environment_variables"






Teardown of contexts
* Capture go state "EditAnExistingEnvironment" - teardown
* Using pipeline "environment-pipeline, environment-pipeline-locked, environment-failing-pipeline,pipeline-with-environment-variables" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


