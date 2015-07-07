package com.thoughtworks.cruise.api;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.httpclient.NameValuePair;
import org.hamcrest.Matchers;
import org.hamcrest.core.Is;
import org.junit.Assert;

import com.google.gson.Gson;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.api.response.JobHistoryItem;
import com.thoughtworks.cruise.api.response.PipelineHistory;
import com.thoughtworks.cruise.api.response.PipelineInstance;
import com.thoughtworks.cruise.api.response.StageHistoryItem;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.materials.Repository;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

public class UsingPipelineApi {
	private String scheduleUrl;
	private final ScenarioState state;
	private final TalkToCruise talkToCruise;
    private RepositoryState repositoryState;
    private Map<String, String> revisions;
    private Map<String, String> variables;
	private String pipelineName;
	
	protected UsingPipelineApi(ScenarioState state, TalkToCruise talkToCruise, RepositoryState repositoryState){
		this.state = state;
		this.talkToCruise = talkToCruise;
        this.repositoryState = repositoryState;
    }

    @com.thoughtworks.gauge.Step("Using <which> last revision of <materialName>")
	public void usingLastRevisionOf(String which, String materialName) throws Exception {
        String commit = repositoryState.commitRevision(which, materialName, state.pipelineNamed(pipelineName));
        usingRevisionOf(commit, materialName);
    }
    

    @com.thoughtworks.gauge.Step("For pipeline <pipelineName> - Using pipeline api")
	public void forPipeline(String pipelineName) throws Exception {
		this.pipelineName = pipelineName;
		forPipelineNamed(state.pipelineNamed(pipelineName));		
	}

	@com.thoughtworks.gauge.Step("Schedule should return code <code>")
	public void scheduleShouldReturnCode(Integer code) throws Exception {		
		CruiseResponse response = schedulePipeline();
		Assert.assertThat("Schedule failed " + response.getBody(), response.getStatus(), Is.is(code));
	}
	
	@com.thoughtworks.gauge.Step("Schedule should fail with <code> and message <bodyFragment>")
	public void scheduleShouldFailWithAndMessage(Integer code, String bodyFragment) throws Exception {      
        CruiseResponse response = schedulePipeline();
        Assert.assertThat("Schedule failed " + response.getBody(), response.getStatus(), Is.is(code));
        Assert.assertThat(bodyFragment, Matchers.containsString(bodyFragment));
    }

    private CruiseResponse schedulePipeline() {
        ArrayList<NameValuePair> params = new ArrayList<NameValuePair>();		
		addParams(params,revisions, "materials");
		addParams(params,variables, "variables");		
		CruiseResponse response = talkToCruise.post(scheduleUrl, params);
        return response;
    }

	private void addParams(ArrayList<NameValuePair> params,Map<String, String> map, String paramPrefix) {		
		for(String key : map.keySet()){
			params.add(new NameValuePair(String.format("%s[%s]",paramPrefix,key), map.get(key)));
		}
	}
	
	public void unlockShouldReturn(String pipelineName, Integer code, String shouldHaveMessage) throws Exception {
		String url = Urls.urlFor(String.format("/api/pipelines/%s/releaseLock", pipelineName));
		CruiseResponse response = talkToCruise.post(url);
		Assert.assertThat(response.getBody(), Matchers.containsString(shouldHaveMessage));
		Assert.assertThat(response.getStatus(), Matchers.is(code));
	}

	public void waitUntilUnlockReturns(String pipelineName, final Integer code, final String shouldHaveMessage) throws Exception {
		final String url = Urls.urlFor(String.format("/api/pipelines/%s/releaseLock", pipelineName));
		Assertions.waitUntil(Timeout.TWENTY_SECONDS, new Predicate() {
			
			@Override
			public boolean call() throws Exception {
				CruiseResponse response = talkToCruise.post(url);
				return response.getBody().contains(shouldHaveMessage) && response.getStatus() == code;
			}
		});
	}
	
