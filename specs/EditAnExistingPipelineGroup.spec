EditAnExistingPipelineGroup
===========================

Setup of contexts 
* Group admin security configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1,pipeline5" - setup
* Capture go state "EditPipelineGroups" - setup

EditAnExistingPipelineGroup
---------------------------

tags: 4369, Clicky Admin, pipeline group

* Open "Pipelines" tab

* Verify groups "group1,group4" are visible
* Click to edit pipeline group "group4"

* Enter "group5" as group name
* Click save - Already On Pipeline Group Edit Page
* Verify that the message "Saved successfully." shows up

* Open "Pipelines" tab

* Verify groups "group1,group5" are visible
* Click to edit pipeline group "group5"

* Enter user "0" as "pavan" with permissions "admin"
* Click save - Already On Pipeline Group Edit Page
* Verify that the message "Saved successfully." shows up
* Enter role "0" as "role-that-does-not-exist" with permissions "view"
* Click save - Already On Pipeline Group Edit Page
* Verify shows error "Role \"role-that-does-not-exist\" does not exist!" on role "0"


* Logout and login as "pavan"


* Open "Pipelines" tab

* Verify groups "group5" are visible
* Click to edit pipeline group "group5"

* Enter user "1" as "admin" with permissions "operate"
* Enter user "2" as "Rajeshvaran" with permissions "view, operate"
* Enter user "3" as "shilpa" with permissions "admin"
* Enter role "0" as "viewer" with permissions "view"
* Enter role "1" as "operator" with permissions "operate"
* Enter role "2" as "admins" with permissions "admin"
* Click save - Already On Pipeline Group Edit Page
* Verify that the message "Saved successfully." shows up

* Verify pipeline group "group5" has "user" "shilpa" with "admins" permissions
* Verify pipeline group "group5" has "role" "admins" with "admins" permissions
* Verify pipeline group "group5" has "user" "admin" with "operate" permissions
* Verify pipeline group "group5" has "user" "Rajeshvaran" with "view,operate" permissions
* Verify pipeline group "group5" has "role" "operator" with "operate" permissions
* Verify pipeline group "group5" has "role" "viewer" with "view" permissions

* Open "Pipelines" tab

* Click to edit pipeline group "group5"

* Delete user "shilpa"
* Delete role "viewer"
* Click save - Already On Pipeline Group Edit Page
* Verify that the message "Saved successfully." shows up

* Verify pipeline group "group5" does not have "user" "shilpa" with "admins" permissions
* Verify pipeline group "group5" does not have "role" "viewer" with "view" permissions














Teardown of contexts 
* Capture go state "EditPipelineGroups" - teardown
* Using pipeline "pipeline1,pipeline5" - teardown
* Login as "admin" - teardown
* Group admin security configuration - teardown


