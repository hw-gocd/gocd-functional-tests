package com.thoughtworks.cruise.page;

// JUnit Assert framework can be used for verification

import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.page.admin.PageElementIdentifiers;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

public class AlreadyOnOauthClientForm {

	private Browser browser;
	private String clientName;
	private String redirectUrl;

	public AlreadyOnOauthClientForm(Browser browser) {
		this.browser = browser;
	}

	@com.thoughtworks.gauge.Step("Using client name <clientName>")
	public void usingClientName(String clientName) throws Exception {
		this.clientName = clientName;
	}

	@com.thoughtworks.gauge.Step("Using redirect url <redirectUrl>")
	public void usingRedirectUrl(String redirectUrl) throws Exception {
		this.redirectUrl = redirectUrl;
	}

	@com.thoughtworks.gauge.Step("Add new auth client")
	public void addNewAuthClient() throws Exception {
		browser.textbox(PageElementIdentifiers.get(PageElementIdentifiers.OAUTH_CLIENT_NAME)).setValue(clientName);
        browser.textbox(PageElementIdentifiers.get(PageElementIdentifiers.OAUTH_CLIENT_REDIRECT_URI)).setValue(redirectUrl);
        ElementStub submitLink = browser.link("Submit");
        Assert.assertThat(submitLink.exists(), Is.is(true));
		submitLink.click();
	}

    @com.thoughtworks.gauge.Step("Change redirect url to <newRedirectUrl>")
	public void changeRedirectUrlTo(String newRedirectUrl) throws Exception {
		browser.textbox(PageElementIdentifiers.get(PageElementIdentifiers.OAUTH_CLIENT_REDIRECT_URI)).setValue(Urls.urlFor(newRedirectUrl));
	}

	@com.thoughtworks.gauge.Step("Update this client")
	public void updateThisClient() throws Exception {
		browser.link("Submit").click();
	}

	public void navigateBackToListing() throws Exception {
		browser.link("Back").click();
	}
}
