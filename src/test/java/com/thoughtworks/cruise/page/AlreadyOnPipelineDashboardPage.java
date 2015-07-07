package com.thoughtworks.cruise.page;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

public class AlreadyOnPipelineDashboardPage extends OnPipelineDashboardPage {

	public AlreadyOnPipelineDashboardPage(ScenarioState scenarioState, CurrentPageState currentPageState, ScenarioHelper scenarioHelper, Browser browser,
			TalkToCruise talkToCruise, Configuration configuration, RepositoryState repositoryState) {
		super(scenarioState, currentPageState, scenarioHelper, true, browser, talkToCruise, configuration, repositoryState);
		currentPageState.assertCurrentPageIs(Page.PIPELINE_DASHBOARD);
	}

	@com.thoughtworks.gauge.Step("Looking at pipeline <pipelineName> - Already On Pipeline Dashboard Page")
	public void lookingAtPipeline(String pipelineName) throws Exception {
		super.lookingAtPipeline(pipelineName);
	}

	@com.thoughtworks.gauge.Step("Verify pipeline is in group <group> - Already On Pipeline Dashboard Page")
	public void verifyPipelineIsInGroup(String group) throws Exception {
		super.verifyPipelineIsInGroup(group);
	}

	@com.thoughtworks.gauge.Step("Verify group <groupName> is not visible - Already On Pipeline Dashboard Page")
	public void verifyGroupIsNotVisible(String groupName) throws Exception {
		super.verifyGroupIsNotVisible(groupName);
	}

	@com.thoughtworks.gauge.Step("Verify group <groupName> is visible")
	public void verifyGroupIsVisible(String groupName) throws Exception {
		super.verifyGroupIsVisible(groupName);
	}

	@com.thoughtworks.gauge.Step("Turn on autoRefresh - Already On Pipeline Dashboard Page")
	public void turnOnAutoRefresh() throws Exception {
		super.turnOnAutoRefresh();
	}
	
	@com.thoughtworks.gauge.Step("Verify pipeline <pipelineName> is visible - Already On Pipeline Dashboard Page")
	public void verifyPipelineIsVisible(String pipelineName) throws Exception {
		super.verifyPipelineIsVisible(pipelineName);
	}
	
	@com.thoughtworks.gauge.Step("Verify pipeline <pipelineName> is not visible - Already On Pipeline Dashboard Page")
	public void verifyPipelineIsNotVisible(String pipelineName) throws Exception {
		super.verifyPipelineIsNotVisible(pipelineName);
	}

    @com.thoughtworks.gauge.Step("Verify stage <indexOfStage> is <stageStatus> on pipeline with label <pipelineLabel> - Already On Pipeline Dashboard Page")
	public void verifyStageIsOnPipelineWithLabel(Integer indexOfStage, String stageStatus, String pipelineLabel) throws Exception {
        super.verifyStageIsOnPipelineWithLabel(indexOfStage, stageStatus, pipelineLabel);
    }

	public void clickCompareLink() throws Exception {
		super.clickCompareLink();
	}
}
