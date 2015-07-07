package com.thoughtworks.cruise.page.edit;

import org.hamcrest.core.Is;
import org.junit.Assert;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.page.CruisePage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

public class AlreadyOnNewPipelineGroupPopup extends CruisePage {
	private Browser browser;
	private CurrentPageState currentPageState;

	public AlreadyOnNewPipelineGroupPopup(Browser browser, ScenarioState state,
			CurrentPageState pageState) {
		super(state, true, browser);
		this.browser = browser;
		this.currentPageState = pageState;
		pageState.assertCurrentPageIs(Page.NEW_PIPELINE_GROUP_POPUP);
	}

	@Override
	protected String url() {
		// TODO Auto-generated method stub
		return null;
	}

	@com.thoughtworks.gauge.Step("Save - Already On New Pipeline Group Popup")
	public void save() throws Exception {
		browser.submit("SAVE").click();
	}

	@com.thoughtworks.gauge.Step("Verify error message <expectedMessage> - Already On New Pipeline Group Popup")
	public void verifyErrorMessage(String expectedMessage) throws Exception {
		ElementStub errorDiv = browser.div("form_error");
		Assert.assertThat(errorDiv.exists(), Is.is(true));
		Assert.assertThat(errorDiv.getText(), Is.is(expectedMessage));
	}

	@com.thoughtworks.gauge.Step("Enter pipeline group name <pipelineGroupName> - Already On New Pipeline Group Popup")
	public void enterPipelineGroupName(String pipelineGroupName) throws Exception {
		browser.textbox("group[group]").setValue(pipelineGroupName);
	}

	@com.thoughtworks.gauge.Step("Save for success - Already On New Pipeline Group Popup")
	public void saveForSuccess() throws Exception {
		save();
		currentPageState.currentPageIs(Page.EDIT_PIPELINE_GROUP);
	}
}
