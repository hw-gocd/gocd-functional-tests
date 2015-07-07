package com.thoughtworks.cruise.page;

// JUnit Assert framework can be used for verification

import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.EnvironmentState;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;

import net.sf.sahi.client.Browser;
import static junit.framework.Assert.*;

public class AlreadyOnEnvironmentPage extends OnEnvironmentPage {

	public AlreadyOnEnvironmentPage(ScenarioState scenarioState, CurrentPageState currentPageState, RepositoryState repoState, EnvironmentState envState, ScenarioHelper scenarioHelper,
			Browser browser) {
		super(scenarioState, currentPageState, repoState, envState, scenarioHelper, true, browser);
	}

	public void lookingAtEnvironment(String environmentName) throws Exception {
		super.lookingAtEnvironment(environmentName);
	}

	public void verifyMessageIsPresent(String message) {
		super.verifyMessageIsPresent(message);
	}

	public void clickAddNewEnvironmentLink() throws Exception {
		super.clickAddNewEnvironmentLink();
	}

	public void verifyEnvironmentHasInIt(String message) {
		reloadPage();
		super.verifyEnvironmentHasInIt(message);
	}

	public void verifyPipelineIsVisible(String pipelineName) throws Exception {
		super.verifyPipelineIsVisible(pipelineName);
	}
}
