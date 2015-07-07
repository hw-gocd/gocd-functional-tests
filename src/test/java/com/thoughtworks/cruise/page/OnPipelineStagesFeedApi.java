package com.thoughtworks.cruise.page;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.api.feeds.StagesFeedXml;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.DomUtil;
import org.dom4j.Document;
import org.dom4j.Element;
import org.hamcrest.Matchers;
import org.junit.Assert;

// JUnit Assert framework can be used for verification

public class OnPipelineStagesFeedApi {
	private final ScenarioState state;
	private final TalkToCruise talkToCruise;
	
	public OnPipelineStagesFeedApi(ScenarioState state, TalkToCruise talkToCruise) {
		this.state = state;
		this.talkToCruise = talkToCruise;
	}

	@com.thoughtworks.gauge.Step("Verify <pipelineName> is viewable")
	public void verifyIsViewable(String pipelineName) throws Exception {
		CruiseResponse response = loadStageListing(state.pipelineNamed(pipelineName));
		Assert.assertThat(response.getStatus(), Matchers.is(200));
	}

	private CruiseResponse loadStageListing(String pipelineName) {
		String pipelineUrl = Urls.urlFor(String.format("/api/pipelines/%s/stages.xml", pipelineName));
		return talkToCruise.get(pipelineUrl);
	}

	@com.thoughtworks.gauge.Step("Verify pipeline instance <expandedPipelineName> is not found")
	public void verifyPipelineInstanceIsNotFound(String expandedPipelineName) throws Exception {
		CruiseResponse response = loadStageListing(expandedPipelineName);
		Assert.assertThat(response.getStatus(), Matchers.is(404));
	}

	@com.thoughtworks.gauge.Step("Verify <pipelineName> is not viewable")
	public void verifyIsNotViewable(String pipelineName) throws Exception {
		CruiseResponse response = loadStageListing(state.pipelineNamed(pipelineName));
		Assert.assertThat(response.getStatus(), Matchers.is(401));
	}

    @com.thoughtworks.gauge.Step("Verify shows first instance of <stageName> of <pipelineName>")
	public void verifyShowsFirstInstanceOfOf(String stageName, String pipelineName) throws Exception {
        String expandedPipelineName = state.pipelineNamed(pipelineName);
        CruiseResponse response = loadStageListing(expandedPipelineName);
        Document dom = DomUtil.getDomFor(response.getBody());
        Element pipelineInstanceElement = (Element) dom.selectSingleNode(StagesFeedXml.entryTitleXpath(expandedPipelineName, 1, stageName, 1, "Passed"));
        Assert.assertThat(pipelineInstanceElement, Matchers.is(Matchers.not(Matchers.nullValue())));
        Element pipelineLink = (Element) pipelineInstanceElement.selectSingleNode("//atom:link[@rel='http://www.thoughtworks-studios.com/ns/relations/go/pipeline'][@type='application/vnd.go+xml']");
        state.knownPipelineInstanceUrl(pipelineName, pipelineLink.attribute("href"));
    }

}
