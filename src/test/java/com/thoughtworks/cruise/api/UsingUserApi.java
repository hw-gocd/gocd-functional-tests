package com.thoughtworks.cruise.api;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

import org.apache.commons.httpclient.NameValuePair;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;

public class UsingUserApi {
	private TalkToCruise talkToCruise;

	public UsingUserApi(TalkToCruise talkToCruise){
		this.talkToCruise = talkToCruise;
    }

	public void disableUser(String userName) throws Exception {
		NameValuePair operation = new NameValuePair("operation", "Disable");
		NameValuePair selected = new NameValuePair("selected[]", userName);
		CruiseResponse response = talkToCruise.post(Urls.urlFor("/admin/users/operate"), operation, selected);
		assertThat(response.getStatus(), is(302));
	}

	@com.thoughtworks.gauge.Step("Attempt to delete <username> user and should return <httpStatus>")
	public void attemptToDeleteUserAndShouldReturn(String username, String httpStatus) throws Exception {
		CruiseResponse response = talkToCruise.delete(Urls.urlFor(String.format("/api/users/%s", username)));
		assertThat(response.getStatus(), is(Integer.parseInt(httpStatus)));
	}
}
