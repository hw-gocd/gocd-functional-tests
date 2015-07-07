package com.thoughtworks.cruise.page;

import com.thoughtworks.cruise.util.CruiseConstants;
import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import org.apache.commons.lang.StringUtils;
import org.hamcrest.Matchers;
import org.hamcrest.core.Is;
import org.hamcrest.text.StringContains;
import org.junit.Assert;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.SahiBrowserWrapper;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.editpipelinewizard.AutoCompleteSuggestions;
import com.thoughtworks.cruise.state.ConfigState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Function;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

import static com.thoughtworks.twist.core.execution.TwistVerification.verifyEquals;
import static junit.framework.Assert.assertEquals;
import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsString;
import static org.junit.Assert.assertThat;
public abstract class CruiseAdminPage extends CruisePage{
	public CruiseAdminPage(ScenarioState scenarioState, boolean alreadyOn, Browser browser) {
		super(scenarioState, alreadyOn, browser);
	}
    
	public void assertMD5() throws Exception {
    	String md5value = scenarioState.getValueFromStore(ConfigState.md5key);
    	assertEquals(browser.hidden("config_md5").getValue(), md5value);
    }
	
	public void verifySuccessfulMergeMessageShowUp() throws Exception {
	    Assert.assertThat(message(), containsString("Saved configuration successfully. The configuration was modified by someone else, but your changes were merged successfully."));
	}
	
	protected String message() {
		return Assertions.waitFor(Timeout.TWENTY_SECONDS, new Function<String>() {
			public String call() {				
				String message = browser.byId("message_pane").getText().trim();
				if (StringUtils.isBlank(message)) {
					return null;
				}
				return message;
			}
		});
	}
}
