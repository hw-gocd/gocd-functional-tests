package com.thoughtworks.cruise.editpipelinewizard;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.page.CruisePage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.ScenarioState;

public class OnPipelineConfigurationWizard extends CruisePage {
	private final CurrentPageState currentPageState;
	
	public OnPipelineConfigurationWizard(ScenarioState scenarioState, Browser browser, CurrentPageState currentPageState){
		super(scenarioState,browser);
		this.currentPageState = currentPageState;
	}

	@Override
	protected String url() {
		return Urls.urlFor("/go/admin/pipelines/" + scenarioState.currentPipeline() + "/general");		
	}

	@com.thoughtworks.gauge.Step("Click on pipeline <pipelineName> for editing")
	public void clickOnPipelineForEditing(String pipelineName) throws Exception {
		browser.expectConfirm("/Are you sure you want to navigate away from this page/", true);
	   browser.navigateTo(Urls.urlFor("/go/admin/pipelines/" + scenarioState.pipelineNamed(pipelineName) + "/general"));	
	   currentPageState.currentPageIs(Page.EDIT_PIPELINE_WIZARD_GENERAL_PAGE);
	}

}
