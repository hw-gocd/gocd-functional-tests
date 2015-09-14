NewUserCannotCreatePipelineWithInvalidParametersUsingREST
=========================================================

Setup of contexts
* Capture go state "NewUserCannotCreatePipelineWithInvalidParametersUsingREST" - setup

NewUserCannotCreatePipelineWithInvalidParametersUsingREST
---------------------------------------------------------

tags: configuration, restful api, configuration changes auto-detect, manual

* CreatePipelineWithInvalidParameters 
     |Pipeline name |Material Url       |Builder|Return code?|
     |--------------|-------------------|-------|------------|
     |bad%20pipeline|http://material/url|       |400         |
     |pipeline      |                   |       |400         |
     |pipeline      |http://material/url|exec   |400         |






Teardown of contexts
* Capture go state "NewUserCannotCreatePipelineWithInvalidParametersUsingREST" - teardown


