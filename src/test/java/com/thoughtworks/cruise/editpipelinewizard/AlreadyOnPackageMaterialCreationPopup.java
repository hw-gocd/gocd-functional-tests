package com.thoughtworks.cruise.editpipelinewizard;

import org.junit.Assert;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.Assertions.Predicate;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.is;

public class AlreadyOnPackageMaterialCreationPopup extends
		AlreadyOnEditMaterialPopup {
	private PackageMaterialCreator packageMaterialCreator;

	public AlreadyOnPackageMaterialCreationPopup(
			CurrentPageState currentPageState, ScenarioState scenarioState,
			Browser browser) {
		super(currentPageState, scenarioState, browser);
		packageMaterialCreator = new PackageMaterialCreator(browser, browserWrapper);
		currentPageState
				.assertCurrentPageIs(Page.EDIT_PIPELINE_WIZARD_MATERIAL_POPUP);
	}
	
	@com.thoughtworks.gauge.Step("Click save - AlreadyOnPackageMaterialCreationPopup")
	public void clickSave() throws Exception {
		browser.submit("primary finish submit MB_focusable").click();
		currentPageState
				.currentPageIs(Page.EDIT_PIPELINE_WIZARD_MATERIAL_LISTING_PAGE);
	}
	
	public void clickCancel() throws Exception {
		browser.submit("left submit close_modalbox_control MB_focusable").click();
		currentPageState
				.currentPageIs(Page.EDIT_PIPELINE_WIZARD_MATERIAL_LISTING_PAGE);
	}

	@com.thoughtworks.gauge.Step("Select repository <repositoryName>")
	public void selectRepository(String repositoryName) throws Exception {
		packageMaterialCreator.selectRepository(repositoryName);
	}

	@com.thoughtworks.gauge.Step("Select package <packageName>")
	public void selectPackage(String packageName) throws Exception {
		packageMaterialCreator.selectPackage(packageName);
	}
	
	@com.thoughtworks.gauge.Step("Verify readonly configuration for package with name <packageName> and spec <packageSpec> is displayed")
	public void verifyReadonlyConfigurationForPackageWithNameAndSpecIsDisplayed(
			String packageName, String packageSpec) throws Exception {
		packageMaterialCreator.verifyReadonlyConfigurationForPackageWithNameAndSpecIsDisplayed(packageName, packageSpec);
	}

	@com.thoughtworks.gauge.Step("Select option <option> - AlreadyOnPackageMaterialCreationPopup")
	public void selectOption(String option) throws Exception {
		packageMaterialCreator.selectOption(option);
	}

	@com.thoughtworks.gauge.Step("Enter package name <packageName> and spec <packageSpec>")
	public void enterPackageNameAndSpec(String packageName, String packageSpec) throws Exception {
		packageMaterialCreator.enterPackageNameAndSpec(packageName, packageSpec);
	}

	@com.thoughtworks.gauge.Step("Verify error message <message> is shown - Already On package Material Creation Popup")
	public void verifyErrorMessageIsShown(String message) throws Exception {
		packageMaterialCreator.verifyErrorMessageIsShown(message);
	}

	@com.thoughtworks.gauge.Step("Verify global errors has error <message>")
	public void verifyGlobalErrorsHasError(String message) throws Exception {
		packageMaterialCreator.verifyGlobalErrorsHasError(message);
	}

	@com.thoughtworks.gauge.Step("Verify missing plugin error is shown")
	public void verifyMissingPluginErrorIsShown() throws Exception {
		packageMaterialCreator.verifyMissingPluginErrorIsShown();
	}

	@com.thoughtworks.gauge.Step("Verify that save is <state>")
	public void verifyThatSaveIs(String state) throws Exception {
		packageMaterialCreator.verifyThatSaveIs(state);
	}

	@com.thoughtworks.gauge.Step("Verify radio buttons are <radioButtonState>")
	public void verifyRadioButtonsAre(String radioButtonState) {
		packageMaterialCreator.verifyRadioButtonsAre(radioButtonState);
	}

	@com.thoughtworks.gauge.Step("Verify that message <message> is shown - Already On package Material Creation Popup")
	public void verifyThatMessageIsShown(String message) {
		packageMaterialCreator.verifyThatMessageIsShown(message);
	}

	@com.thoughtworks.gauge.Step("Verify check package gives message containing <message>")
	public void verifyCheckPackageGivesMessageContaining(final String message)throws Exception {
		browser.button("check_package").click();
		Assertions.waitUntil(Timeout.TWENTY_SECONDS, new Predicate(){
			@Override
			public boolean call() throws Exception {
				String actualMessage = browser.byId("package_check_message").getText();
				return actualMessage != null && actualMessage.contains(message);
			}			
		});			
	}

	@com.thoughtworks.gauge.Step("Verify successful merge message shows up")
	public void verifySuccessfulMergeMessageShowsUp() throws Exception {
	    Assert.assertThat(message(), containsString("Saved successfully. The configuration was modified by someone else, but your changes were merged successfully."));
	}
}
