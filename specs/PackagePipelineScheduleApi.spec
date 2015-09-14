PackagePipelineScheduleApi
==========================

Setup of contexts
* Package configuration - setup
* Setup http based yum repo - setup
* Using pipeline "pipeline_with_yum_repo_package_api" - setup
* With "1" live agents in directory "pipeline_with_yum_repo_package_api" - setup
* Capture go state "pipeline_with_yum_repo_package_api" - setup

PackagePipelineScheduleApi
--------------------------

tags: 7805, plugins-tests

* For pipeline "pipeline_with_yum_repo_package_api" - Using pipeline api
* Schedule should return code "202"

* Looking at pipeline "pipeline_with_yum_repo_package_api"
* Wait for labels "1" to pass

* Publish new artifact

* For pipeline "pipeline_with_yum_repo_package_api" - Using pipeline api
* Using "go-agent-13.1.1-16715.noarch" revision of "tw-repo:go-agent"
* Schedule should return code "202"

* Looking at pipeline "pipeline_with_yum_repo_package_api"
* Wait for labels "2" to pass

* For pipeline "pipeline_with_yum_repo_package_api" - Using pipeline api
* Using "go-agent-13.1.1-16715.noarch" revision of "tw-repo:go-agent1"
* Schedule should fail with "404" and message "material with fingerprint [tw-repo:go-agent1] not found in pipeline [pipeline_with_yum_repo_package_api"




Teardown of contexts
* Capture go state "pipeline_with_yum_repo_package_api" - teardown
* With "1" live agents in directory "pipeline_with_yum_repo_package_api" - teardown
* Using pipeline "pipeline_with_yum_repo_package_api" - teardown
* Setup http based yum repo - teardown
* Package configuration - teardown


