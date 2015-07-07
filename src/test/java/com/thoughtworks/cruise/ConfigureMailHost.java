package com.thoughtworks.cruise;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.page.AlreadyOnServerConfigurationTab;
import com.thoughtworks.cruise.page.OnAdminPage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;

public class ConfigureMailHost {

	private AlreadyOnServerConfigurationTab tab;
	private final Browser browser;
	private final CurrentPageState currentPageState;
	private OnAdminPage onAdminPage;

	public ConfigureMailHost(Browser browser, CurrentPageState currentPageState, ScenarioState scenarioState) {
		this.browser = browser;
		this.currentPageState = currentPageState;
		this.onAdminPage = new OnAdminPage(scenarioState, browser, currentPageState);
	}

	public String message() throws Exception {
		tab.saveConfiguration();
		return tab.message();
	}

	public void setAdminEmail(String adminEmail) throws Exception {
		tab.forField("adminMail", adminEmail);
	}

	public void setFromEmail(String fromEmail) throws Exception {
		tab.forField("from", fromEmail);
	}

	public void setHostname(String hostname) throws Exception {
		tab.forField("hostName", hostname);
	}

	public void setLdapPassword(String ldapPassword) throws Exception {
		tab.forField("ldap_password", ldapPassword);
	}

	public void setLdapUsername(String ldapUsername) throws Exception {
		tab.forField("ldap_username", ldapUsername);
	}

	public void setPassword(String password) throws Exception {
		tab.forField("password", password);

	}

	public void setPort(String port) throws Exception {
		tab.forField("port", port);
	}

	public void setSearchBase(String searchBase) throws Exception {
		tab.forTextAreaField("ldap_search_base", searchBase);
	}

	public void setSearchFilter(String searchFilter) throws Exception {
		tab.forField("ldap_search_filter", searchFilter);
	}

	public void setTLS(String checked) throws Exception {
		tab.forField("tls", checked);
	}

	public void setUp() throws Exception {
		onAdminPage.openTab("Server Configuration");	
		tab = new AlreadyOnServerConfigurationTab(browser, currentPageState);
	}

	public void setURI(String uRI) throws Exception {
		tab.forField("ldap_uri", uRI);
	}

	public void setUsername(String username) throws Exception {
		tab.forField("username", username);
	}

	public void tearDown() throws Exception {
	}

	@com.thoughtworks.gauge.Step("ConfigureMailHost <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Exception {
		com.thoughtworks.twist.migration.brt.BRTMigrator.BRTExecutor(table, this);
	
	}
}
