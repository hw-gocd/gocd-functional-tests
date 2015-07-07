PerforceMaterialViewerAndEditor
===============================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "PerforceMaterialViewerAndEditor" - setup

PerforceMaterialViewerAndEditor
-------------------------------

tags: Clicky Admin, 4598

* Click on pipeline "edit-pipeline" for editing

* Open material listing page

* Open new perforce material creation popup

* Enter material name "p4_material" - Already On Perforce Material Creation Popup
* Enter server and port "p4:1643"
* Make autoupdate to be "false" - Already On Perforce Material Creation Popup
* Enter username "user" - Already On Perforce Material Creation Popup
* Enter password "abc" - Already On Perforce Material Creation Popup
* Enter view details "perforce_view_details"
* Set use tickets flag "true"
* Enter destination directory "p4_dir" - Already On Perforce Material Creation Popup
* Enter black list details "*.htm"
* Click save - Already On Perforce Material Creation Popup

* Verify that material saved successfully
* Verify that "p4" with name "p4_material" is added with attributes "materialName>p4_material,port>p4:1643,username>user,encryptedPassword>/yPnfnXXsrc=,useTickets>true,dest>p4_dir,autoUpdate>false"
* Edit material "p4_material"

* Verify material name is "p4_material" - Already On Perforce Material Creation Popup
* Verify server and port is "p4:1643"
* Verify autoupdate is "false" - Already On Perforce Material Creation Popup
* Verify username is "user"
* Verify "password" field is "disabled" and contains "**********"
* Verify view details is "perforce_view_details"
* Verify use tickets is "true"
* Verify destination directory is "p4_dir" - Already On Perforce Material Creation Popup
* Verify black list details is "*.htm"
* Enter server and port "p5:2000"
* Click save - Already On Perforce Material Creation Popup

* Verify that material saved successfully
* Verify that "p4" with name "p4_material" is added with attributes "materialName>p4_material,port>p5:2000"





Teardown of contexts 
* Capture go state "PerforceMaterialViewerAndEditor" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


