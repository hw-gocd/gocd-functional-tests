package com.thoughtworks.cruise.editpipelinewizard;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.is;

import com.thoughtworks.cruise.SahiBrowserWrapper;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

public class PackageMaterialCreator {
	private Browser browser;
	private SahiBrowserWrapper browserWrapper;
	
	public PackageMaterialCreator(Browser browser, SahiBrowserWrapper browserWrapper) {
		this.browser = browser;
		this.browserWrapper = browserWrapper;
	}
	
	public void selectRepository(String repositoryName) throws Exception {
		browser.select("repository").choose(repositoryName);
	}

	public void selectPackage(String packageName) throws Exception {
		browser.select("package").choose(packageName);
	}
	
	public void verifyReadonlyConfigurationForPackageWithNameAndSpecIsDisplayed(
			String packageName, String packageSpec) throws Exception {
		ElementStub configurationSection = browser.div("package_configuration");
		ElementStub name = browser.textbox("package_name_value").in(configurationSection);
		ElementStub specLabel = browser.label("Package Spec").in(configurationSection);	
		ElementStub spec = browser.textbox("package_PACKAGE_SPEC_value").in(configurationSection);		
		assertThat(name.exists(), is(true));		
		assertThat(name.value(), is(packageName));
		assertThat(browserWrapper.isEnabled(name), is(false));

		assertThat(specLabel.exists(), is(true));
		
		assertThat(spec.exists(), is(true));
		assertThat(spec.value(), is(packageSpec));
		assertThat(browserWrapper.isEnabled(spec), is(false));
	}

	public void selectOption(String option) throws Exception {
		browser.radio(option).click();
	}

	public void enterPackageNameAndSpec(String packageName, String packageSpec) throws Exception {
		ElementStub configurationSection = browser.div("package_configuration");
		browser.textbox("material_package_definition_name").in(configurationSection).setValue(packageName);
		browser.textbox("material_package_definition_configuration_0_configurationValue_value").in(configurationSection).setValue(packageSpec);
	}

	public void verifyErrorMessageIsShown(String message) throws Exception {
		assertThat(browser.div("form_error").getText(), is(message));
	}

	public void verifyGlobalErrorsHasError(String message) throws Exception {
		assertThat(browser.div("errors").containsText(message), is(true));
	}

	public void verifyMissingPluginErrorIsShown() throws Exception {
		assertThat(browser.div("package_configuration").containsText("Associated plugin 'missing' not found. Please contact the Go admin to install the plugin."), is(true));
	}

	public void verifyThatSaveIs(String state) throws Exception {
		boolean saveButtonState = false;
		if(state.equals("enabled")){
			saveButtonState = true;
		}
		assertThat(browserWrapper.isEnabled(browser.submit("primary finish submit MB_focusable")), is(saveButtonState));		
	}

	public void verifyRadioButtonsAre(String radioButtonState) {
		boolean isEnabled = true;
		if(radioButtonState.equals("disabled")){
			isEnabled = false;
		}
		assertThat(browserWrapper.isEnabled(browser.radio("chooseExisting")), is(isEnabled));
		assertThat(browserWrapper.isEnabled(browser.radio("addNew")), is(isEnabled));
	}

	public void verifyThatMessageIsShown(String message) {
		assertThat(browser.div("package_configuration").containsText(message), is(true));
	}
}
