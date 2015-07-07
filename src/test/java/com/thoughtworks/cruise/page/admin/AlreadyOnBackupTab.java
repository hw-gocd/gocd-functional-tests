package com.thoughtworks.cruise.page.admin;

import static org.hamcrest.Matchers.is;
import static org.hamcrest.text.StringContains.containsString;
import static org.junit.Assert.assertThat;
import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

public class AlreadyOnBackupTab {

	private Browser browser;
	private final CurrentPageState state;

	public AlreadyOnBackupTab(Browser browser, CurrentPageState state) {
		this.browser = browser;
		this.state = state;
		state.assertCurrentPageIs(Page.BACKUP_SERVER_TAB);
	}

	@com.thoughtworks.gauge.Step("Verify the location of the backup store is at <nameOfDir>")
	public void verifyTheLocationOfTheBackupStoreIsAt(String nameOfDir) throws Exception {
		assertThat(elementBackupLocation().getText().trim(), containsString(nameOfDir));
	}

	private ElementStub elementBackupLocation() {
		return browser.strong(Regex.wholeWord("location")).in(browser.span(Regex.wholeWord("info")).in(browser.div(Regex.wholeWord("backup_storage_message")).in(browser.div(Regex.wholeWord("backup_server")))));
	}

	@com.thoughtworks.gauge.Step("Verify the last performed backup message contains <message>")
	public void verifyTheLastPerformedBackupMessageContains(String message) throws Exception {
		assertThat(browser.span(0).in(browser.div(Regex.wholeWord("last_backup"))).getText(), containsString(message));
	}

	@com.thoughtworks.gauge.Step("Perform backup")
	public void performBackup() throws Exception {
		browser.byId("backup_server").click();
		state.currentPageIs(Page.PERFORM_BACKUP_POPUP);
	}

	@com.thoughtworks.gauge.Step("Verify the message <message>")
	public void verifyTheMessage(String message) throws Exception {
		assertThat(browser.div(message).exists(), is(true));
	}
}
