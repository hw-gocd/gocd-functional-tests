SearchInPackageRepositoryTab
============================

Setup of contexts
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1" - setup
* Setup http based yum repo - setup
* Capture go state "SearchInPackageRepositoryTab" - setup

SearchInPackageRepositoryTab
----------------------------

tags: 7752, clicky ui, admin-page, configuration, plugins-tests

* Open "Package Repositories" tab

* Verify that search box is not shown
* Enter repository name as "this-is-a-repository-with-long-name-having-56-characters"
* Select "yum" plugin
* Enter repo url as "http://localhost:8081/${runtime_package_http_repo_name:http_repo1}"
* Enter username as "user"
* Enter password as "password"
* Verify check connection gives message containing "Connection OK"
* Click save - Already on Package Repositories tab
* Verify repo details are filled with name "this-is-a-repository-with-long-name-having-56-characters" plugin "yum" and non secure configuration "http://localhost:8081/${runtime_package_http_repo_name:http_repo1},user"
* Verify password is encrypted value
* Click on add new repository
* Enter repository name as "repo.with.periods"
* Select "yum" plugin
* Enter repo url as "http://localhost:8081/${runtime_package_http_repo_name:http_repo1}"
* Enter username as "user"
* Enter password as "password"
* Verify check connection gives message containing "Connection OK"
* Click save - Already on Package Repositories tab
* Verify repo details are filled with name "repo.with.periods" plugin "yum" and non secure configuration "http://localhost:8081/${runtime_package_http_repo_name:http_repo1},user"
* Verify password is encrypted value
* Click on add new repository
* Enter repository name as "repo_one"
* Select "yum" plugin
* Enter repo url as "http://localhost:8081/${runtime_package_http_repo_name:http_repo1}"
* Enter username as "user"
* Enter password as "password"
* Verify check connection gives message containing "Connection OK"
* Click save - Already on Package Repositories tab
* Verify repo details are filled with name "repo_one" plugin "yum" and non secure configuration "http://localhost:8081/${runtime_package_http_repo_name:http_repo1},user"
* Verify password is encrypted value
* Click on add new repository
* Enter repository name as "repo_two"
* Select "yum" plugin
* Enter repo url as "http://localhost:8081/${runtime_package_http_repo_name:http_repo1}"
* Enter username as "user"
* Enter password as "password"
* Verify check connection gives message containing "Connection OK"
* Click save - Already on Package Repositories tab
* Verify repo details are filled with name "repo_two" plugin "yum" and non secure configuration "http://localhost:8081/${runtime_package_http_repo_name:http_repo1},user"
* Verify password is encrypted value

* Open "Pipelines" tab

* Edit pipeline "pipeline1"

* Open material listing page

* Open new package material creation popup

* Select repository "this-is-a-repository-with-long-name-having-56-characters"
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Enter package name "this-is-a-package-with-long-name-having-53-characters" and spec "go-agent"
* Verify check package gives message containing "Found package 'go-agent"
* Click save - AlreadyOnPackageMaterialCreationPopup

* Open new package material creation popup

* Select repository "repo.with.periods"
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Enter package name "package.with.periods" and spec "package.with.periods"
* Click save - AlreadyOnPackageMaterialCreationPopup

* Open new package material creation popup

* Select repository "repo_one"
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Enter package name "package_one" and spec "package_one"
* Click save - AlreadyOnPackageMaterialCreationPopup

* Open new package material creation popup

* Select repository "repo_two"
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Enter package name "package_two" and spec "package_two"
* Click save - AlreadyOnPackageMaterialCreationPopup

* Open "Package Repositories" tab

* Verify that search box is shown
* Type "this-" in search box and verify repository "this-is-a-repository-with-long-name-having-56-characters" is shown while repository "repo.with.periods" is not
* Type "repo_" in search box and verify repository "repo_one" is shown while repository "repo.with.periods" is not
* Type "repo_" in search box and verify repository "repo_two" is shown while repository "repo.with.periods" is not
* Type "package." in search box and verify repository "repo.with.periods" is shown while repository "repo_one" is not
* Type "package_" in search box and verify repository "repo_one" is shown while repository "this-is-a-repository-with-long-name-having-56-characters" is not
* Type "package_" in search box and verify repository "repo_two" is shown while repository "repo.with.periods" is not








Teardown of contexts
* Capture go state "SearchInPackageRepositoryTab" - teardown
* Setup http based yum repo - teardown
* Using pipeline "pipeline1" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


