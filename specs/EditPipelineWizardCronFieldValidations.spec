EditPipelineWizardCronFieldValidations
======================================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "EditPipelineWizardCronFieldValidations" - setup

EditPipelineWizardCronFieldValidations
--------------------------------------

tags: 4737, Clicky Admin

* Click on pipeline "edit-pipeline" for editing


Cron Field Validations

* CronFieldValidation
| Cron Field Value | valid | 
| 0 0/5 * * * ? | true | 
| 10 0/5 * * * ? | true | 
| 0 30 10-13 ? * WED,FRI | true | 
| 0 0/30 8-9 5,20 * ? | true | 
| 0 30 10-13 ? * WED-FRI | true | 
| 0 30 10-13 ? * FRI-MON | true | 
| 0 30 10-13 ? * WED,FRI 2011 | true | 
| some_string | false | 
| @hourly | false | 
| @monthly | false | 
| @weekly | false | 
| @daily | false | 
| @reboot | false | 
| 0 30  1-12 1-28 JAN-JUN ? | true | 


* Open parameters page

* Enter parameter "1" name "cron_time_specifier" and value "0 30 10-13 ? * WED-FRI"
* Enter parameter "2" name "partial_cron_time_specifier" and value "0 30 10-13 ? *"
* Click save
* Verify "Saved successfully." message is displayed - Already on parameters page
* Open general options page


Cron Field Validations with parameter substituion

* CronFieldValidation
| Cron Field Value | valid | 
| #{cron_time_specifier} | true | 
| #{partial_cron_time_specifier} WED-FRI | true | 
| #(cron_time_specifier} #{partial_cron_time_specifier} | false | 
| ${env_cron_time_specifier} | false | 
| ${env_partial_cron_specifier} | false | 


* Go to environment variables page

* Enter environment variable "1" name "env_cron_specifier" and value "0 30 10-13 ? * WED-FRI"
* Enter environment variable "2" name "env_partial_cron_specifier" and value "0 30 10-13 ? * "
* Click save - Already On Environment Variables Page
* Open general options page - Already on environment variables page



Cron time specifier validation with environment variables


* CronFieldValidation
| Cron Field Value | valid | 
| ${env_cron_specifier} | false | 
| ${env_partial_cron_specifier} | false | 







Teardown of contexts 
* Capture go state "EditPipelineWizardCronFieldValidations" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


