package com.thoughtworks.cruise.context;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.page.OnAnyPage;
import com.thoughtworks.cruise.page.OnLoginPage;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

public class LoginAs {
	private final ScenarioState state;
	private ScenarioHelper scenarioHelper;
	private final Browser browser;

	public LoginAs(ScenarioState state, ScenarioHelper scenarioHelper, Browser browser) {
		this.state = state;
		this.scenarioHelper = scenarioHelper;
		this.browser = browser;
	}
	
	@com.thoughtworks.gauge.Step("Login as <userName> - setup")
	public void setUp(String userName) throws Exception {
		//Logout is done explicitly here to avoid failures if teardown fails to run. This happens when there is a failure in setup
		new OnAnyPage(state, scenarioHelper, browser).logout();
		new OnLoginPage(state, scenarioHelper, browser).loginAs(userName);
		state.loggedInAs(userName);
	}

	@com.thoughtworks.gauge.Step("Login as <ignore> - teardown")
	public void tearDown(String ignore) throws Exception {
		new OnAnyPage(state, scenarioHelper, browser).logout();
		state.logOut();
	}

}
