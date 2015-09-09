ComparePipelinesWithDifferentMingleConfigurations
=================================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline-with-mingle-config,down-pipeline-with-mingle-config" - setup
* With "1" live agents in directory "compare_pipelines" - setup
* Capture go state "ComparePipelinesWithDifferentMingleConfigurations" - setup

ComparePipelinesWithDifferentMingleConfigurations
-------------------------------------------------

tags: 4643, automate, compare_pipeline, dependency_walk, 4687

* With material "hg-for-down-pipeline-with-mingle-config" for pipeline "down-pipeline-with-mingle-config"
* Checkin file "hg-new-file" as user "go" with message "Added hg-new-file"
* Remember current version as "hg-new"
* With material "git-for-pipeline-with-mingle-config" for pipeline "pipeline-with-mingle-config"
* Checkin file "git-new-file" as user "go <go@thoughtworks.com>" with message "Added git-new-file"
* Remember current version as "git-new"

* Trigger pipelines "pipeline-with-mingle-config" and wait for labels "1" to pass
* Trigger pipelines "down-pipeline-with-mingle-config" and wait for labels "1" to pass

* Looking at pipeline "down-pipeline-with-mingle-config"
* Click compare link

* Verify that there are "3" materials
* Verify displays revision "${runtime_name:pipeline-with-mingle-config}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:pipeline-with-mingle-config}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline-with-mingle-config" for pipeline "down-pipeline-with-mingle-config"
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-pipeline-with-mingle-config" for pipeline "pipeline-with-mingle-config"

* Changing "mingle" attribute "baseUrl" to "https://mingle.example.com" for pipeline "down-pipeline-with-mingle-config"

* Looking at pipeline "down-pipeline-with-mingle-config"
* Click compare link

* Verify that there are "3" materials
* Verify displays revision "${runtime_name:pipeline-with-mingle-config}/1/defaultStage/1" having label "1" under pipeline named "${runtime_name:pipeline-with-mingle-config}"
* Verify displays revision "hg-new" having comment "Added hg-new-file" under "Mercurial" named "hg-for-down-pipeline-with-mingle-config" for pipeline "down-pipeline-with-mingle-config"
* Verify displays revision "git-new" having comment "Added git-new-file" under "Git" named "git-for-pipeline-with-mingle-config" for pipeline "pipeline-with-mingle-config"





Teardown of contexts
* Capture go state "ComparePipelinesWithDifferentMingleConfigurations" - teardown
* With "1" live agents in directory "compare_pipelines" - teardown
* Using pipeline "pipeline-with-mingle-config,down-pipeline-with-mingle-config" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


