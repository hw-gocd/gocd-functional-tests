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

public class UsingCommandSnippetCacheApi {
	
	private ScenarioState state;
	private CruiseResponse cruiseResponse;
	
	protected UsingCommandSnippetCacheApi(ScenarioState state) {
		this.state = state;
	}

	@com.thoughtworks.gauge.Step("Reload cache as <userName>")
	public void reloadCacheAs(final String userName) throws Exception {
		String url = Urls.urlFor("/api/admin/command-repo-cache/reload");
		System.err.println("posting to " + url);
		
		TalkToCruise talkToCruise = new TalkToCruise(new CurrentUsernameProvider() {
			@Override
			public String loggedInUser() {
				return userName;
			}
		});
		
		cruiseResponse = talkToCruise.post(url);
	}

	@com.thoughtworks.gauge.Step("Verify reload was successful")
	public void verifyReloadWasSuccessful(){
				Assert.assertThat(cruiseResponse.isSuccess(), Is.is(true));
	}
	
	@com.thoughtworks.gauge.Step("Verify user is not authorized to reload cache")
	public void verifyUserIsNotAuthorizedToReloadCache(){
		Assert.assertThat(cruiseResponse.isForbidden(), Is.is(true));
	}

}
