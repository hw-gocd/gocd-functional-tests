UsePriorVersionOfConfig
=======================

UsePriorVersionOfConfig
-----------------------

tags: manual

1. Install a 2.1 version of go-server
Create a few pipelines and execute them
Now install 2.2 version of go-server and verify if the server is started proprely and also the current state of cruise-config.xml has been versioned.
Verify if the logs (/etc/go/go-server.log) is showing appropriate messages

2. Install a 2.1 version of go-server
Modify the cruise-config.xml through file system so that it becomes invalid
Now install 2.2 version of go-server
Verify if the server is not starting up
Verify if the logs are also showing the appropriate messages
Now fix the issues with cruise-config.xml file manually
Restart the server
Verify if the server is starting up
Now modify the cruise-config.xml  through file system so that it becomes invalid
Verify the if changes to filesystem has not triggered any versioning in git. Verify if the logs are showing messages related to replacement of cruise-config.xml file.
Verify if the changed cruise-config.xml has been replaced by last known valid cruise-config.xml
Now modify the cruise-config.xml through files system as well as UI (config.xml screen and clicky admin) so that changes are considered valid.
Verify if the changes to cruise-config.xml has triggered a versioning internally with in the git folder and also logs are updated with appropriate messages. Verify if the logs are showing messages related to versioning.

3.
Install a 2.2 version of go-server say EA1 build
Create pipelines and run them
Stop the server
Make the cruise-config.xml as invalid
Now install latest version of go-server
verify  if the invalid cruise-config.xml is being replaced by last known valid cruise-config.xml during installation.
Verify if the log message shows appropriate messages too.



