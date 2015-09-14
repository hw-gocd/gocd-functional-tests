NewFreeLicense
==============

Setup of contexts
* Free license configuraion - setup
* Capture go state "NewFreeLicense" - setup

NewFreeLicense
--------------

tags: #2760, licensing, free license, #2403, #2514, manual

Old Twist test - AgentLicensing.scn

* open server details page
* user applied license key
* then licence saved successfully
* add 3 agents
* verify message "Your license allows you to use 0 remote agents, but you are trying to use 3. Please disable agents to comply with your license, or contact our sales team to buy more agents." shown on all pages
* verify message "Your license allows you to use 0 remote agents, but you are trying to use 3. Please disable agents to comply with your license, or contact our sales team to buy more agents." is shown in the health state dialog as a warning

Any old license will be considered free license

* open server details page
* enter old enterprise license
* verify shows free edition
* enter old standard license
* verify shows free edition
* enter old free license
* verify shows free edition
* verify shows "0" agent


Cannot turn on operate permission

* allow user "userA" to operate pipeline group "firstGroup"
* login as "userB"
* open current activity page
* verify shows error message "License limitation error"
* verify shows error message "You have configured operate permission feature"
* verify shows pipeline group "firstGroup"
* remove operate permission configuration from first pipeline group
* verify not show error message "License limitation error"
* Verify cannot add permissions through clicky admin
* Verify flash error "You cannot configure security permissions in Go Community Edition. Help Topic: Configuration"

Cannot turn on view permission

* login as "user-no-permission"
* open current activity page
* verify shows error message "License limitation error"
* verify shows error message "You have configured view permission feature"
* verify shows pipeline group "firstGroup"
* remove view permission configuration from first pipeline group
* verify not show error message "License limitation error"
* Verify cannot add permissions through clicky admin
* Verify flash error "You cannot configure security permissions in Go Community Edition. Help Topic: Configuration"

Cannot have more than one pipeline group

* Verify cannot add group through clicky admin
* Try to add a new pipeline group through source xml
* Verify flash error "You cannot have more than one Pipeline group in Go Community Edition. Help Topic: Configuration"





Teardown of contexts
* Capture go state "NewFreeLicense" - teardown
* Free license configuraion - teardown


