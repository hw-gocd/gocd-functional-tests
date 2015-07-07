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

public class DeletePackageConfiguration extends AbstractConfiguration {

	private Configuration config;
	
	public DeletePackageConfiguration(Configuration config, ScenarioState state,
			RepositoryState repositoryState, ScenarioHelper scenarioHelper, Browser browser) throws Exception {
		super("/config/delete-package-cruise-config.xml", config, state,
				repositoryState, scenarioHelper, browser);
		this.config = config;
	}

	// setUp and tearDown is needed because Twist scenarios need their contexts
	// to support these otherwise they show compile errors!
	@com.thoughtworks.gauge.Step("Delete package configuration - setup")
	public void setUp() throws Exception {
		super.setUp();
	}
	
	@Override
	protected void postProcess(CruiseConfigDom dom) throws IOException {
		pointPasswordFileToAbsolutePath(dom);
	}

	private void pointPasswordFileToAbsolutePath(CruiseConfigDom dom) throws IOException {
		File destination = config.copyPasswordFile(getClass().getResource("/config/password.properties"));
		Element passwordFile = dom.getPasswordFile();
		passwordFile.attribute("path").setValue(destination.getCanonicalPath());
	}

	@com.thoughtworks.gauge.Step("Delete package configuration - teardown")
	public void tearDown() throws Exception {
		super.tearDown();
	}
}