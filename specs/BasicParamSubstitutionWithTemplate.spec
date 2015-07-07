BasicParamSubstitutionWithTemplate
==================================

|Param0|Param1|Param2|
|template-params-pipeline-trunk|Start to execute task: &lt;exec command=\"echo\" args=\"trunk-dir\" /&gt;.|Tasks:Exec ( Command=echo, Args=trunk-dir|
|template-params-pipeline-branch|Start to execute task: &lt;exec command=\"echo\" args=\"branch-dir\" /&gt;.|Tasks:Exec ( Command=echo, Args=branch-dir|
Setup of contexts 
* Basic configuration - setup
* Using pipeline "template-params-pipeline-trunk, template-params-pipeline-branch" - setup
* With "1" live agents in directory "Params" - setup
* Capture go state "BasicParamSubstitutionWithTemplate" - setup

BasicParamSubstitutionWithTemplate
----------------------------------

tags: 4207, params, template


* Trigger pipelines "Param0" and wait for labels "1" to pass
* Navigate to stage "defaultStage" of run "1" having counter "1"

* Navigate to job "defaultJob"

* Open console tab
* Verify console contains "Param1"








Teardown of contexts 
* Capture go state "BasicParamSubstitutionWithTemplate" - teardown
* With "1" live agents in directory "Params" - teardown
* Using pipeline "template-params-pipeline-trunk, template-params-pipeline-branch" - teardown
* Basic configuration - teardown


