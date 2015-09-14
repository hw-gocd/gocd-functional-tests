MaterialUpdateHungStatusMessage
===============================

Setup of contexts
* Basic configuration - setup
* Using "edit-pipeline" pipeline - setup
* Capture go state "MaterialUpdateHungStatusMessage" - setup

MaterialUpdateHungStatusMessage
-------------------------------

tags: 6667, manual

Start the server with setting -Dmaterial.update.idle.timeout=60000 to see the warning message within 1 min.
The default is 15 mins.


* click on pipeline "edit-pipeline" for editing

* Open material listing page

* open new git material Creation popup

* enter material name "bad_git_material"
* enter url "https://blrstdscm01.thoughtworks.com/git/go_performance"
* make autoupdate to be "false"
* enter destination directory "git_dir"
* click save

* looking at pipeline "edit-pipeline"
* trigger pipeline
* sleep for "90" seconds
* open error and warning messages popup

* verify warning "description" contains "Material update is currently running but has not shown any activity in the last 1 minute(s). This may be hung."





Teardown of contexts
* Capture go state "MaterialUpdateHungStatusMessage" - teardown
* Using "edit-pipeline" pipeline - teardown
* Basic configuration - teardown


