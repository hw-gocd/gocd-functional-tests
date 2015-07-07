package com.thoughtworks.cruise.api;

import org.apache.commons.httpclient.HttpStatus;
import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;
import com.thoughtworks.cruise.state.CurrentUsernameProvider;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;

public class UsingBackupServerApi {
	
	private ScenarioState state;
	private CruiseResponse cruiseResponse;
	
	protected UsingBackupServerApi(ScenarioState state, RepositoryState repositoryState) {
		this.state = state;
	}

	@com.thoughtworks.gauge.Step("Take backup as <userName>")
	public void takeBackupAs(final String userName) throws Exception {
		String url = Urls.urlFor(String.format("/api/admin/start_backup"));
		System.err.println("posting to " + url);
		
		TalkToCruise talkToCruise = new TalkToCruise(new CurrentUsernameProvider() {
			@Override
			public String loggedInUser() {
				return userName;
			}
		});
		
		cruiseResponse = talkToCruise.post(url);
	}

	@com.thoughtworks.gauge.Step("Verify backup is successful")
	public void verifyBackupIsSuccessful(){
				Assert.assertThat(cruiseResponse.isSuccess(), Is.is(true));
	}
	
	@com.thoughtworks.gauge.Step("Verify user is not authorized to take backups")
	public void verifyUserIsNotAuthorizedToTakeBackups(){
		Assert.assertThat(cruiseResponse.isForbidden(), Is.is(true));
	}

}
