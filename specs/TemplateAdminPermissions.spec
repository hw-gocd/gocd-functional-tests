TemplateAdminPermissions
========================

Setup of contexts
* Template admin configuration - setup
* Login as "admin" - setup
* Using pipeline "pipeline1,pipeline2,pipeline3,pipeline-without-template" - setup
* Capture go state "TemplatesAdminPermissions" - setup

TemplateAdminPermissions
------------------------

tags: Clicky Admin, 7876

* Open "Templates" tab

* Verify that templates "simple-pass" are present
* Verify that template "simple-pass" is used by pipelines "pipeline1,pipeline2,pipeline3"
* Verify that "simple-pass" template has permissions link enabled and click on it

* Enter user "0" as "some-user"
* Click reset - Already On Permissions Page For Template
* Verify that user "some-user" does not show up in user permissions
* Enter user "0" as "group1Admin"
* Click save - Already On Permissions Page For Template
* Verify that the message "Saved successfully." shows up - Already On Permissions Page For Template
* Verify that user "group1Admin" shows up in user permissions

* Logout and login as "group1Admin"

* Open "Templates" tab

* Verify that template "simple-pass" is present with disabled permissions link
* Verify that template "template-admin-pipeline" is present with disabled permissions link

* Logout and login as "admin"

* Open "Templates" tab

* Verify that templates "simple-pass" are present
* Verify that "simple-pass" template has permissions link enabled and click on it

* Delete user "group1Admin" - Already On Permissions Page For Template
* Click save - Already On Permissions Page For Template

* Logout and login as "group1Admin"

* Open "Templates" tab

* Verify that templates "simple-pass" are not present
* Verify that template "template-admin-pipeline" is present with disabled permissions link






Teardown of contexts
* Capture go state "TemplatesAdminPermissions" - teardown
* Using pipeline "pipeline1,pipeline2,pipeline3,pipeline-without-template" - teardown
* Login as "admin" - teardown
* Template admin configuration - teardown


