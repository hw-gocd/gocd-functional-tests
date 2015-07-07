package com.thoughtworks.cruise.page.edit;

import static junit.framework.Assert.assertFalse;
import static org.junit.Assert.assertThat;
import static org.junit.Assert.assertTrue;

import java.util.ArrayList;
import java.util.List;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import org.hamcrest.collection.IsCollectionContaining;
import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.page.CruisePage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.util.CommaSeparatedParams;

public abstract class AlreadyOnSomeCreateTemplatePopup extends CruisePage {
    private CurrentPageState currentPageState;

    public AlreadyOnSomeCreateTemplatePopup(Browser browser, ScenarioState state, CurrentPageState pageState) {
        super(state, true, browser);
        this.currentPageState = pageState;
        pageState.assertCurrentPageIs(Page.NEW_TEMPLATE_POPUP);
    }
    
    @Override
    protected String url() {
        return null;
    }

    public void save() throws Exception {
        browser.submit("SAVE").click();
    }

    public void verifyErrorMessage(String expectedMessage) throws Exception {
        ElementStub errorDiv = browser.div("form_error");
        Assert.assertThat(errorDiv.exists(), Is.is(true));
        Assert.assertThat(errorDiv.getText(), Is.is(expectedMessage));
    }

    public void enterTemplateName(String templateName) throws Exception {
        browser.textbox("pipeline[template][name]").setValue(templateName);
    }
    
    public void saveForSuccess() throws Exception {
        save();
        currentPageState.currentPageIs(Page.EDIT_TEMPLATE_PAGE);
    }

    public void selectExtractTemplateFromAExistingPipeline() throws Exception {
        browser.checkbox("pipeline[useExistingPipeline]").click();
    
    }

    public void verifyTemplateCanBeExtractedOnlyFromPipelines(String pipelineNamesAsString) throws Exception {
        List<String> pipelineNames = new ArrayList<String>();
        for (String param : new CommaSeparatedParams(pipelineNamesAsString)) {
            pipelineNames.add(scenarioState.pipelineNamed(param));
        }
        List<ElementStub> options = browserWrapper.collectIn("option", "", elementPipelinesSelectBox());
        assertThat(pipelineNames.size(), Is.is(options.size()));
        for (int i = 0; i < options.size(); i++) {
            ElementStub option = options.get(i);
            assertThat(pipelineNames,  IsCollectionContaining.hasItem(option.getText()));
        }
    }
    
    protected abstract ElementStub elementPipelinesSelectBox();

    public void selectPipeline(String pipelineName) throws Exception {
        elementPipelinesSelectBox().choose(scenarioState.pipelineNamed(pipelineName));
    }

    public void verifyExtractTemplateCheckboxIsDisabled() throws Exception {
        assertThat(browser.checkbox("pipeline_useExistingPipeline").fetch("disabled"), Is.is("true"));
    }
    
    public void verifyExtractTemplateCheckboxIsChecked() throws Exception {
        assertTrue(browser.checkbox("pipeline_useExistingPipeline").checked());
    }

    public void verifyPipelineSelectionDropdownHasValue(String pipelineName) throws Exception {
        assertThat(elementPipelinesSelectBox().value(), Is.is(scenarioState.pipelineNamed(pipelineName)));
    }

    public void verifyPipelineSelectionDropdownIsDisabled() throws Exception {
        assertThat(elementPipelinesSelectBox().fetch("disabled"), Is.is("true"));
    }

    public void verifyExtractTemplateCheckboxIsNotChecked() throws Exception {
        assertFalse(browser.checkbox("pipeline_useExistingPipeline").checked());
    }
    
}
