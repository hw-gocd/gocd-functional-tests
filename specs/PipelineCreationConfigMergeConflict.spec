PipelineCreationConfigMergeConflict
===================================

Setup of contexts
* Secure configuration - setup
* Login as "Admin" - setup
* Capture go state "PipelineCreationConfigMergeConflict" - setup

PipelineCreationConfigMergeConflict
-----------------------------------

tags: 7280

* Force navigate to add new pipeline

* Set "pipeline_group[pipeline][name](text_field): P1"
* Set "pipeline_group[group](text_field): PG1"
* Go next from settings
* Select material type as "Git"
* Set "pipeline_group[pipeline][materials][GitMaterial][url](text_field): http://git.url"
* Set "pipeline_group[pipeline][materials][GitMaterial][branch](text_field): some_branch"
* Go next from materials
* Set "pipeline_group[pipeline][stage][name](text_field): some_stage"
* Set "pipeline_group[pipeline][stage][jobs][][name](text_field): some_job"
* Select task type as "More..."
* Set "pipeline_group[pipeline][stage][jobs][][tasks][exec][command](text_field): ls"
* Save pipeline "P1" successfully


* Force navigate to add new pipeline

* Remember current tab
* Set "pipeline_group[pipeline][name](text_field): P3"
* Set "pipeline_group[group](text_field): PG1"
* Go next from settings
* Select material type as "Git"
* Set "pipeline_group[pipeline][materials][GitMaterial][url](text_field): http://git.url"
* Set "pipeline_group[pipeline][materials][GitMaterial][branch](text_field): some_branch"
* Go next from materials
* Set "pipeline_group[pipeline][stage][name](text_field): some_stage"
* Set "pipeline_group[pipeline][stage][jobs][][name](text_field): some_job"
* Select task type as "More..."
* Set "pipeline_group[pipeline][stage][jobs][][tasks][exec][command](text_field): ls"

* For pipeline group "PG1"
* Create pipeline "P2" using template "simple-pass"

* Remember md5 - Already on new pipeline wizard
* Save pipeline
* Verify validation message "Save failed. Configuration file has been modified by someone else."
* Verify md5 is same - Already on new pipeline wizard
* Set "pipeline_group[pipeline][stage][jobs][][tasks][exec][command](text_field): ls"
* Save pipeline
* Verify validation message "Save failed. Configuration file has been modified by someone else."

* For pipeline group "PG1"
* Delete pipeline "P2" - Configure cruise using api

* Force navigate to add new pipeline

* Set "pipeline_group[pipeline][name](text_field): P3"
* Set "pipeline_group[group](text_field): PG1"
* Go next from settings
* Select material type as "Git"
* Set "pipeline_group[pipeline][materials][GitMaterial][url](text_field): http://git.url"
* Set "pipeline_group[pipeline][materials][GitMaterial][branch](text_field): some_branch"
* Go next from materials
* Remember current tab
* Remember md5 - Already on new pipeline wizard
* Set "pipeline_group[pipeline][stage][name](text_field): some_stage"
* Set "pipeline_group[pipeline][stage][jobs][][name](text_field): some_job"
* Select task type as "More..."
* Save pipeline
* Verify inline validation message " This field is required."
* Verify md5 is same - Already on new pipeline wizard
* Set "pipeline_group[pipeline][stage][jobs][][tasks][exec][command](text_field): ls"

* Create pipeline "P2" as first pipeline in group "PG1"

* Save pipeline
* Verify validation message "Pipeline successfully created. The configuration was modified by someone else, but your changes were merged successfully."

















Teardown of contexts
* Capture go state "PipelineCreationConfigMergeConflict" - teardown
* Login as "Admin" - teardown
* Secure configuration - teardown


