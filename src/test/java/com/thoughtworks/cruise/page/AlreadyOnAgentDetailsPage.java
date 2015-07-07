package com.thoughtworks.cruise.page;

import org.hamcrest.core.Is;
import org.junit.Assert;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

public class AlreadyOnAgentDetailsPage extends CruisePage {
	
	private final CurrentPageState currentPageState;

	public AlreadyOnAgentDetailsPage(ScenarioState scenarioState, CurrentPageState currentPageState, Browser browser) {
		super(scenarioState, true, browser);
		this.currentPageState = currentPageState;
		currentPageState.assertCurrentPageIs(Page.AGENT_DETAILS);
	}

	@Override
	protected String url() {
		return null;
	}

	@com.thoughtworks.gauge.Step("Verify presence of tabs <tabs>")
	public void verifyPresenceOfTabs(String tabs) throws Exception {
		String[] allTabs = splitMe(tabs);
		for(String tabName : allTabs) {
			Assert.assertThat(String.format("Tab %s not found", tabName), browser.link(tabName.trim()).exists(), Is.is(true));
		}
	
	}
	
	
	@com.thoughtworks.gauge.Step("Verify absence of tabs <tabs>")
	public void verifyAbsenceOfTabs(String tabs) throws Exception {
		String[] allTabs = splitMe(tabs);
		for(String tabName : allTabs) {
			Assert.assertThat(String.format("Tab %s not found", tabName), browser.link(tabName.trim()).exists(), Is.is(false));
		}
	
	}

	@com.thoughtworks.gauge.Step("Verify presence of labels <labels>")
	public void verifyPresenceOfLabels(String labels) throws Exception {
		String[] allLabels = splitMe(labels);
        ElementStub detailsContainer = browser.div("agent_details_pane");
        for(String label : allLabels) {
        	Assert.assertThat(String.format("Label %s not found on agent details tab", label), browser.label(label.trim()).in(detailsContainer).exists(), Is.is(true));
        }
	}

    @com.thoughtworks.gauge.Step("Navigate to job run history")
	public void navigateToJobRunHistory() throws Exception {
		browser.link("Job Run History").click();
		currentPageState.currentPageIs(Page.AGENT_JOB_RUN_HISTORY);
	}
}
