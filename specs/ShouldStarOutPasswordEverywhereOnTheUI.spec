ShouldStarOutPasswordEverywhereOnTheUI
======================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "remote-pipeline" - setup
* With "1" live agents in directory "material_urls_display_test" - setup
* Capture go state "NewShouldShowPasswordAsStarInMaterialTabAndConsoleOutputAndPopup" - setup

ShouldStarOutPasswordEverywhereOnTheUI
--------------------------------------

tags: 2626, diagnostics messages, svn support, dashboard, authentication, passwordfile support, configuration, automate

* Looking at pipeline "remote-pipeline"
* Trigger pipeline
* Verify stage "1" is "Passed" on pipeline with label "1"
* Click on pipeline name

TODO - Add a test to make sure the Pipeline Dashboard build cause popup and the Stage Details Materials tab has password starred out

* Verify build cause message on row "2" contains "http://username:******@localhost:8008" and not "password"

* Looking at pipeline "remote-pipeline"
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "from http://username:******@localhost:8008" and not "password"
* Verify material tab contains "http://username:******@localhost:8008" and not "password"





Teardown of contexts 
* Capture go state "NewShouldShowPasswordAsStarInMaterialTabAndConsoleOutputAndPopup" - teardown
* With "1" live agents in directory "material_urls_display_test" - teardown
* Using pipeline "remote-pipeline" - teardown
* Basic configuration - teardown


