package com.thoughtworks.cruise.page;

// JUnit Assert framework can be used for verification

import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.Assertions.Function;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

public class AlreadyInEnvironmentVariablesSection {

	private Browser browser;

	public AlreadyInEnvironmentVariablesSection(Browser browser) {
		this.browser = browser;
	}
	
	private ElementStub scope() {
		return browser.div("tab-content-of-env-vars");
	}

	@com.thoughtworks.gauge.Step("Add new variable")
	public void addNewVariable() throws Exception {
		addLink().click();
	}

	private ElementStub addLink() {
		return browser.link("add_item").in(browser.div("plain-text-variables"));
	}

	@com.thoughtworks.gauge.Step("For variable <index> name <name> value <value>")
	public void forVariableNameValue(Integer index, String name, String value) throws Exception {
		ElementStub nameField = nameField(index);		
		waitForElementToBeSet(nameField, name , Timeout.TEN_SECONDS);
		ElementStub valueField = valueField(index);
		waitForElementToBeSet(valueField, value , Timeout.TEN_SECONDS);
	}
	
	private Boolean waitForElementToBeSet(final ElementStub element, final String value, final Timeout timeout) {
		return Assertions.waitFor(timeout, new Function<Boolean>() {
			public Boolean call() {
				element.setValue(value);
				return element.getValue().equals(value) ? true : null;
			}
		});
	}

	private ElementStub nameField(Integer index) {
		return environmentVariablePart(index, "environment_variable_name");
	}

	private ElementStub valueField(Integer index) {
		return environmentVariablePart(index, "environment_variable_value");
	}

    private ElementStub environmentVariablePart(Integer index, String matchString) {
        return browser.textbox(Regex.wholeWord(matchString)).in(varRowByIndex(index));
    }

	private ElementStub varRowByIndex(Integer index) {
		return browser.row(index).in(browser.table("variables").in(browser.div("plain-text-variables")));
	}
	
	private ElementStub deleteButton(Integer index) {
		return browser.span("icon_remove delete_parent").in(varRowByIndex(index));
	}

	public void variableShouldHaveError(Integer index, String errorMessage) throws Exception {
		ElementStub errorSpan = browser.span("wizard_error_message").in(varRowByIndex(index));
		Assert.assertThat(errorSpan.getText(), Is.is(errorMessage));
	}

	@com.thoughtworks.gauge.Step("Finish")
	public void finish() throws Exception {
		ElementStub finish = browser.span("FINISH").in(scope()).parentNode();
		finish.click();
	}

	@com.thoughtworks.gauge.Step("Delete variable <index>")
	public void deleteVariable(Integer index) throws Exception {
		ElementStub deleteButton = deleteButton(index);
		deleteButton.click();
	}

	@com.thoughtworks.gauge.Step("Verify variable <index> has name <name> and value <value>")
	public void verifyVariableHasNameAndValue(Integer index, String name, String value) throws Exception {
		Assert.assertThat(nameField(index).getValue(), Is.is(name));
		Assert.assertThat(valueField(index).getValue(), Is.is(value));
	}
}
