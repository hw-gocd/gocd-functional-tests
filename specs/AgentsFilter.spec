AgentsFilter
============

Setup of contexts 
* Multiple agents configuration - setup
* With "1" live agents in directory "AgentsUIScreen" - setup
* Capture go state "AgentsUIScreen" - setup

AgentsFilter
------------

tags: agents, UI, automate, 5455, 5554

Name based search
* Enter filter value "name: random"
* Auto completes should show suggestions "random, random1, random2, random3, random4"
* Perform filter
* Verify agents "random, random1, random2, random3, random4" show up in results
* Enter filter value "name: random1"
* Auto completes should show suggestion "random1"
* Perform filter
* Verify agents "random1" show up in results
* Enter filter value "name: \"random\""
* Perform filter
* Verify agents "random" show up in results
* Enter filter value "name: \"random \""
* Perform filter
* Verify total agent count is "0"

IP based search
* Enter filter value "ip: 10.232.3"
* Auto completes should show suggestions "10.232.3.1, 10.232.3.2, 10.232.3.3"
* Perform filter
* Verify agents "random1, random2, random3" show up in results
* Enter filter value "ip: 10.232.3.1"
* Auto completes should show suggestion "10.232.3.1"
* Perform filter
* Verify agents "random1" show up in results
* Enter filter value "ip: \"10.232.3\""
* Perform filter
* Verify total agent count is "0"
* Enter filter value "ip: \"10.232.3.1\""
* Perform filter
* Verify agents "random1" show up in results

Environment based search
* Enter filter value "environment: Prod"
* Auto completes should show suggestions "Prod, Production, Prod-new"
* Perform filter
* Verify agents "random, random1, random3, random4" show up in results
* Enter filter value "environment: \"Prod\""
* Perform filter
* Verify agents "random1, random3" show up in results
* Enter filter value "environment: Production"
* Auto completes should show suggestion "Production"
* Perform filter
* Verify agents "random4" show up in results
* Enter filter value "environment: \"Prod-n\""
* Perform filter
* Verify total agent count is "0"
* Enter filter value "environment: \"Prod-new\""
* Perform filter
* Verify agents "random" show up in results


Status based search
* Enter filter value "status: miss"
* Auto completes should show suggestions "missing"
* Perform filter
* Verify agents "random, random1, random2, random3, random4" show up in results
* Enter filter value "environment: \"miss\""
* Perform filter
* Verify total agent count is "0"
* Enter filter value "status: \"missing\""
* Perform filter
* Verify agents "random, random1, random2, random3, random4" show up in results
* Enter filter value "status: \"idle \""
* Perform filter
* Verify total agent count is "0"

Resource based search
* Enter filter value "resource: win"
* Auto completes should show suggestions "win, windows"
* Perform filter
* Verify agents "random1, random2" show up in results
* Enter filter value "resource: \"win\""
* Perform filter
* Verify agents "random1" show up in results
* Enter filter value "resource: \"windows\""
* Perform filter
* Verify agents "random1, random2" show up in results
* Enter filter value "resource: \"lin\""
* Perform filter
* Verify total agent count is "0"
* Enter filter value "resource: linux"
* Auto completes should show suggestions "Linux, Linux centos, Linux-fedora"
* Perform filter
* Verify agents "random, random3, random4" show up in results
* Enter filter value "resource: \"linux\""
* Perform filter
* Verify agents "random3" show up in results


OS based search
* Enter filter value "os: Linux"
* Auto completes should show suggestions "Linux"
* Perform filter
* Verify total agent count is "1"
* Enter filter value "os: \"Linux\""
* Perform filter
* Verify total agent count is "1"
* Enter filter value "os:"
* Auto completes should show suggestions "Linux"
* Perform filter
* Verify total agent count is "6"
* Enter filter value "os: \"lin\""
* Perform filter
* Verify total agent count is "0"


Multiple filters (performs OR operation)
* Enter filter value "resource: \"windows\", environment: \"prod\", ip: 10.1.1"
* Perform filter
* Verify agents "random1, random2, random3, random4" show up in results
* Enter filter value "resource: \"win\", environment: prod , ip: 10.1.1"
* Perform filter
* Verify agents "random, random1, random3, random4" show up in results




Teardown of contexts 
* Capture go state "AgentsUIScreen" - teardown
* With "1" live agents in directory "AgentsUIScreen" - teardown
* Multiple agents configuration - teardown


