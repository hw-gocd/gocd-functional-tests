package com.thoughtworks.cruise.page;

// JUnit Assert framework can be used for verification

import com.thoughtworks.cruise.CruiseAgents;
import com.thoughtworks.cruise.api.UsingAgentsApi;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.ScenarioState;

import net.sf.sahi.client.Browser;

public class AlreadyOnServerDetailPage extends OnServerDetailPage {

	public AlreadyOnServerDetailPage(ScenarioState state, UsingAgentsApi agentsApi, CruiseAgents createdAgents, Browser browser, CurrentPageState currentPageState) {
		super(state, agentsApi, createdAgents, browser, true);
		currentPageState.assertCurrentPageIs(Page.SERVER_DETAILS_PAGE);
	}

	public void verifyOnServerDetailsPage() throws Exception {
		super.verifyRedirectedToServerDetailPage();
	}
}
