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

public class InvalidLdapConfiguration extends AbstractConfiguration {


	public InvalidLdapConfiguration(Configuration config, ScenarioState state, RepositoryState repositoryState, ScenarioHelper scenarioHelper, Browser browser) throws Exception {
		super("/config/invalid-ldap-server-cruise-config.xml", config, state, repositoryState, scenarioHelper, browser);
	}

	@com.thoughtworks.gauge.Step("Invalid ldap configuration - setup")
	@Override
	public void setUp() throws Exception {
		super.setUp();
	}

	@com.thoughtworks.gauge.Step("Invalid ldap configuration - teardown")
	@Override
	public void tearDown() throws Exception {
		super.tearDown();
	}
}
