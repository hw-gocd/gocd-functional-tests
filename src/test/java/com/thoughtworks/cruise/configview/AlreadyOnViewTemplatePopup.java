package com.thoughtworks.cruise.configview;

import static junit.framework.Assert.assertEquals;
import junit.framework.Assert;
import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.editpipelinewizard.AlreadyOnEditPipelineWizardPage;
import com.thoughtworks.cruise.page.CruisePage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

public class AlreadyOnViewTemplatePopup  extends AlreadyOnEditPipelineWizardPage {

	public AlreadyOnViewTemplatePopup(CurrentPageState currentPageState,
            ScenarioState scenarioState, Browser browser) {
        super(currentPageState, scenarioState, browser);
        currentPageState.assertCurrentPageIs(Page.VIEW_TEMPLATE_POPUP);
    }

	@Override
	protected String url() {
		return null;
	}

	@com.thoughtworks.gauge.Step("Verify template name is <template_name>")
	public void verifyTemplateNameIs(String template_name) throws Exception {
		ElementStub title = browser.byId("MB_caption");
		Assert.assertEquals(title.text(), template_name);
	}
	
	@com.thoughtworks.gauge.Step("Close popup - Already on view template popup")
	public void closePopup() throws Exception {
		browser.link("Close window").click();
	}

	@com.thoughtworks.gauge.Step("Verify clicking on stage <stageName> which is stage <stageNumberInPipeline> of the template shows the correct stage on right pane")
	public void verifyClickingOnStageWhichIsStageOfTheTemplateShowsTheCorrectStageOnRightPane(
			String stageName, String stageNumberInPipeline) throws Exception {
		browser.link(stageName).click();
		verifyStageShownOnRightPaneIsCorrect(stageName, stageNumberInPipeline);
	
	}

	@com.thoughtworks.gauge.Step("Verify clicking on job <jobName> which is job <jobNumberInStageInTemplate> in stage <stageName> which is stage <stageNumberInTemplate> of the template shows the correct job on the right pane")
	public void verifyClickingOnJobWhichIsJobInStageWhichIsStageOfTheTemplateShowsTheCorrectJobOnTheRightPane(
			String jobName, String jobNumberInStageInTemplate, String stageName, String stageNumberInTemplate)
			throws Exception {
		browser.link(jobName).click();
		ElementStub elementContainingJobName = browser.heading3(Regex.wholeWord("entity_title")).in(browser.div("definition_view_stage_" + stageNumberInTemplate + "_job_" + jobNumberInStageInTemplate));
		String jobNameShowedInRightPane = elementContainingJobName.text();
		assertEquals(stageName + " " + jobName, jobNameShowedInRightPane);	
	}
	
	@com.thoughtworks.gauge.Step("Verfiy clicking on breadcrumb for job number <jobNumberInStage> for stage <stageName> which is stage <stageNumberInTemplate> of template goes back to stage details")
	public void verfiyClickingOnBreadcrumbForJobNumberForStageWhichIsStageOfTemplateGoesBackToStageDetails(
			String jobNumberInStage, String stageName, Integer stageNumberInTemplate) throws Exception {
		browser.link(stageName).in(browser.heading3(Regex.wholeWord("entity_title")).in(browser.div("definition_view_stage_" + stageNumberInTemplate + "_job_" + jobNumberInStage)));
		verifyStageShownOnRightPaneIsCorrect(stageName, stageNumberInTemplate.toString());	
	}
	
	private void verifyStageShownOnRightPaneIsCorrect(String stageName,
			String stageNumberInPipeline) {
		ElementStub elementContainingStageName = browser.heading3(Regex.wholeWord("entity_title")).in(browser.div("definition_view_stage_"+ stageNumberInPipeline));
		String stageNameShowedInRightPane = elementContainingStageName.text();
		assertEquals(stageName, stageNameShowedInRightPane);
	}
}
