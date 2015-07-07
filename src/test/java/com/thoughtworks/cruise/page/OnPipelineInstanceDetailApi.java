package com.thoughtworks.cruise.page;

import java.net.URI;
import java.net.URISyntaxException;

import org.dom4j.Element;
import org.hamcrest.Matchers;
import static org.hamcrest.core.IsNot.not;
import static org.hamcrest.core.IsNull.nullValue;
import org.junit.Assert;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.DomUtil;

// JUnit Assert framework can be used for verification

public class OnPipelineInstanceDetailApi {

	private final ScenarioState state;
	private final TalkToCruise talkToCruise;
	
	public OnPipelineInstanceDetailApi(ScenarioState state, TalkToCruise talkToCruise) {
		this.state = state;
		this.talkToCruise = talkToCruise;
	}

	@com.thoughtworks.gauge.Step("Verify loads <pipelineName> instance with file <fileName>")
	public void verifyLoadsInstanceWithFile(String pipelineName, String fileName)	throws Exception {
		String knownPipelineInstanceUrl = state.knownPipelineInstanceUrl(pipelineName);
		verifyUrlPatternAssumptionIsCorrect(knownPipelineInstanceUrl);
		String body = talkToCruise.get(knownPipelineInstanceUrl).getBody();
		Element pipelineElement = (Element) DomUtil.getDomFor(body).selectSingleNode(String.format("//pipeline[@name='%s']", state.pipelineNamed(pipelineName)));
		assertPipelineDetailElementComplete(pipelineElement, fileName);
		Assert.assertThat(pipelineElement, Matchers.is(Matchers.not(Matchers.nullValue())));
	}

	@com.thoughtworks.gauge.Step("Verify unauthorized to load <pipelineName>")
	public void verifyUnauthorizedToLoad(String pipelineName) throws Exception {
		String knownPipelineInstanceUrl = state.knownPipelineInstanceUrl(pipelineName);
		verifyUrlPatternAssumptionIsCorrect(knownPipelineInstanceUrl);
		CruiseResponse response = talkToCruise.get(knownPipelineInstanceUrl);
		Assert.assertThat(response.getStatus(), Matchers.is(401));
	}
	
	@com.thoughtworks.gauge.Step("Verify fails to find <pipelineName> with bad id")
	public void verifyFailsToFindWithBadId(String pipelineName) throws Exception {
		String unavailablePipelineInstanceUrl = Urls.urlFor(String.format("/api/pipelines/%s/0.xml", state.pipelineNamed(pipelineName)));
		verifyUrlPatternAssumptionIsCorrect(unavailablePipelineInstanceUrl);
		CruiseResponse response = talkToCruise.get(unavailablePipelineInstanceUrl);
		Assert.assertThat(response.getStatus(), Matchers.is(404));	
	}

	private void assertPipelineDetailElementComplete(Element pipelineElement, String fileName) {
		Assert.assertThat(pipelineElement.asXML(),pipelineElement.selectSingleNode("scheduleTime"), Matchers.is(Matchers.not(Matchers.nullValue())));
		String changesetXpath = "materials/material[@type='HgMaterial']/modifications/changeset";
		Assert.assertThat(pipelineElement.asXML(),pipelineElement.selectSingleNode(changesetXpath + "/message").getText(), Matchers.is(not(nullValue())));
		Assert.assertThat(pipelineElement.asXML(),pipelineElement.selectSingleNode(changesetXpath + "/file[contains(@name,'"+fileName+"') and @action='added']"), Matchers.is(Matchers.not(Matchers.nullValue())));
		String stageUrl = pipelineElement.selectSingleNode("stages/stage/@href").getText();
		Assert.assertThat(stageUrl.matches("^.*/api/stages/\\d+\\.xml$"), Matchers.is(true));
		Assert.assertThat(pipelineElement.asXML(),pipelineElement.selectSingleNode("approvedBy").getText(), Matchers.is("admin"));
	}

	private void verifyUrlPatternAssumptionIsCorrect(String knownPipelineInstanceUrl) {
		try {
			String path = new URI(knownPipelineInstanceUrl).getPath();
			String pattern = "^.*/api/pipelines/[^/]+/\\d+\\.xml$";
			if (!path.matches(pattern)) {
				throw new IllegalArgumentException(String.format("url given %s doesn't match pattern %s used in twist tests", knownPipelineInstanceUrl, pattern));
			}
		} catch (URISyntaxException e) {
			throw new IllegalArgumentException(e);
		}
	}
}
