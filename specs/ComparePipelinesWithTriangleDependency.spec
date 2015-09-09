ComparePipelinesWithTriangleDependency
======================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "fourth, fifth, another-sixth-manual" - setup
* With "1" live agents in directory "compare_pipelines" - setup
* Capture go state "ComparePipelinesWithTriangleDependency" - setup

ComparePipelinesWithTriangleDependency
--------------------------------------

tags: 4643, automate, compare_pipeline, dependency_walk

* With material "hg-first" for pipeline "fourth"
* Checkin file "hg-new-file" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-new"

* Trigger pipelines "fourth" and wait for labels "1" to pass
* Trigger pipelines "fourth" and wait for labels "2" to pass
* Trigger pipelines "fifth" and wait for labels "1" to pass
* Trigger pipelines "another-sixth-manual" and wait for labels "1" to pass
* Click compare link

* Verify displays revision "${runtime_name:fourth}/2/defaultStage/1" having label "2" under pipeline named "${runtime_name:fourth}"
* Verify displays revision "${runtime_name:fifth}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:fifth}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-first" for pipeline "fourth"




Teardown of contexts
* Capture go state "ComparePipelinesWithTriangleDependency" - teardown
* With "1" live agents in directory "compare_pipelines" - teardown
* Using pipeline "fourth, fifth, another-sixth-manual" - teardown
* Basic configuration - teardown


