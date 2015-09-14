NewPipelineHistoryPage
======================

Setup of contexts
* Completed svn pipeline - setup
* Capture go state "NewPipelineHistoryPage" - setup

NewPipelineHistoryPage
----------------------

tags: 1256, svn support, dashboard, manual

Can't be automated.

* open pipeline history page
* another user changed configuration for this pipeline
* user should see new pipeline configuration without refresh page
* new pipeline is scheduled
* user should see new stage without refresh page

can be automated

* open Pipeline dashboard
* user navigate to pipeline history
* user can see Id and build cause for certain pipeline
* user navigate to stage history to find detail information

could be automated

* open pipeline history page for pipeline in pipeline group "defaultGroup"
* verify shows pipeline history page for pipeline in pipeline group "defaultGroup"
* verify access pipeline history page in group "secondGroup" got unauthorized error




Teardown of contexts
* Capture go state "NewPipelineHistoryPage" - teardown
* Completed svn pipeline - teardown


