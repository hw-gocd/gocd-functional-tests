package com.thoughtworks.cruise.page;

// JUnit Assert framework can be used for verification

import static org.hamcrest.Matchers.is;
import java.net.URI;
import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import org.hamcrest.core.Is;
import org.hamcrest.number.IsGreaterThan;
import org.junit.Assert;

import org.hamcrest.text.StringContains;

import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

import com.thoughtworks.cruise.state.ScenarioState;

import com.thoughtworks.cruise.util.ArrayUtil;

public class AlreadyOnShowEnvironmentPage extends CruisePage {

	private String environmentName;

	public AlreadyOnShowEnvironmentPage(ScenarioState scenarioState, Browser browser, CurrentPageState currentPageState) {
		super(scenarioState, true, browser);
		currentPageState.currentPageIs(Page.ENVIONMENT_SHOW_PAGE);
	}

	@com.thoughtworks.gauge.Step("For environment <environmentName>")
	public void forEnvironment(String environmentName) throws Exception {
		String url = browser.fetch("window.top.location.href");
		URI uri = new URI(url);
		Assert.assertThat(uri.getPath(), Is.is(String.format("/go/environments/%s/show", environmentName)));
		this.environmentName = environmentName;
	}

	@com.thoughtworks.gauge.Step("Verify breadcrumbs has environment name")
	public void verifyBreadcrumbsHasEnvironmentName() throws Exception {
		ElementStub envNameInBreadcrumbs = browser.listItem("last").in(browser.list("entity_title"));
		Assert.assertThat(envNameInBreadcrumbs.getText().trim(), Is.is(environmentName));
	}

	@com.thoughtworks.gauge.Step("Verify no <sectionName> are shown")
	public void verifyNoAreShown(String sectionName) throws Exception {
		ElementStub section = browser.div(String.format("/%s/", sectionName));
		Assert.assertThat(browser.listItem("").in(section).exists(), is(false));
	}
	
	@com.thoughtworks.gauge.Step("Verify values <commaSeperatedValues> are shown in section <sectionName>")
	public void verifyValuesAreShownInSection(String commaSeperatedValues, String sectionName) throws Exception {
		ElementStub section = browser.div("added_item " + sectionName);
		String[] values = commaSeperatedValues.split(",");
		for(String expectedValue : values) {
			Assert.assertThat(browser.listItem(scenarioState.expand(expectedValue)).in(section).exists(), Is.is(true));
		}
		Assert.assertThat("must have some matchable elements for section '" + sectionName + "'", values.length, new IsGreaterThan<Integer>(0));
	}

	@Override
	protected String url() {
		return null;
	}

	@com.thoughtworks.gauge.Step("Click on edit pipelines")
	public void clickOnEditPipelines() throws Exception {
		browser.byId("edit_pipelines").click();
	}
	
	@com.thoughtworks.gauge.Step("Click on edit agents")
	public void clickOnEditAgents() throws Exception {
		browser.byId("edit_agents").click();
	}
	
	@com.thoughtworks.gauge.Step("Click on edit environment variables")
	public void clickOnEditEnvironmentVariables() throws Exception {
		browser.byId("edit_environment_variables").click();
	}

	public void verifyListHas(String section, String list) throws Exception {
		String[] names = list == null ? new String[0] : list.split(",");
		ElementStub container = browser.div("added_item added_" + section);		
		for (int i = 0; i < names.length; i++){
			Assert.assertThat(browser.listItem(names[i]).in(container).exists(), is(true)); 
		}
	}
	
	public void verifyPipelineListHas(String[] list) throws Exception {
		String[] pipelineNames = new String[list.length];
		for (int i = 0; i < list.length; i++)
			pipelineNames[i] = scenarioState.pipelineNamed(list[i]);
		verifyListHas("pipelines", ArrayUtil.join(pipelineNames, ","));
	}

	@com.thoughtworks.gauge.Step("Click on save")
	public void clickOnSave() throws Exception {
		browser.submit("primary finish submit MB_focusable").click();
	
	}

	@com.thoughtworks.gauge.Step("Verify message <message> is present")
	public void verifyMessageIsPresent(String message) {
		Assert.assertThat(browser.div("message_pane").in(browser.div("messaging_wrapper")).getText(), StringContains.containsString(message));
	}

	@com.thoughtworks.gauge.Step("Verify error message <errorMessage> is present")
	public void verifyErrorMessageIsPresent(String errorMessage) throws Exception {
		Assert.assertThat(browser.div(errorMessage).isVisible(), is(true));
	}

	@com.thoughtworks.gauge.Step("Close popup")
	public void closePopup() throws Exception {
		browser.link("Close window").click();
	}
	

}
