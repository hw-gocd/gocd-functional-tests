package com.thoughtworks.cruise.api;

// JUnit Assert framework can be used for verification

import net.sf.sahi.client.Browser;

import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.state.ConfigState;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class UsingConfigVersioningApi {

	private ConfigState configState;

	public UsingConfigVersioningApi(ConfigState configState) {
		this.configState = configState;
	}

	@com.thoughtworks.gauge.Step("Alias current md5 as <alias>")
	public void aliasCurrentMd5As(String alias) throws Exception {
		configState.aliasCurrentAs(alias);
	}
	
	@com.thoughtworks.gauge.Step("Capture current md5")
	public void captureCurrentMd5() throws Exception {
		configState.captureCurrentMd5();
	}

	@com.thoughtworks.gauge.Step("Verify <alias> does not have <content>")
	public void verifyDoesNotHave(String alias, String content) throws Exception {
		assertConfigHasContent(alias, content, false);
	}

	@com.thoughtworks.gauge.Step("Verify <alias> has <content>")
	public void verifyHas(String alias, String content) throws Exception {
		assertConfigHasContent(alias, content, true);
	}
	
	private void assertConfigHasContent(String alias, String content, boolean hasContent) {
		String configFileContent = configState.getConfig(alias);
		Assert.assertThat(configFileContent.contains(content), Is.is(hasContent));
	}

	@com.thoughtworks.gauge.Step("Wait for config load")
	public void waitForConfigLoad() throws Exception {
		final String lastKnown = configState.lastAliased();
		Assertions.waitUntil(Timeout.TWENTY_SECONDS, new Predicate() {
			@Override
			public boolean call() throws Exception {
				String latest = configState.getConfig(ConfigState.LATEST_VERSION);
				return ! lastKnown.equals(latest);
			}
			
		});
	}
}
