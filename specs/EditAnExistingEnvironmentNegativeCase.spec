EditAnExistingEnvironmentNegativeCase
=====================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "environment-pipeline, environment-pipeline-locked, environment-failing-pipeline,pipeline-with-environment-variables" - setup
* Capture go state "EditAnExistingEnvironmentNegativeCase" - setup

EditAnExistingEnvironmentNegativeCase
-------------------------------------

tags: #4189, clicky ui, environment

Negatve scenario 1

* Click edit environment link for "uat"

* For environment named "uat"
* Change environment name to "new_uat"

* Click on edit pipelines
* Verify error message "Environment named 'uat' not found." is present
* Close popup
* Click on edit agents
* Verify error message "Environment named 'uat' not found." is present
* Close popup
* Click on edit environment variables
* Verify error message "Environment named 'uat' not found." is present
* Close popup

Negative Scenario 2

Pipelines section
* Click edit environment link for "new_uat"

* Click on edit pipelines
* UnSelect pipelines "environment-pipeline,environment-pipeline-locked"

* For environment named "new_uat"
* Change environment name to "uat"

* Click on save
* Verify error message "Environment named 'new_uat' not found." is present
* Close popup

Agents Section
* Click edit environment link for "uat"

* Click on edit agents
* Select agent "missing-agent"

* For environment named "uat"
* Change environment name to "new_uat"

* Click on save
* Verify error message "Environment named 'uat' not found." is present
* Close popup

Environment Variables Section
* Click edit environment link for "new_uat"

* Click on edit environment variables

* For variable "0" name "another" value "abc"

* For environment named "new_uat"
* Change environment name to "uat"

* Click on save
* Verify error message "Environment named 'new_uat' not found." is present
* Close popup





Teardown of contexts
* Capture go state "EditAnExistingEnvironmentNegativeCase" - teardown
* Using pipeline "environment-pipeline, environment-pipeline-locked, environment-failing-pipeline,pipeline-with-environment-variables" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


