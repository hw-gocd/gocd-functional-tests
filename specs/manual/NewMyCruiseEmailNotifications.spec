NewMyCruiseEmailNotifications
=============================

Setup of contexts
* Configure enterprise license - setup
* Setup password file and define roles - setup
* Config two pipeline groups - setup
* Capture go state "NewMyCruiseEmailNotifications" - setup

NewMyCruiseEmailNotifications
-----------------------------

tags: #2271, project filtering, passwordfile support, svn support, diagnostics messages, #1458, personal notification, #2708

test case - add a filter

* open Server Configuration page
* input hostname "10.18.3.171"
* input port "25"
* input username "twistuser1"
* input password "cru1s3123"
* select tls "no"
* input from "twistuser1@cruise.com"
* input admin mail "twistuser2@cruise.com"
* click send test mail button
* verify proper message "Test mail was sent successfully. Please check your inbox to confirm that the email was received." shows
* click save button
* verify proper message "Email Notification configuration has been updated successfully." shows

Checkin matchers

* login as "userA"
* open my cruise page
* add checkin matchers "kaihu, ps" with email id "ps@tw.com"
* verify matchers "kaihu" and "ps" are present
* modify checkin matcher to "ps"
* verify "kaihu" is not present

h2.TODO: Verify emails are actually sent, use Dumbster

* login as "userA"
* open my cruise page
* add notification filter for first pipeline and first stage and event "Passes"
* message "Saved success" should be present

test case - can not add duplicate filter
* add notification filter for first pipeline and first stage and event "Passes"
* message "Failed to save" should be present

test case - can add filter for other stage
* add notification filter for second pipeline and first stage and event "All"
* message "Saved success" should be present

test case - can not add filter which is already included in existing filter
* add notification filter for second pipeline and first stage and event "Passes"
* message "Failed to save" should be present

test case - delete a filter
* delete notification filter for first pipeline and first stage and event "Passes"
* message "Successfully deleted" should be present

StageCompletionEmail
* login as "userA"
* open my cruise page
* enable email notification with email "twistuser1@cruise.com" and matcher ".*"
* open current activity page
* trigger pipeline
* verify pipeline is completed
* verify email is received
* verify email not contains "The stage was cancelled by "






Teardown of contexts
* Capture go state "NewMyCruiseEmailNotifications" - teardown
* Config two pipeline groups - teardown
* Setup password file and define roles - teardown
* Configure enterprise license - teardown


