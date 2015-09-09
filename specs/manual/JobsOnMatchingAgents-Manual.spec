JobsOnMatchingAgents-Manual
===========================

Setup of contexts
* Capture go state "JobsOnMatchingAgents-Manual" - setup

JobsOnMatchingAgents-Manual
---------------------------

tags: 3102, job template, manual, 3307

* verify a stage that contains jobs and job run-ons run both these
* verify that the configuration file does not convert job run-ons into jobs to show in the config file


* verify when a job is run on all agents it picks agents which has resources in the configuration
* verify when a job is run on all agents it picks only agents from the same environmentin which the pipeline exist containing the job with run-on
* verify that if there are 5 matching agents there are 5 jobs created with different integers in job name and is run on that agent only




Teardown of contexts
* Capture go state "JobsOnMatchingAgents-Manual" - teardown


