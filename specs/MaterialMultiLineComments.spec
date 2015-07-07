MaterialMultiLineComments
=========================

Setup of contexts 
* Basic configuration - setup
* Using pipeline "edit-pipeline" - setup
* Capture go state "MaterialMultiLineComments" - setup

MaterialMultiLineComments
-------------------------

tags: 6431, materials

* With material "hg-material" for pipeline "edit-pipeline"
* Checkin file "new_file_1" as user "foo <foo@bar.com>" with message "This is a one line description.\n\nThis should be on a new paragraph"

* Looking at pipeline "edit-pipeline"
* Trigger pipeline
* Verify stage "1" is "Building" on pipeline with label "1"
* Open changes section for counter "1"

* Looking at material of type "hg" named "hg-material" for pipeline "edit-pipeline" with counter "1"
* Verify modification "0" has multi line comment with paragraph content "This is a one line description."
* Verify modification "0" has multi line comment with paragraph content "This should be on a new paragraph"

* Navigate to materials for "edit-pipeline" "1" "defaultStage" "1"

* Looking at material of type "Mercurial" named "hg-material"
* Verify modification "0" has multi line comment with paragraph content "This is a one line description." - Already On Build Cause Section
* Verify modification "0" has multi line comment with paragraph content "This should be on a new paragraph" - Already On Build Cause Section




Teardown of contexts 
* Capture go state "MaterialMultiLineComments" - teardown
* Using pipeline "edit-pipeline" - teardown
* Basic configuration - teardown


