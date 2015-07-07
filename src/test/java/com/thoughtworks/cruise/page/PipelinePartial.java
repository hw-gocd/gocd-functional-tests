package com.thoughtworks.cruise.page;

//import org.openqa.selenium.By;
import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.SahiBrowserWrapper;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Function;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class PipelinePartial {

	private final ScenarioState scenarioState;
	private final CruisePage page;
	private final Browser browser;

	public PipelinePartial(ScenarioState scenarioState, CruisePage page, Browser browser) {
		this.scenarioState = scenarioState;
		this.page = page;
		this.browser = browser;
	}
	
	public void verifyCannotTriggerWithOptions(){
		Assertions.assertOverTime(Timeout.TEN_SECONDS, new Function<Boolean>(){
			@Override
			public Boolean call() {
				return !new SahiBrowserWrapper(browser).isEnabled(elementTriggerWithOptions());
			}
			
		});
	}
	
	public void openTriggerWithOptions() {
		Assertions.waitUntil(Timeout.TEN_SECONDS, new Predicate() {
			@Override
			public boolean call() throws Exception {
				page.reloadPage();
			    ElementStub element = elementTriggerWithOptions();
			    if (!new SahiBrowserWrapper(browser).isEnabled(element)) {
			    	return false;
			    }
			    element.click();
				return true;
			}

		});
		Assertions.waitUntil(Timeout.TEN_SECONDS, new Predicate() {			
			@Override
			public boolean call() throws Exception {
				return browser.byId("MB_caption").getText().contains("Trigger");
			}
		});
	}

	private ElementStub elementTriggerWithOptions() {
		return browser.submit(String.format("deploy-with-options-%s", scenarioState.currentRuntimePipelineName()));
	}
}