	@com.thoughtworks.gauge.Step("For pipeline named <runtimePipelineName>")
	public void forPipelineNamed(String runtimePipelineName) throws Exception {
		this.scheduleUrl = Urls.urlFor(String.format("/api/pipelines/%s/schedule",runtimePipelineName));
		this.revisions = new HashMap<String,String>();
		this.variables = new HashMap<String,String>();
	}

	@com.thoughtworks.gauge.Step("Using <revision> revision of <material>")
	public void usingRevisionOf(String revision, String material) throws Exception {
		this.revisions.put(state.expand(material), state.expand(revision));		
	}
	
	@com.thoughtworks.gauge.Step("Using latest revision of material <materialName> for pipeline <pipelineName>")
	public void usingLatestRevisionOfMaterialForPipeline(String materialName, String pipelineName) throws Exception {
		Repository repo = repositoryState.getRepoByMaterialName(state.pipelineNamed(pipelineName), materialName);
		String revisionNumber = repo.latestRevision().revisionNumber();
		this.revisions.put(state.expand(materialName), state.expand(revisionNumber));
	}
	
	@com.thoughtworks.gauge.Step("With variable <name> set to <value>")
	public void withVariableSetTo(String name, String value) throws Exception {
		this.variables.put(name, value);
	}

	public void usingStageOfUpstreamPipelineWithMaterialNameAndCounter(String stageName,String pipelineName,String materialName, Integer counter)
			throws Exception {
		String actualPipelineName = state.pipelineNamed(pipelineName);
		usingRevisionOf(String.format("%s/%s/%s/1", actualPipelineName, counter, stageName), materialName);
	}

	@com.thoughtworks.gauge.Step("Using stage <stageName> of upstream pipeline <pipelineName> with counter <counter>")
	public void usingStageOfUpstreamPipelineWithCounter(String stageName,String pipelineName,Integer counter) throws Exception {
		usingStageOfUpstreamPipelineWithMaterialNameAndCounter(stageName,pipelineName,state.pipelineNamed(pipelineName),counter);
	}

	@com.thoughtworks.gauge.Step("Verify unauthorized to unlock <pipelineName>")
	public void verifyUnauthorizedToUnlock(String pipelineName) throws Exception {
		unlockShouldReturn(state.pipelineNamed(pipelineName), 401, "user does not have operate permission on the pipeline");
	}

	@com.thoughtworks.gauge.Step("Verify unlocking <pipelineName> is not acceptable because <shouldHaveMessage>")
	public void verifyUnlockingIsNotAcceptableBecause(String pipelineName, String shouldHaveMessage) throws Exception {
		unlockShouldReturn(state.pipelineNamed(pipelineName), 406, shouldHaveMessage);
	}

	@com.thoughtworks.gauge.Step("Verify unlocking <litteralPipelineName> fails as pipeline is not found")
	public void verifyUnlockingFailsAsPipelineIsNotFound(String litteralPipelineName) throws Exception {
		unlockShouldReturn(litteralPipelineName, 404, String.format("pipeline name %s is incorrect", litteralPipelineName));
	}

	@com.thoughtworks.gauge.Step("Verify can unlock <pipelineName>")
	public void verifyCanUnlock(String pipelineName) throws Exception {
		String actualPipelineName = state.pipelineNamed(pipelineName);
		waitUntilUnlockReturns(actualPipelineName, 200, String.format("pipeline lock released for %s", actualPipelineName));
	}

	@com.thoughtworks.gauge.Step("Unlock <pipelineName>")
	public void unlock(String pipelineName) throws Exception {
		String actualPipelineName = state.pipelineNamed(pipelineName);
		unlockShouldReturn(actualPipelineName, 200, String.format("pipeline lock released for %s", actualPipelineName));
	}

	@com.thoughtworks.gauge.Step("Using remembered revision <revisionAlias> for material <materialName>")
	public void usingRememberedRevisionForMaterial(String revisionAlias, String materialName) throws Exception {
		usingRevisionOf(repositoryState.getRevisionFromAlias(revisionAlias), state.expand(materialName));
	}

