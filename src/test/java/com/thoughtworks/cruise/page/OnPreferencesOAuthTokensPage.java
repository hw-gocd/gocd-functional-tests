package com.thoughtworks.cruise.page;

import org.junit.Assert;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.ScenarioState;

public class OnPreferencesOAuthTokensPage extends CruisePage {

	public OnPreferencesOAuthTokensPage(ScenarioState scenarioState, Browser browser) {
		super(scenarioState, browser);
	}

	@Override
	protected String url() {
		return Urls.localhostUrlFor("/oauth/user_tokens");
	}

	@com.thoughtworks.gauge.Step("Verify token <expectedToken> exists")
	public void verifyTokenExists(String expectedToken) {
		Assert.assertEquals("Expected to find OAuth token: " + expectedToken,
				browser.cell(expectedToken).in(browser.table("oauth_user_token_table")).exists(),
				true);
	}
}
