YumRepoPackageAsMaterialMDUErrors
=================================

Setup of contexts
* Setup http based yum repo - setup
* Package configuration - setup
* Using pipeline "pipeline_with_yum_repo_package_as_material" - setup
* With "1" live agents in directory "YumRepoPackageAsMaterialMDUErrors" - setup
* Capture go state "YumRepoPackageAsMaterialMDUErrors" - setup

YumRepoPackageAsMaterialMDUErrors
---------------------------------

tags: #7411, #7571, Yum repo package, plugins-tests

* Looking at pipeline "pipeline_with_yum_repo_package_as_material"
* Verify stage "1" is "Passed" on pipeline with label "1"

* Update value of key "USERNAME" to "userDoesNotExist" for repo with id "repo-id" - Configure Cruise By

* Open error and warning messages popup

* Verify error message "Modification check failed for material: Repository: [repo_url=http://localhost:8081/${runtime_package_http_repo_name:http_repo1}] - Package: [package_spec=go-agent]" and description "Interaction with plugin with id 'yum' implementing 'package-repository' extension failed while requesting for 'latest-revision-since'. Reason: [Unsuccessful response from plugin. Plugin returned with code '500' and the following response: 'HTTP/1.1 401 Unauthorized']"

* Update value of key "USERNAME" to "user" for repo with id "repo-id" - Configure Cruise By

* Verify there are no error messages




Teardown of contexts
* Capture go state "YumRepoPackageAsMaterialMDUErrors" - teardown
* With "1" live agents in directory "YumRepoPackageAsMaterialMDUErrors" - teardown
* Using pipeline "pipeline_with_yum_repo_package_as_material" - teardown
* Package configuration - teardown
* Setup http based yum repo - teardown


