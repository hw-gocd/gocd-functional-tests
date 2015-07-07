package com.thoughtworks.cruise.api;

import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.state.ScenarioState;

public class JobDetailApi {

	protected CruiseResponse cruiseResponse;
	protected final TalkToCruise talkToCruise;
	protected String locator;
	protected final ScenarioState scenarioState;

	public JobDetailApi(TalkToCruise talkToCruise, ScenarioState scenarioState) {
		this.talkToCruise = talkToCruise;	
		this.scenarioState = scenarioState;
	}

	public void verifyReturnCodeIs(int status) {
		Assert.assertThat(cruiseResponse.getStatus(),Is.is(status));
	}

	public void forPipelineLabelStageCounterJob(String pipelineName, String pipelineLabel, String stageName, String stageCounter, String jobName) throws Exception {
		this.locator = String.format("%s/%s/%s/%s/%s", scenarioState.pipelineNamed(pipelineName), pipelineLabel, stageName, stageCounter, jobName);
	}

}
