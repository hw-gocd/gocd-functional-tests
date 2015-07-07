package com.thoughtworks.cruise.page;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.ScenarioState;

public class OnAnyPageOverLocalhostSsl extends CruisePage {

	public OnAnyPageOverLocalhostSsl(ScenarioState scenarioState, Browser browser) {
		super(scenarioState, false, browser);
	}	
		
	public void lookingAtPipeline(String pipelineName) throws Exception {
		scenarioState.usingPipeline(pipelineName);
	}

	@Override
	protected String url() {
		return Urls.localhostSslUrlFor("/");
	}
	
	@com.thoughtworks.gauge.Step("Logout - On any page over localhost ssl")
	public void logout() {
		super.logout();
	}
}
