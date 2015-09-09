HistoricalConfigSnapshotRetrival
================================

Setup of contexts
* Secure configuration - setup
* Login as "admin" - setup
* Using pipeline "basic-pipeline" - setup
* Capture go state "HistoricalConfigSnapshotRetrival" - setup

HistoricalConfigSnapshotRetrival
--------------------------------

tags: config, api, 1441, versioning

* Alias current md5 as "first-revision"

* Type new resource "linux" for agent "1" and press return

* Alias current md5 as "second-revision"
* Verify "first-revision" does not have "<resource>linux</resource>"
* Verify "current" has "<resource>linux</resource>"
* Verify "second-revision" has "<resource>linux</resource>"

* Add user "hero" as admin

* Wait for config load
* Alias current md5 as "third-revision"
* Verify "first-revision" does not have "<user>hero</user>"
* Verify "second-revision" does not have "<user>hero</user>"
* Verify "current" has "<user>hero</user>"
* Verify "third-revision" has "<user>hero</user>"






Teardown of contexts
* Capture go state "HistoricalConfigSnapshotRetrival" - teardown
* Using pipeline "basic-pipeline" - teardown
* Login as "admin" - teardown
* Secure configuration - teardown


