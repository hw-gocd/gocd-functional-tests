ApiBackupGoServer
=================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Delete backup history - setup
* Capture go state "ApiBackupGoServer" - setup

ApiBackupGoServer
-----------------

tags: 5570, administration, backup, 5818, h2db_only

* Take backup as "admin"
* Verify backup is successful

* Login as "admin"

* Open "Backup" tab

* Verify the last performed backup message contains "Last backup was taken by 'admin' on"

* Verify the "serverBackups" directory exists
* Verify the "serverBackups" directory contains "db.zip" file in the tree
* Verify the "serverBackups" directory contains "config-repo.zip" file in the tree
* Verify the "serverBackups" directory contains "config-dir.zip" file in the tree
* Verify the "serverBackups" directory contains "version.txt" file in the tree
* Verify the "serverBackups" directory contains file named "version.txt" which has running go version

* Take backup as "view"
* Verify user is not authorized to take backups





Teardown of contexts
* Capture go state "ApiBackupGoServer" - teardown
* Delete backup history - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


