RejectArtifactUploadWhenOutOfSpace-Manual
=========================================

RejectArtifactUploadWhenOutOfSpace-Manual
-----------------------------------------

tags: 5131, reject artifact, manual

Automated only for linux
There are multiple agents. One of the agents is trying to upload a file to server. Server has enough space to upload
File size is well within the size of upload
File should  be uploaded. Successfull upload message should be shown.

Automated onlu for linux
There are multiple agents. One of the agents is trying to upload a file to server. Server has not enough space to upload
File size is larger than available disk space
File should not be uploaded. Associated artifact task should fail. The job console should have a message stating ""

Given:
There are multiple agents. Many agents are trying to upload the files simultaneously. Sever has enough disk space for all them
When:
Multiple agents are trying to upload the file
Then:
Full Files should be uploaded untill there is enough disk space.
If we can't upload a full file, then we should roll back partly uploaded files.
Also send back a failure message.



