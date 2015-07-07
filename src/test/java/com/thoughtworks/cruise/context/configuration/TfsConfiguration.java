package com.thoughtworks.cruise.context.configuration;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

public class TfsConfiguration extends AbstractConfiguration {

	public TfsConfiguration(Configuration config, ScenarioState state, RepositoryState repositoryState, ScenarioHelper scenarioHelper, Browser browser) throws Exception {
		super("/config/tfs-cruise-config.xml", config, state, repositoryState, scenarioHelper, browser);
	}

	// setUp and tearDown is needed because Twist scenarios need their contexts to support these otherwise they show compile errors!
	@com.thoughtworks.gauge.Step("Tfs configuration - setup")
	public void setUp() throws Exception {
		super.setUp();
	}

	@com.thoughtworks.gauge.Step("Tfs configuration - teardown")
	public void tearDown() throws Exception {
		super.tearDown();
	}
}