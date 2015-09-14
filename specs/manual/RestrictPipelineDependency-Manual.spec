RestrictPipelineDependency-Manual
=================================

Setup of contexts
* Capture go state "RestrictPipelineDependency-Manual" - setup

RestrictPipelineDependency-Manual
---------------------------------

tags: 3289, pipeline, dependencies, manual

* verify that user gets an error message if config file has the following scenario


<materials>
  <pipeline pipelineName = "upstreamLibrary" stage="stage3"/>
  <pipeline pipelineName = "upstreamLibrary" stage="stage4"/>
</materials>





Teardown of contexts
* Capture go state "RestrictPipelineDependency-Manual" - teardown


