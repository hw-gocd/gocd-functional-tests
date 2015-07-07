package com.thoughtworks.cruise.page;

import static org.hamcrest.Matchers.is;
import static org.hamcrest.Matchers.not;
import static org.hamcrest.Matchers.nullValue;

import java.io.IOException;

import org.apache.commons.httpclient.HttpException;
import org.dom4j.Element;
import org.junit.Assert;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.DomUtil;

// JUnit Assert framework can be used for verification

public class OnConfiguredPipelineApi {
	
	private final ScenarioState state;
	private final TalkToCruise talkToCruise;
	
	public OnConfiguredPipelineApi(ScenarioState state, TalkToCruise talkToCruise) {
		this.state = state;
		this.talkToCruise = talkToCruise;
	}

	@com.thoughtworks.gauge.Step("Verify <pipelineName> is shown")
	public void verifyIsShown(String pipelineName) throws Exception {
		Element pipelineElement = getConfiguredPipelinesPage(pipelineName);
		Assert.assertThat("Pipeline element should exist", pipelineElement, is(not(nullValue())));
	}

	private Element getConfiguredPipelinesPage(String pipelineName)	throws IOException, HttpException {
		CruiseResponse response = talkToCruise.get(Urls.urlFor("/api/pipelines.xml"));
		String pipelineXpath = String.format("//pipelines/pipeline[@href='%s']", Urls.urlFor(String.format("/api/pipelines/%s/stages.xml", state.pipelineNamed(pipelineName))));
		Assert.assertThat(response.getStatus(), is(200));
		Element pipelineElement = (Element) DomUtil.getDomFor(response.getBody()).selectSingleNode(pipelineXpath);
		return pipelineElement;
	}

	@com.thoughtworks.gauge.Step("Verify <pipelineName> is not shown")
	public void verifyIsNotShown(String pipelineName) throws Exception {
		Element pipelineElement = getConfiguredPipelinesPage(pipelineName);
		Assert.assertThat(pipelineElement, is(nullValue()));
	}

	

}
