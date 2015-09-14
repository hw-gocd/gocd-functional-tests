CleanUpArtifacts-Manual
=======================

Setup of contexts
* Basic configuration - setup

CleanUpArtifacts-Manual
-----------------------

tags: 1920, Clicky Admin, administration, manual

Scenario : Migration related scenario

Given
There is already a go/cruise version installed.

When
User upgrades to latest version of go

Then
After sucessful migration, existing artifacts attribute of server tag should have been removed and replaced with artifacts tag with in the server tag.
Opening the server configuration page should show previously configured artifacts location (Is it a part of story scope???)
He should also see a check box for auto-deleting of the documents and an adjacent textbox field with an input value of zero





Teardown of contexts
* Basic configuration - teardown


