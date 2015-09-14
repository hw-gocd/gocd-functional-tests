package com.thoughtworks.cruise;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.page.CruisePage;
import com.thoughtworks.cruise.page.OnAnyPage;
import com.thoughtworks.cruise.page.OnLoginPage;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;


public class VerifyIfUserIsAdmin {

	private String loginAsUser;
	private final OnLoginPage onLoginPage;
	private final CruisePage onAnyPage;
	private Browser browser;

	public VerifyIfUserIsAdmin(OnLoginPage onLoginPage, OnAnyPage onAnyPage, Browser browser) {
		this.onLoginPage = onLoginPage;
		this.onAnyPage = onAnyPage;
		this.browser = browser;
	}

	public void setUp() throws Exception {
		onAnyPage.logout();
	}

	public void tearDown() throws Exception {
		onAnyPage.logout();
	}

	public void setAdmin(final boolean isAdmin) throws Exception {
		Assertions.waitUntil(Timeout.THIRTY_SECONDS, new Predicate() {
			
			public boolean call() throws Exception {
				onAnyPage.logout();
				onLoginPage.loginAs(loginAsUser);
				ElementStub adminLink = browser.link("ADMIN");
				return adminLink.exists() == isAdmin;
			}
		});
	}

	public void setLoginAsUser(String loginAsUser) {
		this.loginAsUser = loginAsUser;
	}

	@com.thoughtworks.gauge.Step("VerifyIfUserIsAdmin <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Throwable {
		com.thoughtworks.twist.migration.brt.BRTMigrator brtMigrator = new com.thoughtworks.twist.migration.brt.BRTMigrator();
		try {
			brtMigrator.BRTExecutor(table, this);
		} catch (Exception e) {
			throw e.getCause();
		}
	}
}