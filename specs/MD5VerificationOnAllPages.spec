MD5VerificationOnAllPages
=========================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Capture go state "MD5VerificationOnAllPages" - setup

MD5VerificationOnAllPages
-------------------------

tags: 7321

* Capture current md5

* Open "Pipelines" tab

* Assert mD5
* Click clone button for pipeline "basic-pipeline"

* Assert mD5 - Already On Clone Pipeline Popup
* Close popup - Already On Clone Pipeline Popup

* Open "Pipelines" tab

* Delete group with confirm prompt "empty-group"
* Assert mD5

* Open "Pipelines" tab

* Click to edit pipeline group "basic"

* Assert mD5 - Already On Pipeline Group Edit Page

* Open "Pipelines" tab

* Click on pipeline "pipeline-with-multiple-materials-stages-jobs" for editing

* Assert mD5 - Already on general options page
* Go to project management page

* Assert mD5 - Already on Project Management Page
* Go to materials page

* Assert mD5 - Already on material listing page
* Open stage listing page - Already on material listing page

* Assert mD5 - Already On Stages Page
* Go to environment variables page - Already On Stages Page

* Assert mD5 - Already on environment variables page
* Open parameters page - Already on environment variables page

* Assert mD5 - Already on parameters page
* Open general options page

* Open stage listing page

* Open stage "stageOne"

* Assert mD5 - Already on edit stage page
* Go to environment variables page - Already on edit stage page

* Assert mD5 - Already on environment variables page
* Navigate to tab "Permissions"
* Assert mD5 - Already on environment variables page
* Open jobs - Already On Environment Variables Page

* Assert mD5 - Already on Job listing Page
* Open job "job1"

* Open job settings
* Assert mD5 - Already on Job edit page
* Open tasks

* Assert mD5 - Already on Task listing page
* Open artifacts - Already on Task listing page

* Assert mD5 - Already On Artifacts Listing Page
* Go to environment variables page - Already On Artifacts Listing Page

* Assert mD5 - Already on environment variables page
* Open custom tabs - Already on environment variables page

* Assert mD5 - Already on Job Custom Tabs Page

* Open "Pipelines" tab

* Extract template for pipeline "basic-pipeline"

* Assert mD5 - Already on extract template popup
* Close popup - Already on extract template popup

* Open "Templates" tab

* Add new template

* Assert mD5 - Already on create new template popup
* Close popup - Already on create new template popup

* Open "Templates" tab

* Delete template with confirm prompt "template.with.params.one"
* Assert mD5 - Already On Templates Listing tab

* Open "Templates" tab

* Verify that templates "simple-pass" are present
* Verify that "simple-pass" template has permissions link enabled and click on it

* Assert mD5 - Already On Permissions Page For Template

* Open "Config XML" tab

* Click edit
* Assert mD5 - Already on Source Xml Tab

* Click edit environment link for "uat"

* Click on edit pipelines

* Assert mD5 - Already on Add Environment Page
* Close popup - Already on Add Environment Page

* Click on edit agents

* Assert mD5 - Already on Add Environment Page
* Close popup - Already on Add Environment Page

* Click on edit environment variables

* Assert mD5 - Already on Add Environment Page
* Close popup - Already on Add Environment Page

* Open "Package Repositories" tab

* Assert mD5 - Already on package repositories tab




Teardown of contexts
* Capture go state "MD5VerificationOnAllPages" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


