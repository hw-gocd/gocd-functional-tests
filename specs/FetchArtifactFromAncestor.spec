FetchArtifactFromAncestor
=========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "uppest_pipeline, upper_pipeline, upper_peer_pipeline, up_pipeline, down_pipeline" - setup
* With "2" live agents in directory "FetchMaterialFromAncestor" - setup
* Capture go state "FetchMaterialFromAncestor" - setup

FetchArtifactFromAncestor
-------------------------

tags: 5783, fetchartifact, ancestor, stage1

* With material named "hg_material" in pipeline "uppest_pipeline"
* Checkin file "first" as user "user" with message "Comment user"
* With material named "hg_material" in pipeline "uppest_pipeline"
* Checkin file "second" as user "user" with message "Comment user"

* Trigger pipelines "uppest_pipeline" and wait for label "1" to pass for stage "3"
* Trigger pipelines "upper_pipeline" and wait for labels "1" to pass
* Trigger pipelines "uppest_pipeline" and wait for labels "2" to pass
* Trigger pipelines "upper_peer_pipeline" and wait for labels "1" to pass
* Trigger pipelines "up_pipeline" and wait for labels "1" to pass
* Trigger pipelines "down_pipeline" and wait for labels "1" to pass
* Navigate to stage "down-stage1" of run "1" having counter "1"

Successful fetch from an ancestor
* Navigate to job "down-job1"

* Open console tab
* Verify console says that artifact "first" was fetched from "${runtime_name:uppest_pipeline}/1/uppest-stage1/latest/uppest-job1" for path "uppest_pipeline/upper_pipeline/up_pipeline"
* Verify console says that artifact "first" was fetched from "${runtime_name:uppest_pipeline}/2/uppest-stage1/1/uppest-job1" for path "uppest_pipeline/upper_peer_pipeline/up_pipeline"

Successful fetch from direct parent

* Looking at pipeline "upper_pipeline"
* Navigate to stage "upper-stage1" of run "1" having counter "1"

* Navigate to job "upper-job1"

* Open console tab
* Verify console says that artifact "first" was fetched from "${runtime_name:uppest_pipeline}/1/uppest-stage1/latest/uppest-job1" for path "uppest_pipeline"




Teardown of contexts 
* Capture go state "FetchMaterialFromAncestor" - teardown
* With "2" live agents in directory "FetchMaterialFromAncestor" - teardown
* Using pipeline "uppest_pipeline, upper_pipeline, upper_peer_pipeline, up_pipeline, down_pipeline" - teardown
* Basic configuration - teardown


