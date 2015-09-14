StageWithFetchMaterialsAttribute
================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "fetch-materials" - setup
* With "3" live agents in directory "FetchMaterial" - setup
* Capture go state "StageWithFetchMaterialsAttribute" - setup

StageWithFetchMaterialsAttribute
--------------------------------

tags: 4199

* Add resource "first" to agent "2"
* Add resource "second" to agent "3"
* Add resource "third" to agent "4"

* Looking at pipeline "fetch-materials"
* Trigger pipeline
* Verify stage "3" is "Passed" on pipeline with label "1"

* Navigate to stage "first" of run "1"
* Navigate to job "defaultJob"
* Open console tab
* Verify console contains "Start updating" and not "Skipping material update since stage is configured not to fetch materials"

* Navigate to stage "second" of run "1"
* Navigate to job "defaultJob"
* Open console tab
* Verify console contains "Skipping material update since stage is configured not to fetch materials" and not "Start updating"

* Navigate to stage "third" of run "1"
* Navigate to job "defaultJob"
* Open console tab
* Verify console contains "Start updating" and not "Skipping material update since stage is configured not to fetch materials"

* For pipeline "fetch-materials"
* Verify stage "first" has attribute "fetchMaterials" set to "true" where null means "true"
* Verify stage "second" has attribute "fetchMaterials" set to "false" where null means "true"
* Verify stage "third" has attribute "fetchMaterials" set to "true" where null means "true"




Teardown of contexts
* Capture go state "StageWithFetchMaterialsAttribute" - teardown
* With "3" live agents in directory "FetchMaterial" - teardown
* Using pipeline "fetch-materials" - teardown
* Basic configuration - teardown


