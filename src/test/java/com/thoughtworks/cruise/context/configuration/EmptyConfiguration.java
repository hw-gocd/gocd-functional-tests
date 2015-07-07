package com.thoughtworks.cruise.context.configuration;

import net.sf.sahi.client.Browser;
import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

public class EmptyConfiguration extends AbstractConfiguration {
	public EmptyConfiguration(Configuration config, RepositoryState repositoryState, ScenarioHelper scenarioHelper, Browser browser) throws Exception {
		super("/config/empty-cruise-config.xml", config, null, repositoryState, scenarioHelper, browser);
	}
}