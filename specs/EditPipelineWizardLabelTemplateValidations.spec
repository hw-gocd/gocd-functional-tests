EditPipelineWizardLabelTemplateValidations
==========================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "EditPipelineWizardLabelTemplateValidations" - setup

EditPipelineWizardLabelTemplateValidations
------------------------------------------

tags: Clicky Admin

* Click on pipeline "edit-pipeline" for editing


Label Template Validations

* LabelTemplateValidations 
     |field value     |valid|
     |----------------|-----|
     |#               |false|
     |${COUNT}        |true |
     |##app${COUNT}   |true |
     |#{param}        |false|
     |${svn_material} |false|
     |${COUNT}${COUNT}|true |


* Click on pipeline "edit-pipeline" for editing

* Open parameters page

* Enter parameter "1" name "label_prefix" and value "cruise"
* Click save
* Verify "Saved successfully." message is displayed - Already on parameters page
* Open general options page

Label Template Validations

* LabelTemplateValidations 
     |field value                   |valid|
     |------------------------------|-----|
     |#{label_prefix}               |false|
     |#{label_prefix}${COUNT}       |true |
     |###{label_prefix} app ${COUNT}|false|

* Click on pipeline "edit-pipeline" for editing

* Go to materials page

* Open new subversion material creation popup

* Enter material name "svn_material"
* Enter url "svn.thoughtworks.com"
* Enter destination directory "svn"
* Click save - Already on Subversion Material Add Popup


* Verify that material saved successfully
* Open general options page - Already on material listing page

label template validations with material name

* LabelTemplateValidations 
     |field value                                                                          |valid|
     |-------------------------------------------------------------------------------------|-----|
     |${svn_material}                                                                      |true |
     |${svn_material}${COUNT}                                                              |true |
     |${svn_material}${COUNT}#{label_prefix}-revision-run##                                |true |
     |${COUNT}#{label_prefix}${svn_material} ##                                            |false|
     |${COUNT}--this_is_longest_check_boundary_value_validation_need_to_check_if_this_works|true |






Teardown of contexts
* Capture go state "EditPipelineWizardLabelTemplateValidations" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


