package com.thoughtworks.cruise.page.edit;

import static junit.framework.Assert.assertEquals;
import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.state.ConfigState;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;

public class AlreadyOnCreateNewTemplatePopup extends AlreadyOnSomeCreateTemplatePopup {

    public AlreadyOnCreateNewTemplatePopup(Browser browser, ScenarioState state, CurrentPageState pageState) {
        super(browser, state, pageState);
    }

    protected ElementStub elementPipelinesSelectBox() {
        return browser.select("pipeline[selectedPipelineName]");
    }

    @com.thoughtworks.gauge.Step("Save")
	@Override
    public void save() throws Exception {
        // TODO Auto-generated method stub
        super.save();
    }

    @com.thoughtworks.gauge.Step("Verify error message <expectedMessage>")
	@Override
    public void verifyErrorMessage(String expectedMessage) throws Exception {
        // TODO Auto-generated method stub
        super.verifyErrorMessage(expectedMessage);
    }

    @com.thoughtworks.gauge.Step("Enter template name <templateName>")
	@Override
    public void enterTemplateName(String templateName) throws Exception {
        // TODO Auto-generated method stub
        super.enterTemplateName(templateName);
    }

    @com.thoughtworks.gauge.Step("Save for success - Already on create new template popup")
	@Override
    public void saveForSuccess() throws Exception {
        // TODO Auto-generated method stub
        super.saveForSuccess();
    }

    @com.thoughtworks.gauge.Step("Select extract template from a existing pipeline")
	@Override
    public void selectExtractTemplateFromAExistingPipeline() throws Exception {
        // TODO Auto-generated method stub
        super.selectExtractTemplateFromAExistingPipeline();
    }

    @com.thoughtworks.gauge.Step("Verify template can be extracted only from pipelines <pipelineNamesAsString>")
	@Override
    public void verifyTemplateCanBeExtractedOnlyFromPipelines(String pipelineNamesAsString) throws Exception {
        // TODO Auto-generated method stub
        super.verifyTemplateCanBeExtractedOnlyFromPipelines(pipelineNamesAsString);
    }

    @com.thoughtworks.gauge.Step("Select pipeline <pipelineName>")
	@Override
    public void selectPipeline(String pipelineName) throws Exception {
        // TODO Auto-generated method stub
        super.selectPipeline(pipelineName);
    }

    @com.thoughtworks.gauge.Step("Verify extract template checkbox is disabled")
	@Override
    public void verifyExtractTemplateCheckboxIsDisabled() throws Exception {
        // TODO Auto-generated method stub
        super.verifyExtractTemplateCheckboxIsDisabled();
    }

    @Override
    public void verifyExtractTemplateCheckboxIsChecked() throws Exception {
        // TODO Auto-generated method stub
        super.verifyExtractTemplateCheckboxIsChecked();
    }

    @Override
    public void verifyPipelineSelectionDropdownHasValue(String pipelineName) throws Exception {
        // TODO Auto-generated method stub
        super.verifyPipelineSelectionDropdownHasValue(pipelineName);
    }

    @Override
    public void verifyPipelineSelectionDropdownIsDisabled() throws Exception {
        // TODO Auto-generated method stub
        super.verifyPipelineSelectionDropdownIsDisabled();
    }

    @com.thoughtworks.gauge.Step("Verify extract template checkbox is not checked")
	@Override
    public void verifyExtractTemplateCheckboxIsNotChecked() throws Exception {
        // TODO Auto-generated method stub
        super.verifyExtractTemplateCheckboxIsNotChecked();
    }
    
    @com.thoughtworks.gauge.Step("Assert mD5 - Already on create new template popup")
	public void assertMD5() throws Exception {
    	String md5value = scenarioState.getValueFromStore(ConfigState.md5key);
    	assertEquals(browser.hidden("config_md5").getValue(), md5value);
    }
    
    @com.thoughtworks.gauge.Step("Close popup - Already on create new template popup")
	public void closePopup() throws Exception {
    	browser.link("Close window").click();
    }
    
}
