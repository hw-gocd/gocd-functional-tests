package com.thoughtworks.cruise.page;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.CruiseAgents;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.api.UsingAgentsApi;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.util.StringUtil;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class OnPipelineWizardPage extends CruisePage {
    
    private CurrentPageState currentPageState;

	public OnPipelineWizardPage(ScenarioState state, UsingAgentsApi agentsApi, CruiseAgents createdAgents, Browser browser, CurrentPageState currentPageState) {
		super(state, browser);
		this.currentPageState = currentPageState;
	}

	@Override
	protected String url() {
		return Urls.urlFor("/tab/admin/pipeline");
	}
	
	public void reloadPage(){
		super.reloadPage();
	}

	public void createANewPipelineInPipelineGroup(String pipelineName, String pipelineGroup) throws Exception {
		String actualName = pipelineName + StringUtil.shortUUID();
		ElementStub pipelineNameTextbox = browser.textbox("name");
		pipelineNameTextbox.setValue(actualName);
		
		ElementStub pipelineGroupTextbox = browser.textbox("pipelineGroup");
		pipelineGroupTextbox.setValue(pipelineGroup);

		ElementStub urlTextbox = browser.textbox("url");
		urlTextbox.setValue("http://subversion.assembla.com/svn/tingtong/");
		
		browser.span("ADD THIS PIPELINE").click();
		currentPageState.currentPageIs(Page.EDIT_PIPELINE_WIZARD_GENERAL_PAGE);
		scenarioState.pushPipeline(pipelineName, actualName);		
	}

	public void verifyMessageShowsUp(final String message) throws Exception {
		final ElementStub errorElement = browser.div("error-box").in(browser.div("error-container"));
		
		Assertions.waitUntil(Timeout.TWENTY_SECONDS, new Predicate() {
			public boolean call() throws Exception {
				return errorElement.getText().contains(message);
			}

			@Override
			public String toString() {
				return "Expected error message : " + message + " not found on the page";
			}
		});	
		
	}
	
}
