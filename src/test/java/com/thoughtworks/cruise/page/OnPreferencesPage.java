package com.thoughtworks.cruise.page;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.ScenarioState;

public class OnPreferencesPage extends CruisePage {

	public OnPreferencesPage(ScenarioState scenarioState, Browser browser) {
		super(scenarioState, browser);
	}

	protected String url() {
		return Urls.urlFor("/tab/mycruise/user");
	}
	
	@com.thoughtworks.gauge.Step("Verify page title is <expectedTitle>")
	public void verifyPageTitleIs(String expectedTitle) {
		super.verifyPageTitleIs(expectedTitle);
	}
	
	@com.thoughtworks.gauge.Step("Verify cruise footer - On preferences page")
	@Override
	public void verifyCruiseFooter() throws Exception {
		super.verifyCruiseFooter();
	}
	
    
    public void changeEmailToAndAliasTo(String email, String alias) throws Exception {
        browser.byId("edit-matchers").click();
        browser.byId("email").setValue(email);
        browser.byId("matchers").setValue(alias);        
        browser.byId("save-matchers").click();
    }    
    

}
