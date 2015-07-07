PauseNewPipelineAfterCreation
=============================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "PauseNewPipelineAfterCreation" - setup

PauseNewPipelineAfterCreation
-----------------------------

tags: 4812, Clicky Admin, Admin

* Force navigate to add new pipeline

* Enter pipeline name "newpipeline" - Already on new pipeline wizard
* Set "pipeline_group[group](text_field): group1"
* Go next from settings
* Select material type as "Git"
* Set "pipeline_group[pipeline][materials][GitMaterial][url](text_field): http://git.url"
* Set "pipeline_group[pipeline][materials][GitMaterial][branch](text_field): some_branch"
* Go next from materials
* Set "pipeline_group[pipeline][stage][name](text_field): defaultStage"
* Set "pipeline_group[pipeline][stage][jobs][][name](text_field): defaultJob"
* Select task type as "Ant"
* Set "pipeline_group[pipeline][stage][jobs][][tasks][ant][buildFile](text_field): build.xml"
* Set "pipeline_group[pipeline][stage][jobs][][tasks][ant][target](text_field): compile"
* Set "pipeline_group[pipeline][stage][jobs][][tasks][ant][workingDirectory](text_field): src"
* Save pipeline "newpipeline" successfully

* Verify "Pipeline successfully created." message is displayed
* Verify pipeline "newpipeline" is paused with message "Paused by anonymous"
* Open material listing page

* Verify pipeline "newpipeline" is paused with message "Paused by anonymous"
* Open stage listing page - Already on material listing page

* Verify pipeline "newpipeline" is paused with message "Paused by anonymous"
* Open stage "defaultStage"

* Verify pipeline "newpipeline" is paused with message "Paused by anonymous"
* Open jobs

* Open job "defaultJob"

* Verify pipeline "newpipeline" is paused with message "Paused by anonymous"
* Open tasks

* Verify pipeline "newpipeline" is paused with message "Paused by anonymous"
* Unpause pipeline "newpipeline"

* Looking at pipeline "newpipeline"
* Verify pipeline is unpaused




Teardown of contexts 
* Capture go state "PauseNewPipelineAfterCreation" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


