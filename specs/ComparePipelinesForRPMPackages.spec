ComparePipelinesForRPMPackages
==============================

Setup of contexts 
* Package configuration - setup
* Using pipeline "C1,C2" - setup
* Setup file system based yum repos "repo3" - setup
* With "2" live agents in directory "ComparePipelinesForRPMPackages" - setup
* Capture go state "ComparePipelinesForRPMPackages" - setup

ComparePipelinesForRPMPackages
------------------------------

tags: #7469, Yum repo package, plugins-tests

* Trigger pipelines "C1" and wait for labels "1" to pass
* Trigger pipelines "C2" and wait for labels "1" to pass
* Looking at pipeline "C2"
* Click compare link

* Search for "go-server" on "from" textbox
* Click on label "1" in the dropdown
* Verify that "from" textbox is populated with "1"
* Search for "go-agent" on "to" textbox
* Click on label "1" in the dropdown
* Verify that "to" textbox is populated with "1"
* Verify displays package with uri "file://${runtime_package_repo_uri:repo3}" having spec "go-server" with revision "go-server-12.4.0-1234.noarch" published by "Thoughtworks Studios <;twstudios@thoughtworks.com>"
* Verify displays package with uri "file://${runtime_package_repo_uri:repo3}" having spec "go-agent" with revision "go-agent-13.1.0-112.noarch" published by "anonymous"

* Publish artifacts "go-server-13.1.0-122.noarch.rpm" to "repo3"

* Trigger pipelines "C2" and wait for labels "2" to pass

* Publish artifacts "go-agent-13.1.0-113.noarch.rpm" to "repo3"

* Trigger pipelines "C2" and wait for labels "3" to pass
* Looking at pipeline "C2"
* Pause pipeline with reason "pausing to C2 before checkins"

* Trigger pipelines "C1" and wait for labels "2" to pass

* With material named "hg-c2" in pipeline "C2"
* Checkin file "foo.txt" as user "user" with message "Comment user"
* Remember current version as "FIRST_REVISION"

* Publish artifacts "go-server-13.1.0-123.noarch.rpm,go-server-13.1.1-16714.noarch.rpm" to "repo3"

* Looking at pipeline "C2"
* Unpause pipeline
* Trigger pipelines "C2" and wait for labels "4" to pass
* Click compare link

* Search for "go-server" on "from" textbox
* Click on label "2" in the dropdown
* Verify that "from" textbox is populated with "2"
* Search for "go-agent" on "to" textbox
* Click on label "3" in the dropdown
* Verify that "to" textbox is populated with "3"
* Verify displays package with uri "file://${runtime_package_repo_uri:repo3}" having spec "go-agent" with revision "go-agent-13.1.0-113.noarch" published by "anonymous"

* Looking at pipeline "C2"
* Click compare link

* Search for "go-server" on "from" textbox
* Click on label "1" in the dropdown
* Verify that "from" textbox is populated with "1"
* Search for "go-agent" on "to" textbox
* Click on label "4" in the dropdown
* Verify that "to" textbox is populated with "4"
* Verify displays revision "${runtime_name:C1}/2/defaultStage/1" having label "2" under pipeline named "${runtime_name:C1}"
* Verify displays revision "FIRST_REVISION" having comment "Comment user" under "Mercurial" named "hg-c2" for pipeline "C2"
* Verify displays package with uri "file://${runtime_package_repo_uri:repo3}" having spec "go-agent" with revision "go-agent-13.1.0-113.noarch" published by "anonymous"
* Verify displays package with uri "file://${runtime_package_repo_uri:repo3}" having spec "go-server" with revision "go-server-13.1.1-16714.noarch" published by "anonymous"
* Verify displays package with uri "file://${runtime_package_repo_uri:repo3}" having spec "go-server" with revision "go-server-13.1.0-122.noarch" published by "anonymous"




Teardown of contexts 
* Capture go state "ComparePipelinesForRPMPackages" - teardown
* With "2" live agents in directory "ComparePipelinesForRPMPackages" - teardown
* Setup file system based yum repos "repo3" - teardown
* Using pipeline "C1,C2" - teardown
* Package configuration - teardown


