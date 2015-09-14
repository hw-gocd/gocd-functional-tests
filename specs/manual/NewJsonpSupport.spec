NewJsonpSupport
===============

Setup of contexts
* Completed svn pipeline - setup
* Capture go state "NewJsonpSupport" - setup

NewJsonpSupport
---------------

tags: svn support, customizable reports, scheduling, manual


to support JSONP, then user can write a Go macro for Mingle

   1. setup a Go Server and switch on its security
   2. make sure that user can get pipeline history data through jsonp.
       e.g.http://admin:badger@<hostname>:8153/go/pipelineHistory.json?pipelineName=<pipelineName>
   3. make sure that only users with view permission can get those pipeline history data via jsonp






Teardown of contexts
* Capture go state "NewJsonpSupport" - teardown
* Completed svn pipeline - teardown


