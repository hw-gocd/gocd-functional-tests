package com.thoughtworks.cruise.page;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.ScenarioState;

public class OnAdministrationPage extends CruisePage {
	public OnAdministrationPage(ScenarioState state, Browser browser) {
		super(state, browser);
	}

	@com.thoughtworks.gauge.Step("Verify page title is <pageTitle> - On Administration Page")
	public void verifyPageTitleIs(String pageTitle) {
		super.verifyPageTitleIs(pageTitle);
	}

	@Override
	protected String url() {
		return Urls.urlFor("/tab/admin");
	}

}
