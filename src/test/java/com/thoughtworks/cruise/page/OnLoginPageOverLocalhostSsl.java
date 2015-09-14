
package com.thoughtworks.cruise.page;

// JUnit Assert framework can be used for verification

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;
import net.sf.sahi.client.Browser;

public class OnLoginPageOverLocalhostSsl extends OnLoginPage {

    private Browser browser;

    public OnLoginPageOverLocalhostSsl(Browser browser, final ScenarioState scenarioState, final ScenarioHelper scenarioHelper) {
        super(scenarioState, scenarioHelper, browser);
        this.browser = browser;
    }

    @com.thoughtworks.gauge.Step("Login as <user> - On Login Page Over Localhost Ssl")
	public void loginAs(String user) {
        super.loginAs(user);
    }

    @com.thoughtworks.gauge.Step("On Admin page - Logged in using ssl")
    public void goToAdminPage() {
        navigateToURL();
    }
    @Override
    protected String url() {
        return Urls.localhostSslUrlFor("");
    }
}
