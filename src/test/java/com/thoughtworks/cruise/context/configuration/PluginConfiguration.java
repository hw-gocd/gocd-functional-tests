package com.thoughtworks.cruise.context.configuration;

import java.io.File;
import java.io.IOException;

import net.sf.sahi.client.Browser;

import org.dom4j.Element;

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public class PluginConfiguration extends AbstractConfiguration {

	private Configuration config;

	
	public PluginConfiguration(Configuration config, ScenarioState state, RepositoryState repositoryState, ScenarioHelper scenarioHelper, Browser browser) throws Exception {
		super("/config/plugins-cruise-config.xml", config, state, repositoryState, scenarioHelper, browser);
		this.config = config;

	}

	// setUp and tearDown is needed because Twist scenarios need their contexts to support these otherwise they show compile errors!
	@com.thoughtworks.gauge.Step("Plugin configuration - setup")
	public void setUp() throws Exception {
		super.setUp();
	}
	
	@Override
	protected void postProcess(CruiseConfigDom dom) throws IOException {
		File defaultPasswordProperties = copyPasswordPropertiesToServer("/config/password.properties");
		File otherPasswordProperties = copyPasswordPropertiesToServer("/config/only-admin-password.properties");
		pointPasswordFileToAbsolutePath(dom, defaultPasswordProperties);
	}

	private void pointPasswordFileToAbsolutePath(CruiseConfigDom dom, File passwordProperties) throws IOException {
		Element passwordFile = dom.getPasswordFile();
		passwordFile.attribute("path").setValue(passwordProperties.getCanonicalPath());
	}

	private File copyPasswordPropertiesToServer(String name) {
		return config.copyPasswordFile(getClass().getResource(name));
	}
    
	@com.thoughtworks.gauge.Step("Plugin configuration - teardown")
	public void tearDown() throws Exception {
		super.tearDown();
	}

}
