package com.thoughtworks.cruise.context.configuration;

// JUnit Assert framework can be used for verification

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

public class ValidLdapConfiguration extends AbstractConfiguration{


	public ValidLdapConfiguration(Configuration config, ScenarioState state, RepositoryState repositoryState, ScenarioHelper scenarioHelper, Browser browser) throws Exception {
		super("/config/valid-ldap-server-cruise-config.xml",config,state,repositoryState, scenarioHelper, browser);
	}

	@com.thoughtworks.gauge.Step("Valid ldap configuration - setup")
	public void setUp() throws Exception {
		super.setUp();
	}

	@com.thoughtworks.gauge.Step("Valid ldap configuration - teardown")
	public void tearDown() throws Exception {
		super.tearDown();
	}

}
