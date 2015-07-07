package com.thoughtworks.cruise.context;

import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;

public class WithNoUsers {

    private final TalkToCruise talkToCruise;

    public WithNoUsers(TalkToCruise talkToCruise) {
        this.talkToCruise = talkToCruise;
	}

	@com.thoughtworks.gauge.Step("With no users - setup")
	public void setUp() throws Exception {
	    CruiseResponse response = talkToCruise.delete(Urls.urlFor("/admin/users/delete_all"));
	    Assert.assertThat(response.getStatus(), Is.is(200));
	}
	
	@com.thoughtworks.gauge.Step("With no users - teardown")
	public void tearDown() throws Exception {
	}
}
