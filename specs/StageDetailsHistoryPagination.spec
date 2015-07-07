StageDetailsHistoryPagination
=============================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "pipeline-ls" - setup
* Capture go state "StageDetailsHistoryPagination" - setup

StageDetailsHistoryPagination
-----------------------------

tags: 3609, stage-details, automate

* Trigger and cancel pipeline "pipeline-ls" "21" times
* Navigate to stage "defaultStage" of run "21" having counter "1"

* Turn off auto refresh
* Verify stage history has "21, 20, 19, 18, 17, 16, 15, 14, 13, 12"
* Verify shows history page "2"
* Click on history page "2"
* Verify stage history has "11, 10, 9, 8, 7, 6, 5, 4, 3, 2"
* Verify shows history page "3"
* Click on history page "3"
* Verify stage history has "1"




Teardown of contexts 
* Capture go state "StageDetailsHistoryPagination" - teardown
* Using pipeline "pipeline-ls" - teardown
* Basic configuration - teardown


