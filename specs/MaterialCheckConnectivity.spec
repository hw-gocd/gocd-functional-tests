MaterialCheckConnectivity
=========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "MaterialCheckConnectivity" - setup

MaterialCheckConnectivity
-------------------------

tags: 5018, Clicky admin

* Click on pipeline "edit-pipeline" for editing

* Open material listing page

* Edit material "hg-material"

* Check connectivity should be successful - Already on Mercurial Material Creation Popup
* Close - Already on Mercurial Material Creation Popup

* Remember url for material "hg-material" of pipeline "edit-pipeline"
* Add parameter "url" to pipeline "edit-pipeline"

* Click on pipeline "edit-pipeline" for editing

* Open material listing page

* Edit material "hg-material"

* Enter url "#{url}" - Already on Mercurial Material Creation Popup
* Check connectivity should be successful - Already on Mercurial Material Creation Popup
* Enter url "foo" - Already on Mercurial Material Creation Popup
* Check connectivity should fail






Teardown of contexts 
* Capture go state "MaterialCheckConnectivity" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


