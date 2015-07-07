PackageRepositoryConfigMergeFlow
================================

Setup of contexts 
* Setup http based yum repo - setup
* Package configuration - setup
* Capture go state "PackageRepositoryConfigMergeFlow" - setup

PackageRepositoryConfigMergeFlow
--------------------------------

tags: clicky ui, admin-page, configuration, plugins-tests, #7767, config-merge

Successful Merge
* Open "Package Repositories" tab

* Click on "tw-repo" in repository listing
* Enter username as "user_1"

* Update value of key "USERNAME" to "user_2" for repo with id "repo-id-2"

* Click save - Already on Package Repositories tab
* Verify message shows up "The configuration was modified by someone else, but your changes were merged successfully."

Merge Conflict

* Click on "tw-repo" in repository listing
* Enter username as "user_3"

* Update value of key "USERNAME" to "user_2" for repo with id "repo-id"

* Click save - Already on Package Repositories tab
* Verify message shows up "Save failed. Configuration file has been modified by someone else.RELOADThis will refresh the page and you will lose your changes on this page."
* Click save - Already on Package Repositories tab
* Verify message shows up "Save failed. Configuration file has been modified by someone else.RELOADThis will refresh the page and you will lose your changes on this page."





Teardown of contexts 
* Capture go state "PackageRepositoryConfigMergeFlow" - teardown
* Package configuration - teardown
* Setup http based yum repo - teardown


