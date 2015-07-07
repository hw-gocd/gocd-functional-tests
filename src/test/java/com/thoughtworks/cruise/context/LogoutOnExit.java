package com.thoughtworks.cruise.context;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.page.OnAnyPage;
import com.thoughtworks.cruise.page.OnLoginPage;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

public class LogoutOnExit {
	private final ScenarioState state;
	private ScenarioHelper scenarioHelper;
	private final Browser browser;

	public LogoutOnExit(ScenarioState state, ScenarioHelper scenarioHelper, Browser browser) {
		this.state = state;
		this.scenarioHelper = scenarioHelper;
		this.browser = browser;
	}
	
	@com.thoughtworks.gauge.Step("Logout on exit - setup")
	public void setUp() throws Exception {
	}

	@com.thoughtworks.gauge.Step("Logout on exit - teardown")
	public void tearDown() throws Exception {
		new OnAnyPage(state, scenarioHelper, browser).logout();
		state.logOut();
	}

}
