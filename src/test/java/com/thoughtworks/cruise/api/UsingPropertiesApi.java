package com.thoughtworks.cruise.api;

import org.apache.commons.httpclient.NameValuePair;
import org.hamcrest.Matchers;
import org.junit.Assert;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.state.ScenarioState;

public class UsingPropertiesApi extends JobDetailApi {
	
	public UsingPropertiesApi(TalkToCruise talkToCruise, ScenarioState scenarioState) {		
		super(talkToCruise, scenarioState);
	}

	private String propertyUrl(String property) {
		return Urls.urlFor(String.format("/properties/%s/%s", locator, property));
	}
	
	@com.thoughtworks.gauge.Step("Set value <value> in property <property>")
	public void setValueInProperty(String value, String property) throws Exception {
		cruiseResponse = talkToCruise.post(propertyUrl(property), new NameValuePair("value", value));
	}

	@com.thoughtworks.gauge.Step("Verify return code is <status> - Using Properties Api")
	public void verifyReturnCodeIs(int status) {
		super.verifyReturnCodeIs(status);
	}

	@com.thoughtworks.gauge.Step("For pipeline <pipelineName> label <pipelineLabel> stage <stageName> counter <stageCounter> job <jobName> - Using Properties Api")
	public void forPipelineLabelStageCounterJob(String pipelineName, String pipelineLabel, String stageName, String stageCounter, String jobName) throws Exception {
		super.forPipelineLabelStageCounterJob(pipelineName, pipelineLabel, stageName, stageCounter, jobName);
	}

	@com.thoughtworks.gauge.Step("Verify property <property> has value <value>")
	public void verifyPropertyHasValue(String property, String value) throws Exception {
		cruiseResponse = talkToCruise.get(propertyUrl(property));
		Assert.assertThat(cruiseResponse.getBody(), Matchers.is(property + "\n" + value + "\n"));
	}

	@com.thoughtworks.gauge.Step("Verify property <property> does not exist")
	public void verifyPropertyDoesNotExist(String property) throws Exception {
		cruiseResponse = talkToCruise.get(propertyUrl(property));
		Assert.assertThat(cruiseResponse.getStatus(), Matchers.is(404));
	}
}
