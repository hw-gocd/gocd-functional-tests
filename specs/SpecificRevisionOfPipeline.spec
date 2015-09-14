SpecificRevisionOfPipeline
==========================

Setup of contexts
* Basic configuration - setup
* Using pipeline "basic-pipeline-fast, manual-downstream-pipeline" - setup
* With "2" live agents in directory "specific_revision_deployment" - setup
* Capture go state "SpecificRevisionOfPipeline" - setup

SpecificRevisionOfPipeline
--------------------------

tags: 3388, restful api, 3407, automate, 3453

* Adding pipeline "manual-downstream-pipeline" to "uat" environment
* Assigning "1" agents to environment "uat"

This sets up 2 pipeline instances of each pipeline
* Trigger pipeline "basic-pipeline-fast"
* Wait for first stage to pass with pipeline label "1"

* Looking at "uat" environment
* Looking at pipeline "manual-downstream-pipeline" - On Environment Page
* Verify nothing is currently deployed
* Deploy latest

* Looking at pipeline "manual-downstream-pipeline"
* Wait for first stage to pass with pipeline label "1"

* Looking at "uat" environment
* Looking at pipeline "manual-downstream-pipeline" - On Environment Page
* Verify the pipeline has label "1"


Operate page assertions are moved to a manual scenario as operate page has been removed as a part of #3494, which does deploy latest button for pipelines in environment
REFER -> SpecificRevisionOfPipelineWithOperateScreenCheck.scn





Teardown of contexts
* Capture go state "SpecificRevisionOfPipeline" - teardown
* With "2" live agents in directory "specific_revision_deployment" - teardown
* Using pipeline "basic-pipeline-fast, manual-downstream-pipeline" - teardown
* Basic configuration - teardown