    @com.thoughtworks.gauge.Step("Verify card activity between pipeline <pipelineName> counters <fromCounter> and <toCounter> is <cards> with show _ bisect <showBisect>")
	public void verifyCardActivityBetweenPipelineCountersAndIsWithShow_Bisect(String pipelineName, Integer fromCounter, Integer toCounter,
            String cards, Boolean showBisect) throws Exception {
        String url = Urls.urlFor(String.format("/api/card_activity/%s/%s/to/%s", state.pipelineNamed(pipelineName), fromCounter, toCounter));
        CruiseResponse response = talkToCruise.get(url, new NameValuePair("show_bisect", showBisect.toString()));
        Assert.assertThat(response.getBody(), Matchers.containsString(cards));
        Assert.assertThat(response.getStatus(), Matchers.is(200));
    }

	@com.thoughtworks.gauge.Step("Attempt to pause pipline <pipelineName> with cause <cause> and should return with http status <returnCode>")
	public void attemptToPausePiplineWithCauseAndShouldReturnWithHttpStatus(String pipelineName, String cause, Integer returnCode) throws Exception {
		CruiseResponse response = pauseApiCall(state.pipelineNamed(pipelineName), cause);
		assertThat(response.getStatus(), is(returnCode));
	}

	@com.thoughtworks.gauge.Step("Attempt to unpause pipeline <pipelineName> and should return with http status <returnCode>")
	public void attemptToUnpausePipelineAndShouldReturnWithHttpStatus(String pipelineName, Integer returnCode) throws Exception {
		CruiseResponse response = unpauseApiCall(state.pipelineNamed(pipelineName));
		assertThat(response.getStatus(), is(returnCode));
	}
	
	private CruiseResponse pauseApiCall(String actualPipelineName, String cause) {
		String url = Urls.urlFor(String.format("/api/pipelines/%s/pause", actualPipelineName));
		CruiseResponse response = talkToCruise.post(url, new NameValuePair("pauseCause", cause));
		return response;
	}

	private CruiseResponse unpauseApiCall(String actualPipelineName) {
		String url = Urls.urlFor(String.format("/api/pipelines/%s/unpause", actualPipelineName));
		CruiseResponse response = talkToCruise.post(url, new NameValuePair());
		return response;
	}

	@com.thoughtworks.gauge.Step("Attempt to pause non existent pipline <pipelineName> with cause <cause> and should return with http status <returnCode>")
	public void attemptToPauseNonExistentPiplineWithCauseAndShouldReturnWithHttpStatus(String pipelineName, String cause, Integer returnCode) throws Exception {
		CruiseResponse response = pauseApiCall(pipelineName, cause);
		assertThat(response.getStatus(), is(returnCode));
	}

	@com.thoughtworks.gauge.Step("Attempt to unpause non existent pipline <piplineName> and should return with http status <returnCode>")
	public void attemptToUnpauseNonExistentPiplineAndShouldReturnWithHttpStatus(String piplineName, Integer returnCode) throws Exception {
		CruiseResponse response = unpauseApiCall(pipelineName);
		assertThat(response.getStatus(), is(returnCode));
	}
	
	@com.thoughtworks.gauge.Step("Attempt to get scheduled list of jobs should return with status <returnCode>")
	public void attemptToGetScheduledListOfJobsShouldReturnWithStatus(Integer returnCode) throws Exception {		
		String url = Urls.urlFor(String.format("/api/jobs/scheduled.xml"));
		CruiseResponse response = talkToCruise.get(url);
		Assert.assertThat(response.getStatus(), Is.is(returnCode));
	}

	@com.thoughtworks.gauge.Step("Verify <count> instances of <pipelineName> <stageName> <jobName> <status>")
	public void verifyInstancesOf(String count, String pipelineName, String stageName, String jobName, String status) {
		String actualPipelineName = state.pipelineNamed(pipelineName);

		int offset = 0;
		while (Integer.parseInt(count) - offset > 0) {
			String apiEndPoint = "/api/pipelines/%s/history" + (offset == 0 ? "" : "/" + offset);
			int pipelineCounter = Integer.parseInt(count) - offset;
			int currentPageSize = Integer.parseInt(count) - offset > 10 ? 10 : Integer.parseInt(count) - offset;

			hitPipelineHistoryAPIAndVerifyResponse(actualPipelineName, stageName, jobName, status, apiEndPoint, pipelineCounter, Integer.parseInt(count),
					offset, currentPageSize);

			offset = offset + 10;
		}
	}

