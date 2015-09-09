NewEditPipelineGroup
====================

Setup of contexts
* Trainlines configuration - setup
* Trigger "trainlines-connectfour" - setup
* Capture go state "NewEditPipelineGroup" - setup

NewEditPipelineGroup
--------------------

tags: admin-page, #2724, pipeline-group, administration

* login as "user-admin"
* open admin configration wizard page
* edit group "defaultGroup" and change the group name to "changed"
* verify the group name is "changed"




Teardown of contexts
* Capture go state "NewEditPipelineGroup" - teardown
* Trigger "trainlines-connectfour" - teardown
* Trainlines configuration - teardown


