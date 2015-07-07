package com.thoughtworks.cruise.api;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

import com.google.gson.Gson;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.api.response.JobHistory;
import com.thoughtworks.cruise.api.response.JobInstance;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.state.ScenarioState;

public class UsingJobApi {
	private final ScenarioState state;
	private final TalkToCruise talkToCruise;

	protected UsingJobApi(ScenarioState state, TalkToCruise talkToCruise){
		this.state = state;
		this.talkToCruise = talkToCruise;
    }

	@com.thoughtworks.gauge.Step("Verify <count> instances of <pipelineName> <stageName> <jobName> <status> - Using Job Api")
	public void verifyInstancesOf(String count, String pipelineName, String stageName, String jobName, String status) {
		String actualPipelineName = state.pipelineNamed(pipelineName);

		int offset = 0;
		while (Integer.parseInt(count) - offset > 0) {
			String apiEndPoint = "/api/jobs/%s/%s/%s/history" + (offset == 0 ? "" : "/" + offset);
			int pipelineCounter = Integer.parseInt(count) - offset;
			int currentPageSize = Integer.parseInt(count) - offset > 10 ? 10 : Integer.parseInt(count) - offset;

			hitJobHistoryAPIAndVerifyResponse(actualPipelineName, stageName, jobName, status, apiEndPoint, pipelineCounter, Integer.parseInt(count), offset,
					currentPageSize);

			offset = offset + 10;
		}
	}

	private void hitJobHistoryAPIAndVerifyResponse(String actualPipelineName, String stageName, String jobName, String status, String apiEndPoint,
			int pipelineCounter, int totalInstances, int offset, int currentPageSize) {
		String url = Urls.urlFor(String.format(apiEndPoint, actualPipelineName, stageName, jobName));
		CruiseResponse response = talkToCruise.get(url);
		String historyJSONResponse = response.getBody();
		JobHistory jobHistory = new Gson().fromJson(historyJSONResponse, JobHistory.class);
		verifyPaginationForJobHistory(jobHistory, totalInstances, offset, currentPageSize);
		verifyJobHistoryResponse(actualPipelineName, stageName, jobName, status, jobHistory, pipelineCounter);
	}

	private void verifyPaginationForJobHistory(JobHistory jobHistory, int totalInstances, int offset, int currentPageSize) {
		assertThat(jobHistory.getPagination().getPageSize(), is(10));
		assertThat(jobHistory.getPagination().getTotal(), is(totalInstances));
		assertThat(jobHistory.getPagination().getOffset(), is(offset));
		assertThat(jobHistory.getJobs().size(), is(currentPageSize));
	}

	private void verifyJobHistoryResponse(String actualPipelineName, String stageName, String jobName, String status, JobHistory jobHistory, int pipelineCounter) {
		for (JobInstance jobInstance : jobHistory.getJobs()) {
			assertThat(jobInstance.getName(), is(jobName));
			assertThat(jobInstance.getResult(), is(status));
			if (status.equals("Passed") || status.equals("Failed")) {
				assertThat(jobInstance.getState(), is("Completed"));
			}

			assertThat(jobInstance.getPipelineName(), is(actualPipelineName));
			assertThat(jobInstance.getPipelineCounter(), is(pipelineCounter--));
			assertThat(jobInstance.getStageName(), is(stageName));
			assertThat(jobInstance.getStageCounter(), is("1"));
		}
	}
}
