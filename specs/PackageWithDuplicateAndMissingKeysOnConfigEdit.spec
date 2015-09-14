PackageWithDuplicateAndMissingKeysOnConfigEdit
==============================================

Setup of contexts
* Package configuration - setup
* Using pipeline "M8,M9" - setup
* Capture go state "RPMPackageWithMDUErrors" - setup

PackageWithDuplicateAndMissingKeysOnConfigEdit
----------------------------------------------

tags: #7468, Yum repo package, plugins-tests

* Looking at pipeline "M8"
* Verify pipeline has not been triggered even once
* Looking at pipeline "M9"
* Verify pipeline has not been triggered even once

* Open error and warning messages popup

* Verify error message "Modification check failed for material: Repository: [repo_url=file://${runtime_package_repo_uri:repo3}, repo_url_dup=file://${runtime_package_repo_uri:repo3}] - Package: [package_spec=go-server, package_spec_dup=go-server]" and description "Interaction with plugin with id 'yum' implementing 'package-repository' extension failed while requesting for 'latest-revision'. Reason: [Unsuccessful response from plugin. Plugin returned with code '500' and the following response: 'Unsupported key(s) found : REPO_URL_DUP. Allowed key(s) are : REPO_URL, USERNAME, PASSWORD; Unsupported key(s) found : PACKAGE_SPEC_DUP. Allowed key(s) are : PACKAGE_SPEC']"
* Verify error message "Modification check failed for material: Repository: [] - Package: []" and description "Interaction with plugin with id 'yum' implementing 'package-repository' extension failed while requesting for 'latest-revision'. Reason: [Unsuccessful response from plugin. Plugin returned with code '500' and the following response: 'Repository url is empty; Package spec is empty']"

* Open "Config XML" tab

* Click edit
* Remember current tab - Already on Source Xml Tab
* Change repo config to have duplicate keys
* Click save - Already on Source Xml Tab
* Verify error message "Duplicate key 'REPO_URL' found for Repository 'repo-with-dup-and-invalid-keys'" is shown - Already on Source Xml Tab
* Click cancel
* Click edit
* Change package config to have duplicate keys
* Click save - Already on Source Xml Tab
* Verify error message "Duplicate key 'PACKAGE_SPEC' found for Package 'pkg-dup-and-invalid-keys'" is shown - Already on Source Xml Tab






Teardown of contexts
* Capture go state "RPMPackageWithMDUErrors" - teardown
* Using pipeline "M8,M9" - teardown
* Package configuration - teardown


