package com.thoughtworks.cruise.page;

import static junit.framework.Assert.assertTrue;
import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

import com.thoughtworks.cruise.util.CommaSeparatedParams;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.ScenarioState;

public class AlreadyOnPipelinesAdminTab extends CruisePage {
	private final CurrentPageState currentPageState;

	public AlreadyOnPipelinesAdminTab(ScenarioState state, Browser browser, CurrentPageState currentPageState) {
		super(state, true, browser);
		this.currentPageState = currentPageState;
        this.currentPageState.assertCurrentPageIs(CurrentPageState.Page.EDIT_PIPELINE_GROUPS_TAB);
	}

	@Override
	protected String url() {
		return Urls.urlFor("/admin/pipelines");
	}

    @com.thoughtworks.gauge.Step("Verify pipeline groups <group> are not visible")
	public void verifyPipelineGroupsAreNotVisible(String group) throws Exception {
        assertThat(hasGroup(group), is(false));
    }

    private boolean hasGroup(String group) {
        ElementStub groupEntry = browser.heading2(group);
        return groupEntry.exists() && groupEntry.isVisible() && groupEntry.fetch("className").contains("group_name");
    }

    @com.thoughtworks.gauge.Step("Verify pipeline groups <group> are visible")
	public void verifyPipelineGroupsAreVisible(String group) throws Exception {
        assertThat(hasGroup(group), is(true));
    }

    @com.thoughtworks.gauge.Step("Verify pipelines <names> are visible")
	public void verifyPipelinesAreVisible(String names) throws Exception {
        for (String pipeline : new CommaSeparatedParams(names)) {
            ElementStub pipelineLink = pipelineLink(pipeline);
            assertThat(pipelineLink.isVisible(), is(true));
        }
    }

    private ElementStub pipelineLink(String pipeline) {
        pipeline = scenarioState.pipelineNamed(pipeline);
        return browser.link(pipeline);
    }

    @com.thoughtworks.gauge.Step("Edit pipeline <pipeline>")
	public void editPipeline(String pipeline) throws Exception {
        pipelineLink(pipeline).click();
        currentPageState.currentPageIs(CurrentPageState.Page.EDIT_PIPELINE_WIZARD_GENERAL_PAGE);
    }

    @com.thoughtworks.gauge.Step("Extract template for pipeline <pipelineName>")
	public void extractTemplateForPipeline(String pipelineName) throws Exception {
        ElementStub extractTemplate = browser.link("Extract Template").in(browser.span(Regex.wholeWord("extract_template_for_pipeline_" + scenarioState.pipelineNamed(pipelineName))));
        extractTemplate.click();
        currentPageState.currentPageIs(Page.NEW_TEMPLATE_POPUP);
    }

    @com.thoughtworks.gauge.Step("Verify that extract template is disabled for <pipeline>")
	public void verifyThatExtractTemplateIsDisabledFor(String pipeline) throws Exception {
        ElementStub span = browser.span("action_icon add_icon_disabled extract_template_for_pipeline_" + scenarioState.pipelineNamed(pipeline));
        assertTrue(span.exists());
    }

    @com.thoughtworks.gauge.Step("Delete pipeline <pipeline>")
	public void deletePipeline(String pipeline) throws Exception {
        ElementStub row = browser.row(Regex.wholeWord(scenarioState.pipelineNamed(pipeline)));
        ElementStub actionsOnPipeline = browser.cell("actions").in(row);
        browser.link("Delete").in(actionsOnPipeline).click();
        browser.submit("primary submit MB_focusable").click();
    }

    @com.thoughtworks.gauge.Step("Verify that extract template is visible and enabled for <pipelineName>")
	public void verifyThatExtractTemplateIsVisibleAndEnabledFor(String pipelineName) throws Exception {
        assertThatExtractTemplateExists(pipelineName, true);
    }

    @com.thoughtworks.gauge.Step("Verify that extract template is not visible for <pipelineName>")
	public void verifyThatExtractTemplateIsNotVisibleFor(String pipelineName) throws Exception {
        assertThatExtractTemplateExists(pipelineName, false);
    }
    
    private void assertThatExtractTemplateExists(String pipelineName, boolean exists) {
        ElementStub span = browser.span(Regex.wholeWord("extract_template_for_pipeline_" + scenarioState.pipelineNamed(pipelineName)));
        ElementStub link = browser.link("add_link").in(span);
        assertThat(link.exists(), is(exists));
    }
}
