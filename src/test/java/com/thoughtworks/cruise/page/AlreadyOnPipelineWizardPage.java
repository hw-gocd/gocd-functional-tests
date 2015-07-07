package com.thoughtworks.cruise.page;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.util.StringUtil;

// JUnit Assert framework can be used for verification

public class AlreadyOnPipelineWizardPage extends CruisePage{

    private final CurrentPageState currentPageState;

	public AlreadyOnPipelineWizardPage(ScenarioState scenarioState, Browser browser, CurrentPageState currentPageState) {
        super(scenarioState,true, browser);
		this.currentPageState = currentPageState;
        currentPageState.assertCurrentPageIs(CurrentPageState.Page.ADD_NEW_PIPELINE_PAGE);
    }

    @Override
    protected String url() {
        return browserWrapper.getCurrentUrl();
    }

	public void verifyGroupIs(String groupName) throws Exception {
		ElementStub groupTextBox = browser.textbox("pipelineGroup");
		assertThat(groupTextBox.value(), is(groupName));
	}

	public void createPipeline(String pipelineName) throws Exception {
		String actualName = pipelineName + StringUtil.shortUUID();
		ElementStub pipelineNameTextbox = browser.textbox("name");
		pipelineNameTextbox.setValue(actualName);
		ElementStub urlTextbox = browser.textbox("url");
		urlTextbox.setValue("http://subversion.assembla.com/svn/tingtong/");
		
		browser.span("ADD THIS PIPELINE").click();
		currentPageState.currentPageIs(Page.EDIT_PIPELINE_WIZARD_GENERAL_PAGE);
		scenarioState.pushPipeline(pipelineName, actualName);		
	}
    
}

