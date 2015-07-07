package com.thoughtworks.cruise.page;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.ScenarioState;

public class OnAnyPageOverHostnameSsl extends CruisePage {

	public OnAnyPageOverHostnameSsl(ScenarioState scenarioState, Browser browser) {
		super(scenarioState, false, browser);
	}	
		
	public void lookingAtPipeline(String pipelineName) throws Exception {
		scenarioState.usingPipeline(pipelineName);
	}

	@Override
	protected String url() {
		return Urls.sslUrlFor("/");
	}
	
	@com.thoughtworks.gauge.Step("Logout - On Any Page Over Hostname Ssl")
	public void logout() {
		super.logout();
	}
}
