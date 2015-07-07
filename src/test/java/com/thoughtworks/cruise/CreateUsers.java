package com.thoughtworks.cruise;
import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.page.OnAnyPage;
import com.thoughtworks.cruise.page.OnLoginPage;
import com.thoughtworks.cruise.page.OnPreferencesPage;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

public class CreateUsers {   

    private String email;

    private final ScenarioState scenarioState;

	private final ScenarioHelper scenarioHelper;

	private final Browser browser;    
    
    public CreateUsers(ScenarioState scenarioState, ScenarioHelper scenarioHelper, Browser browser) {
        this.scenarioState = scenarioState;
		this.scenarioHelper = scenarioHelper;
		this.browser = browser;
    }

    public void setAlias(String alias) throws Exception {
        System.err.println("setting alias " + alias);
        new OnPreferencesPage(scenarioState, browser).changeEmailToAndAliasTo(this.email, alias);
    }

    public void setEmail(String email) throws Exception {        
        this.email = email;
    }
    
    public void setUsername(String username) throws Exception {
        System.err.println("logging in as" + username);
        new OnLoginPage(scenarioState, scenarioHelper, browser).loginAs(username);
        System.err.println("logged in");
    }
    
    public void setUp() {        
        new OnAnyPage(scenarioState, scenarioHelper, browser).logout();        
    }

    public void tearDown() throws Exception {        
        new OnAnyPage(scenarioState, scenarioHelper, browser).logout();        
    }

	@com.thoughtworks.gauge.Step("CreateUsers <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Exception {
		com.thoughtworks.twist.migration.brt.BRTMigrator.BRTExecutor(table, this);
	
	}

}