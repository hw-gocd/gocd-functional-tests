package com.thoughtworks.cruise;
import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.api.UsingAgentsApi;
import com.thoughtworks.cruise.page.AlreadyOnOauthClientForm;
import com.thoughtworks.cruise.page.AlreadyOnOauthClientsListing;
import com.thoughtworks.cruise.page.OnAdminPage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.OauthState;
import com.thoughtworks.cruise.state.ScenarioState;

public class PopulateOAuthClients {

	private Browser browser;

	private String clientName;
	private String redirectUrl;

	private AlreadyOnOauthClientForm form;

	private final OauthState outhState;

	public PopulateOAuthClients(Browser browser, ScenarioState state, UsingAgentsApi agentsApi, CruiseAgents createdAgents, CurrentPageState currentPageState, OauthState outhState) throws Exception {
		this.browser = browser;
		this.outhState = outhState;
		new OnAdminPage(state, browser, currentPageState).openTab("OAuth Clients");
	}

	public void setClientName(String clientName) throws Exception {
		this.clientName = clientName;
		form.usingClientName(clientName);
	}

	public void setRedirectUrl(String redirectUrl) throws Exception {
		this.redirectUrl = Urls.localhostUrlFor(redirectUrl);
		form.usingRedirectUrl(this.redirectUrl);
		form.addNewAuthClient();
	}

	public void setUp() throws Exception {
		form = new AlreadyOnOauthClientForm(browser);
		new AlreadyOnOauthClientsListing(browser, outhState).navigateToNewClientForm();
	}

	public void tearDown() throws Exception {
		new AlreadyOnOauthClientsListing(browser, outhState).verifyTableShowsAsRedirectUriFor(redirectUrl, clientName);
	}

	@com.thoughtworks.gauge.Step("PopulateOAuthClients <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Throwable {
		com.thoughtworks.twist.migration.brt.BRTMigrator brtMigrator = new com.thoughtworks.twist.migration.brt.BRTMigrator();
		try {
			brtMigrator.BRTExecutor(table, this);
		} catch (Exception e) {
			throw e.getCause();
		}
	}
}