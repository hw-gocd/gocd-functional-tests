package com.thoughtworks.cruise.page.edit;

import org.hamcrest.core.Is;
import org.junit.Assert;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.page.CruisePage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

public class AlreadyOnEditTemplatePage extends CruisePage {
    
    private final CurrentPageState currentPageState;

    public AlreadyOnEditTemplatePage(ScenarioState scenarioState, Browser browser, CurrentPageState currentPageState) {
        super(scenarioState, true, browser);
        this.browser = browser;
        this.currentPageState = currentPageState;
        currentPageState.assertCurrentPageIs(Page.EDIT_TEMPLATE_PAGE); 
    }

    @Override
    protected String url() {
        return null;
    }

    @com.thoughtworks.gauge.Step("Verify template being edited is <templateName>")
	public void verifyTemplateBeingEditedIs(String templateName) throws Exception {
        Assert.assertThat(browser.div("pipeline_header").getText(), Is.is(templateName));
    }

    @com.thoughtworks.gauge.Step("Open stages tab")
	public void openStagesTab() throws Exception {
        browser.link("Stages").click();
        currentPageState.currentPageIs(Page.EDIT_PIPELINE_WIZARD_STAGES_PAGE);
    }

	@com.thoughtworks.gauge.Step("Verify template name <templateName> cannot be edited")
	public void verifyTemplateNameCannotBeEdited(String templateName) throws Exception {
		Assert.assertThat(browser.textbox("template_name").fetch("disabled"), Is.is("true"));
	}
}
