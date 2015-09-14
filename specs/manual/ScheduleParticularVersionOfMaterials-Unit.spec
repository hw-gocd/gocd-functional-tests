ScheduleParticularVersionOfMaterials-Unit
=========================================

Setup of contexts
* Capture go state "ScheduleParticularVersionOfMaterials-Unit" - setup

ScheduleParticularVersionOfMaterials-Unit
-----------------------------------------

tags: 3086, materials, restful api, unit, New Item, 3293, 3453, manual

* Trigger a pipeline with some old specific revision
* Wait for the pipeline to finish
* Trigger a fresh instance of this pipeline in a normal way without specifing any specific revision
* verify that materials page which shows what changes since last pipeline instance doesnt compare to pipeline triggered with specific revision




We need more scenarios for using all version control systems




Teardown of contexts
* Capture go state "ScheduleParticularVersionOfMaterials-Unit" - teardown


