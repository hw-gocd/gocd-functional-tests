package com.thoughtworks.cruise;

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.page.OnAgentsPage;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;

public class ConfigurePipeline extends ConfigureCruiseBy {

	private String currentPipeline;

	public ConfigurePipeline(Configuration configuration, ScenarioState scenarioState, OnAgentsPage agentsPage, CruiseAgents createdAgents, RepositoryState repositoryState) {
		super(configuration, scenarioState, agentsPage, createdAgents, repositoryState);
	}

	@com.thoughtworks.gauge.Step("Looking at pipeline <pipelineName> - Configure Pipeline")
	public void lookingAtPipeline(String pipelineName) throws Exception {
		this.currentPipeline = pipelineName;
	}

	@Override
	protected String currentPipeline() {
		if (currentPipeline == null) {
			throw new RuntimeException("Must look at a pipeline before using this fixture");
		}
		return currentPipeline;
	}

	//Ugly Methods follow because Twist doesn't support inheritance :(

	public void usingConstantlyBuildingTimer() throws Exception {
		super.usingConstantlyBuildingTimer();
	}
	
	@com.thoughtworks.gauge.Step("Configure timer to trigger pipeline <minutes> minutes from now")
	public void configureTimerToTriggerPipelineMinutesFromNow(int minutes) throws Exception {
		super.configureTimerToTriggerPipelineMinutesFromNow(minutes);
	}

	@com.thoughtworks.gauge.Step("Remove timer")
	public void removeTimer() {
		super.removeTimer();
	}

	@com.thoughtworks.gauge.Step("Set run on all agents to <runOnAllAgents> for job in pipeline <jobName>")
	public void setRunOnAllAgentsToForJobInPipeline(String runOnAllAgents, String jobName) throws Exception {
		super.setRunOnAllAgentsForJobTo(currentPipeline(), jobName, Boolean.parseBoolean(runOnAllAgents));
	}

	@com.thoughtworks.gauge.Step("Set run instance count to <runInstanceCount> for job in pipeline <jobName>")
	public void setRunInstanceCountToForJobInPipeline(String runInstanceCount, String jobName) throws Exception {
		super.setRunInstanceCountForJobTo(currentPipeline(), jobName, Integer.parseInt(runInstanceCount));
	}

	@com.thoughtworks.gauge.Step("Deny one agent")
	public void denyOneAgent() throws Exception {
		super.denyFirstAgent();
	}

	@com.thoughtworks.gauge.Step("Undeny one agent")
	public void undenyOneAgent() throws Exception {
		super.undenyFirstAgent();
	}
}
