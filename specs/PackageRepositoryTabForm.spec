PackageRepositoryTabForm
========================

Setup of contexts 
* Setup http based yum repo - setup
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1" - setup
* Capture go state "PackageRepositoryTabForm" - setup

PackageRepositoryTabForm
------------------------

tags: 4171, clicky ui, admin-page, configuration, plugins-tests, 7488, 7487, 7351

* Logout and login as "group1Admin"

* Open "Package Repositories" tab

* Click save - Already on Package Repositories tab
* Verify message shows up "Save failed, see errors below"
* Verify error message "Please provide name" shows up against field repository name
* Verify error message "Please select package repository plugin" shows up against field plugin selection
* Enter repository name as "repo-1"
* Select "yum" plugin
* Click save - Already on Package Repositories tab
* Verify message shows up "Save failed, see errors below"
* Verify error message "This field is required,Repository url is empty" shows up against field repository url
* Enter repo url as "http://localhost:8081/yumrepo"
* Verify check connection gives message containing "401"
* Click save - Already on Package Repositories tab
* Verify repository listing contains "repo-1"


* Open "Package Repositories" tab

* Verify add new repository form is shown
* Click on "repo-1" in repository listing
* Verify repo details are filled with name "repo-1" plugin "yum" and non secure configuration "http://localhost:8081/yumrepo"
* Enter username as "user1"
* Enter password as "password"
* Verify check connection gives message containing "401"
* Click reset - Already on Package Repositories tab
* Enter username as "user"
* Enter password as "password123"
* Verify check connection gives message containing "401"
* Click reset - Already on Package Repositories tab
* Enter username as "user"
* Enter password as "password"
* Verify check connection gives message containing "Connection OK"
* Click save - Already on Package Repositories tab
* Verify repo details are filled with name "repo-1" plugin "yum" and non secure configuration "http://localhost:8081/yumrepo,user"
* Verify password is encrypted value


* Open "Package Repositories" tab

* Click on "repo-1" in repository listing
* Verify repo details are filled with name "repo-1" plugin "yum" and non secure configuration "http://localhost:8081/yumrepo"
* Enter username as "user1"
* Enter password as "password"
* Click save - Already on Package Repositories tab

* Open "Pipelines" tab

* Edit pipeline "pipeline1"

* Open material listing page

* Open new package material creation popup

* Select repository "repo-1"
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Enter package name "go-server" and spec "go-server"
* Verify check package gives message containing "HTTP/1.1 401 Unauthorized"

* Open "Package Repositories" tab

* Enter repository name as "Repo-1"
* Click save - Already on Package Repositories tab
* Verify error message "You have defined multiple repositories called 'Repo-1'. Repository names are case-insensitive and must be unique." shows up against field repository name
* Enter repository name as "file-repo"
* Select "yum" plugin
* Enter repo url as "file:///testurl"
* Enter username as "user"
* Click save - Already on Package Repositories tab
* Verify message shows up "Save failed, see errors below"
* Verify error message "File protocol does not support username and/or password." shows up against field repository url
* Enter password as "password"
* Click save - Already on Package Repositories tab
* Verify message shows up "Save failed, see errors below"
* Verify error message "File protocol does not support username and/or password." shows up against field repository url

* Logout - On Any Page




Teardown of contexts 
* Capture go state "PackageRepositoryTabForm" - teardown
* Using pipeline "pipeline1" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown
* Setup http based yum repo - teardown


