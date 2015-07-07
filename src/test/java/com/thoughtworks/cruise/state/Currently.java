package com.thoughtworks.cruise.state;


//A wrapper around scenario state. ensures that we use the same instance as the one spring uses to inject state into other objects
public class Currently {
	
	private ScenarioState state;
	public Currently(ScenarioState state) {
		this.state = state;
	}

	@com.thoughtworks.gauge.Step("Logged in as <userName>")
	public void loggedInAs(String userName) throws Exception {
		state.loggedInAs(userName);
	}
}
