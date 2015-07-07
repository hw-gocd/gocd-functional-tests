BackupGoServer
==============

Setup of contexts 
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Delete backup history - setup
* Capture go state "BackupGoServer" - setup

BackupGoServer
--------------

tags: 5570, administration, backup, 5818, stage1, h2db_only

* Open "Backup" tab

* Verify the location of the backup store is at "serverBackups"
* Verify the last performed backup message contains "Go has not performed a backup yet."
* Perform backup

* Proceed with backup

* Verify the message "Backup completed successfully."
* Verify the last performed backup message contains "Last backup was taken by 'admin' on"

* Verify the "serverBackups" directory exists
* Verify the "serverBackups" directory contains "db.zip" file in the tree
* Verify the "serverBackups" directory contains "config-repo.zip" file in the tree
* Verify the "serverBackups" directory contains "config-dir.zip" file in the tree
* Verify the "serverBackups" directory contains "version.txt" file in the tree
* Verify the "serverBackups" directory contains file named "version.txt" which has running go version





Teardown of contexts 
* Capture go state "BackupGoServer" - teardown
* Delete backup history - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


