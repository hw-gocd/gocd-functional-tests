PluginValidations
=================

Setup of contexts
* Capture go state "PluginValidations" - setup

PluginValidations
-----------------

tags: #7481, Plugin Validations, plugins-tests

* Open "Plugins" tab

* Verify plugin named "invalid-xml-plugin.jar" with id "invalid-xml-plugin.jar" is marked as invalid with message "Plugin with ID (invalid-xml-plugin.jar) is not valid: XML Schema validation of Plugin Descriptor(plugin.xml) failed."
* Verify plugin named "plugin-with-invalid-id.jar" with id "plugin-with-invalid-id.jar" is marked as invalid with message "Plugin with ID (plugin-with-invalid-id.jar) is not valid: XML Schema validation of Plugin Descriptor(plugin.xml) failed."
* Verify plugin named "plugin-with-multiple-load-methods.jar" with id "plugin-with-multiple-load-methods.jar" is marked as invalid with message which is either "Class [PluginWithMultipleLoadMethods] is annotated with @Extension will not be registered. Reason: java.lang.RuntimeException: More than one method with @Load annotation not allowed. Methods Found: [public void com.tw.qa.plugin.sample.PluginWithMultipleLoadMethods.onLoad(com.thoughtworks.go.plugin.api.info.PluginContext), public void com.tw.qa.plugin.sample.PluginWithMultipleLoadMethods.duplicateLoad(com.thoughtworks.go.plugin.api.info.PluginContext)]" or "Class [PluginWithMultipleLoadMethods] is annotated with @Extension will not be registered. Reason: java.lang.RuntimeException: More than one method with @Load annotation not allowed. Methods Found: [public void com.tw.qa.plugin.sample.PluginWithMultipleLoadMethods.duplicateLoad(com.thoughtworks.go.plugin.api.info.PluginContext), public void com.tw.qa.plugin.sample.PluginWithMultipleLoadMethods.onLoad(com.thoughtworks.go.plugin.api.info.PluginContext)]"




Teardown of contexts
* Capture go state "PluginValidations" - teardown


