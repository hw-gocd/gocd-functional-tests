PackageRepositoryTestsTabVerification
=====================================

Setup of contexts 
* Package configuration - setup
* Using pipeline "K3,K4" - setup
* Setup file system based yum repos "repo3" - setup
* With "1" live agents in directory "PackageRepositoryTestsTabVerification" - setup
* Capture go state "PackageRepositoryTestsTabVerification" - setup

PackageRepositoryTestsTabVerification
-------------------------------------

tags: #7451, #7806, plugins-tests

-----Happy Path ------
* Trigger pipelines "K3" and wait for labels "1" to pass
* Looking at pipeline "K3"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Go to tests tab

* Verify message "The stage passed" shows up - Already on Stage Detail Tests Tab
* Verify test runs "5" failures "0" errors "0"

-----Negative path ------

* Looking at pipeline "K4"
* Trigger pipeline
* Looking at pipeline "K4"
* Wait for labels "1" to fail
* Looking at pipeline "K4"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Go to tests tab

* Verify message "New Tests Broken Since: " shows up - Already on Stage Detail Tests Tab
* Verify test runs "1" failures "1" errors "0"




Teardown of contexts 
* Capture go state "PackageRepositoryTestsTabVerification" - teardown
* With "1" live agents in directory "PackageRepositoryTestsTabVerification" - teardown
* Setup file system based yum repos "repo3" - teardown
* Using pipeline "K3,K4" - teardown
* Package configuration - teardown


