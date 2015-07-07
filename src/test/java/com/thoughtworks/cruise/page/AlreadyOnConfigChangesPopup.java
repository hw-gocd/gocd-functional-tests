package com.thoughtworks.cruise.page;
// JUnit Assert framework can be used for verification


import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import org.hamcrest.core.Is;
import static junit.framework.Assert.assertTrue;
import static org.hamcrest.Matchers.containsString;
import static org.junit.Assert.assertThat;
import org.springframework.beans.factory.annotation.Autowired;

import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.twist.core.execution.TwistScenarioDataStore;

public class AlreadyOnConfigChangesPopup {

	private Browser browser;

	@Autowired
	private TwistScenarioDataStore scenarioStore;

	private final CurrentPageState currentPageState;

	public AlreadyOnConfigChangesPopup(Browser browser, CurrentPageState currentPageState) {
		this.browser = browser;
		this.currentPageState = currentPageState;
		currentPageState.assertCurrentPageIs(Page.STAGE_CONFIG_CHANGES_POPUP);
	}

	@com.thoughtworks.gauge.Step("Verify added changes contains lines <line>")
	public void verifyAddedChangesContainsLines(String line) throws Exception {
		ElementStub addedLines = browser.row("add").in(browser.div("config-changes"));
		assertThat(addedLines.getText(), containsString(line));
	}

	@com.thoughtworks.gauge.Step("Verify removed changes contains lines <line>")
	public void verifyRemovedChangesContainsLines(String line) throws Exception {
		ElementStub addedLines = browser.row("remove").in(browser.div("config-changes"));
		assertThat(addedLines.getText(), containsString(line));
	}

}