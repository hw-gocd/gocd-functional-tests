MercurialMaterialViewerAndEditor
================================

Setup of contexts
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "MercurialMaterialViewerAndEditor" - setup

MercurialMaterialViewerAndEditor
--------------------------------

tags: Clicky Admin, 4598

* Click on pipeline "edit-pipeline" for editing

* Open material listing page

* Open new mercurial material creation popup

* Enter material name "hg_material" - Already on Mercurial Material Creation Popup
* Enter url "http://foo.bar" - Already on Mercurial Material Creation Popup
* Make autoupdate to be "false" - Already on Mercurial Material Creation Popup
* Enter destination directory "hg_dir" - Already on Mercurial Material Creation Popup
* Enter black list "*.htm" - Already on Mercurial Material Creation Popup
* Click save - Already on Mercurial Material Creation Popup

* Verify that material saved successfully
* Verify that "hg" with name "hg_material" is added with attributes "materialName>hg_material,url>http://foo.bar,dest>hg_dir,autoUpdate>false"
* Edit material "hg_material"

* Verify material name is "hg_material" - Already on Subversion Material Add Popup
* Verify url is "http://foo.bar" - Already on Subversion Material Add Popup
* Verify destination directory is "hg_dir" - Already on Subversion Material Add Popup
* Verify autoupdate is "false" - Already on Subversion Material Add Popup
* Verify black list is "*.htm" - Already on Subversion Material Add Popup
* Enter url "http://bar.baz"
* Click save - Already on Subversion Material Add Popup

* Verify that material saved successfully
* Verify that "hg" with name "hg_material" is added with attributes "materialName>hg_material,url>http://bar.baz"





Teardown of contexts
* Capture go state "MercurialMaterialViewerAndEditor" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


