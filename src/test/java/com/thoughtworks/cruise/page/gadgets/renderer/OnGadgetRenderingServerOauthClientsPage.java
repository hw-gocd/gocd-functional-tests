package com.thoughtworks.cruise.page.gadgets.renderer;

// JUnit Assert framework can be used for verification

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.OauthState;
import com.thoughtworks.cruise.state.OauthState.OauthClient;

import net.sf.sahi.client.Browser;

public class OnGadgetRenderingServerOauthClientsPage {

	private Browser browser;
	private final OauthState oauthState;
	private OauthClient client;
	private String service;

	public OnGadgetRenderingServerOauthClientsPage(Browser browser, OauthState oauthState) {
		this.browser = browser;
		this.oauthState = oauthState;
		browser.navigateTo("http://localhost:3000/gadgets/oauth_clients");
	}

	@com.thoughtworks.gauge.Step("Using client <clientName>")
	public void usingClient(String clientName) throws Exception {
		client = oauthState.getOauthClientNamed(clientName);
	}

	@com.thoughtworks.gauge.Step("Using service <service>")
	public void usingService(String service) throws Exception {
		this.service = service;
	}

	@com.thoughtworks.gauge.Step("Add client for gadget <gadgetName>")
	public void addClientForGadget(String gadgetName) throws Exception {
		browser.link("New gadgets_oauth_client").click();
		browser.textbox("gadgets_oauth_client[gadget_url]").setValue(Urls.gadgetUrl(gadgetName));
		browser.textbox("gadgets_oauth_client[client_id]").setValue(client.getId());
		browser.textbox("gadgets_oauth_client[client_secret]").setValue(client.getSecret());
		browser.textbox("gadgets_oauth_client[service_name]").setValue(service);
		browser.textbox("gadgets_oauth_client[redirect_uri]").setValue(client.getRedirectURI());
		browser.submit("Create").click();
	}
}
