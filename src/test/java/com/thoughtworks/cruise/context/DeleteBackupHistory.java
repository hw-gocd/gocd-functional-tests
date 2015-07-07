package com.thoughtworks.cruise.context;

// JUnit Assert framework can be used for verification

import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.state.ScenarioState;

public class DeleteBackupHistory {

	private final ScenarioState state;

	public DeleteBackupHistory(ScenarioState state) {
		this.state = state;
	}

	@com.thoughtworks.gauge.Step("Delete backup history - setup")
	public void setUp() throws Exception {
		deleteAllBackups();
	}

	private void deleteAllBackups() {
		CruiseResponse response = new TalkToCruise(state).delete(Urls.deleteAllBackupExtries());
		Assert.assertThat(response.isSuccess(), Is.is(true));
	}

	@com.thoughtworks.gauge.Step("Delete backup history - teardown")
	public void tearDown() throws Exception {
		deleteAllBackups();
	}
}
