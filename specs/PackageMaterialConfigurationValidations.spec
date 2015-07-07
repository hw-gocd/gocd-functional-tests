PackageMaterialConfigurationValidations
=======================================

Setup of contexts 
* Setup http based yum repo - setup
* Package configuration - setup
* Using pipeline "pipeline_with_yum_repo_package_as_material" - setup
* Capture go state "PackageMaterialConfigurationValidations" - setup

PackageMaterialConfigurationValidations
---------------------------------------

tags: #7272, Yum repo package, plugins-tests, 7317, 7488

* Click on pipeline "pipeline_with_yum_repo_package_as_material" for editing

* Open material listing page

* Verify that package with name "tw-repo:go-agent" is added with url "Repository: [repo_url=http://localhost:8081/yumrepo] - Package: [package_spec=go-agent]"
* Open new package material creation popup

* Select repository "tw-repo"
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Enter package name "go-agent" and spec "go-agent"
* Verify check package gives message containing "Found package 'go-agent"
* Enter package name "go-agent" and spec "go*"
* Verify check package gives message containing "Found package 'go-agent"
* Enter package name "go-agent" and spec "[go]*"
* Verify check package gives message containing "Found package 'go-agent"
* Enter package name "go-agent" and spec "go-[a-z]*"
* Verify check package gives message containing "Found package 'go-agent"
* Enter package name "go-agent" and spec "???*"
* Verify check package gives message containing "Found package 'go-agent"
* Enter package name "go-agent" and spec "go-agent-13.?.1-*.noarch"
* Verify check package gives message containing "Found package 'go-agent"

* Select repository "tw-repo"
* Select option "chooseExisting" - AlreadyOnPackageMaterialCreationPopup
* Select package "go-agent"
* Verify check package gives message containing "Found package 'go-agent"
* Click save - AlreadyOnPackageMaterialCreationPopup
* Verify error message "Duplicate package material detected!" is shown - Already On package Material Creation Popup
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Click save - AlreadyOnPackageMaterialCreationPopup
* Verify global errors has error "Package name is mandatory"
* Verify global errors has error "Package spec is empty"
* Select option "chooseExisting" - AlreadyOnPackageMaterialCreationPopup
* Select repository "repo-with-missing-plugin"
* Select package "package-with-missing-plugin"
* Verify missing plugin error is shown
* Verify that save is "disabled"
* Select repository "tw-repo"
* Verify that save is "enabled"
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Verify check package gives message containing "Package check Failed. Reason(s): Package spec is empty"
* Enter package name "go-agent1" and spec "non-existent-package-spec"
* Verify check package gives message containing "Package check Failed. Reason(s): Could not find any package that matched 'non-existent-package-spec'."
* Select option "addNew" - AlreadyOnPackageMaterialCreationPopup
* Enter package name "go-agent" and spec "go-agent"
* Click save - AlreadyOnPackageMaterialCreationPopup
* Verify global errors has error "You have defined multiple packages called 'go-agent'. Package names are case-insensitive and must be unique within a repository."
* Enter package name "GO-AGENT" and spec "go-agent"
* Click save - AlreadyOnPackageMaterialCreationPopup
* Verify global errors has error "Cannot save package or repo, found duplicate packages. [Repo Name: 'tw-repo', Package Name: 'go-agent'], [Repo Name: 'tw-repo', Package Name: 'GO-AGENT']"
* Verify global errors has error "You have defined multiple packages called 'GO-AGENT'. Package names are case-insensitive and must be unique within a repository."


* Click on pipeline "pipeline_with_yum_repo_package_as_material" for editing


label template validations with material name

* LabelTemplateValidations
| field value | valid | 
| ${COUNT}#{tw-repo:go-agent} | false | 
| ${COUNT}-${tw-repo:go-agent} | true | 





Teardown of contexts 
* Capture go state "PackageMaterialConfigurationValidations" - teardown
* Using pipeline "pipeline_with_yum_repo_package_as_material" - teardown
* Package configuration - teardown
* Setup http based yum repo - teardown


