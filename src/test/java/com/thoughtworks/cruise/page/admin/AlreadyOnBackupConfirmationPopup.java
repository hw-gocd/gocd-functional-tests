package com.thoughtworks.cruise.page.admin;

// JUnit Assert framework can be used for verification

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

import net.sf.sahi.client.Browser;

public class AlreadyOnBackupConfirmationPopup {

	private Browser browser;
	private final CurrentPageState state;

	public AlreadyOnBackupConfirmationPopup(Browser browser, CurrentPageState state) {
		this.browser = browser;
		this.state = state;
		state.assertCurrentPageIs(Page.PERFORM_BACKUP_POPUP);
	}

	@com.thoughtworks.gauge.Step("Proceed with backup")
	public void proceedWithBackup() throws Exception {
		browser.submit(Regex.wholeWord("submit")).in(browser.div("MB_content")).click();
		state.currentPageIs(Page.BACKUP_SERVER_TAB);
	}

}
