package com.thoughtworks.cruise.editpipelinewizard;

import org.hamcrest.core.Is;
import org.junit.Assert;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.page.CruisePage;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.Assertions.Predicate;

public class BuildTaskPopup extends CruisePage {

    private CurrentPageState currentPageState;
    
    public BuildTaskPopup(ScenarioState scenarioState, Browser browser, CurrentPageState currentPageState) {
        super(scenarioState, true, browser);
        this.currentPageState = currentPageState;
    }

    @Override
    protected String url() {
        return null;
    }
                                            
    @com.thoughtworks.gauge.Step("Enter build file as <value>")
	public void enterBuildFileAs(final String value) throws Exception {
        enterInTextBox("task[buildFile]", value);
    }

    @com.thoughtworks.gauge.Step("Enter target as <value>")
	public void enterTargetAs(final String value) throws Exception {
        enterInTextBox("task[target]", value);
    }

    @com.thoughtworks.gauge.Step("Enter working directory as <value>")
	public void enterWorkingDirectoryAs(final String value) throws Exception {
        enterInTextBox("task[workingDirectory]", value);
    }

    @com.thoughtworks.gauge.Step("Click save - BuildTaskPopup")
	public void clickSave() throws Exception {
        browser.submit("SAVE").click();
        currentPageState.currentPageIs(Page.PIPELINE_WIZARD_JOB_EDIT_PAGE);
    }

    @com.thoughtworks.gauge.Step("Set failed runif")
	public void setFailedRunif() throws Exception {
        browser.checkbox("task[runIfConfigsFailed]").click();
    }

    @com.thoughtworks.gauge.Step("Set any runif")
	public void setAnyRunif() throws Exception {
        browser.checkbox("task[runIfConfigsAny]").click();
    }

    @com.thoughtworks.gauge.Step("Verify build file is <value>")
	public void verifyBuildFileIs(String value) throws Exception {
        Assert.assertThat(browser.textbox("task[buildFile]").value(), Is.is(value));
    }

    @com.thoughtworks.gauge.Step("Verify target is <value>")
	public void verifyTargetIs(String value) throws Exception {
        Assert.assertThat(browser.textbox("task[target]").value(), Is.is(value));    
    }

    @com.thoughtworks.gauge.Step("Verify working directory is <value>")
	public void verifyWorkingDirectoryIs(String value) throws Exception {
        Assert.assertThat(browser.textbox("task[workingDirectory]").value(), Is.is(value));
    }
    
    protected void enterInTextBox(String fieldName, String value) {
        super.enterInTextBox(fieldName, value);
    }

    @com.thoughtworks.gauge.Step("Add a <onCancelTaskType> on cancel task")
	public void addAOnCancelTask(String onCancelTaskType) throws Exception {
       browser.checkbox("task[hasCancelTask]").check();
       browser.select("task[onCancelConfig][onCancelOption]").choose(onCancelTaskType);
    }

    @com.thoughtworks.gauge.Step("Enter on cancel build file as <value>")
	public void enterOnCancelBuildFileAs(String value) throws Exception {
        enterInTextBox("task[onCancelConfig][antOnCancel][buildFile]", value);
    }

    @com.thoughtworks.gauge.Step("Enter on cancel target as <value>")
	public void enterOnCancelTargetAs(String value) throws Exception {
        enterInTextBox("task[onCancelConfig][antOnCancel][target]", value);
    }

    @com.thoughtworks.gauge.Step("Enter on cancel working directory as <value>")
	public void enterOnCancelWorkingDirectoryAs(String value) throws Exception {
        enterInTextBox("task[onCancelConfig][antOnCancel][workingDirectory]", value);
    }

    public void clickSaveInErrorCase() throws Exception {
        browser.submit("SAVE").click();
        currentPageState.currentPageIs(Page.PIPELINE_WIZARD_TASK_EDIT_POPUP);
    }

}