	@com.thoughtworks.gauge.Step("Verify <pipelineCounter> instance of <pipelineName> <stageName> <jobName> <status>")
	public void verifyInstanceOf(String pipelineCounter, String pipelineName, String stageName, String jobName, String status) {
		String actualPipelineName = state.pipelineNamed(pipelineName);
		String apiEndPoint = "/api/pipelines/%s/instance/%d";
		hitPipelineInstanceAPIAndVerifyResponse(actualPipelineName, stageName, jobName, status, apiEndPoint, Integer.parseInt(pipelineCounter));
	}

	private void hitPipelineHistoryAPIAndVerifyResponse(String actualPipelineName, String stageName, String jobName, String status, String apiEndPoint,
			int pipelineCounter, int totalInstances, int offset, int currentPageSize) {
		String url = Urls.urlFor(String.format(apiEndPoint, actualPipelineName));
		CruiseResponse response = talkToCruise.get(url);
		String historyJSONResponse = response.getBody();
		PipelineHistory pipelineHistory = new Gson().fromJson(historyJSONResponse, PipelineHistory.class);
		verifyPaginationForPipelineHistory(pipelineHistory, totalInstances, offset, currentPageSize);
		verifyPipelineHistoryResponse(actualPipelineName, stageName, jobName, status, pipelineHistory, pipelineCounter);
	}

	private void hitPipelineInstanceAPIAndVerifyResponse(String actualPipelineName, String stageName, String jobName, String status, String apiEndPoint, int pipelineCounter) {
		String url = Urls.urlFor(String.format(apiEndPoint, actualPipelineName, pipelineCounter));
		CruiseResponse response = talkToCruise.get(url);
		String instanceJSONResponse = response.getBody();
		PipelineInstance pipelineInstance = new Gson().fromJson(instanceJSONResponse, PipelineInstance.class);
		verifyPipelineInstanceResponse(actualPipelineName, stageName, jobName, status, pipelineCounter, pipelineInstance);
	}

	private void verifyPaginationForPipelineHistory(PipelineHistory pipelineHistory, int totalInstances, int offset, int currentPageSize) {
		assertThat(pipelineHistory.getPagination().getPageSize(), is(10));
		assertThat(pipelineHistory.getPagination().getTotal(), is(totalInstances));
		assertThat(pipelineHistory.getPagination().getOffset(), is(offset));
		assertThat(pipelineHistory.getPipelines().size(), is(currentPageSize));
	}

	private void verifyPipelineHistoryResponse(String actualPipelineName, String stageName, String jobName, String status, PipelineHistory pipelineHistory,
			int pipelineCounter) {
		for (PipelineInstance pipelineInstance : pipelineHistory.getPipelines()) {
			verifyPipelineInstanceResponse(actualPipelineName, stageName, jobName, status, pipelineCounter--, pipelineInstance);
		}
	}

	private void verifyPipelineInstanceResponse(String actualPipelineName, String stageName, String jobName, String status,
			int pipelineCounter, PipelineInstance pipelineInstance) {
		assertThat(pipelineInstance.getName(), is(actualPipelineName));
		assertThat(pipelineInstance.getCounter(), is(pipelineCounter));

		StageHistoryItem stageHistoryItem = pipelineInstance.getStages().get(0);
		assertThat(stageHistoryItem.getName(), is(stageName));
		assertThat(stageHistoryItem.getCounter(), is("1"));
		assertThat(stageHistoryItem.getResult(), is(status));

		JobHistoryItem jobHistoryItem = stageHistoryItem.getJobs().get(0);
		assertThat(jobHistoryItem.getName(), is(jobName));
		assertThat(jobHistoryItem.getResult(), is(status));
		if (status.equals("Passed") || status.equals("Failed")) {
			assertThat(jobHistoryItem.getState(), is("Completed"));
		}
	}
}
