EditPipelineWizardReorderStages
===============================

Setup of contexts
* Basic configuration - setup
* Using pipeline "edit-pipeline-with-3-stages" - setup
* Capture go state "EditPipelineWizardReorderStages" - setup

EditPipelineWizardReorderStages
-------------------------------

tags: Clicky Admin, 4742

* Click on pipeline "edit-pipeline-with-3-stages" for editing

* Open stage listing page

* Verify the stages are "defaultStage,second,third"
* Verify cannot move "defaultStage" up
* Verify cannot move "third" down
* Move "second" up
* Verify the stages are "second,defaultStage,third"
* Move "defaultStage" down
* Verify the stages are "second,third,defaultStage"




Teardown of contexts
* Capture go state "EditPipelineWizardReorderStages" - teardown
* Using pipeline "edit-pipeline-with-3-stages" - teardown
* Basic configuration - teardown


