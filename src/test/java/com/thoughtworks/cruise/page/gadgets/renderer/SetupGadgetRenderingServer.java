package com.thoughtworks.cruise.page.gadgets.renderer;

// JUnit Assert framework can be used for verification

import net.sf.sahi.client.Browser;

public class SetupGadgetRenderingServer {

	private Browser browser;

	public SetupGadgetRenderingServer(Browser browser) {
		this.browser = browser;
	}

	@com.thoughtworks.gauge.Step("By creating user <username> with password <password>")
	public void byCreatingUserWithPassword(String username, String password) throws Exception {
		browser.navigateTo("http://localhost:3000");
		browser.link("Sign up").click();
		browser.textbox("user[email]").setValue(username);
		browser.password("user[password]").setValue(password);
		browser.submit("Create").click();
	}
}
