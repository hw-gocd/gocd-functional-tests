package com.thoughtworks.cruise;

import java.util.ArrayList;
import java.util.List;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

public class OnPropertiesTab {

	private final List<String> properties = new ArrayList<String>();
	
	private String propertyName;

	private Browser browser;

	public OnPropertiesTab(Browser browser) {
		this.browser = browser;
	}
	
	public String exists() throws Exception {
		return new Boolean(properties.contains(propertyName)).toString();
	}

	public void setPropertyName(String propertyName) {
		this.propertyName = propertyName;
	}

	public void setUp() throws Exception {
		if (properties.isEmpty()) {
			List<ElementStub> columns = new SahiBrowserWrapper(browser).collectIn("cell", "first", browser.table("build-peroperties-table"));
			for (ElementStub webElement : columns) {
				properties.add(webElement.getText().trim());
			}
		}
		System.err.println("The properties are: " + properties);
	}

	public void tearDown() throws Exception {
	}

	@com.thoughtworks.gauge.Step("OnPropertiesTab <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Throwable {
		com.thoughtworks.twist.migration.brt.BRTMigrator brtMigrator = new com.thoughtworks.twist.migration.brt.BRTMigrator();
		try {
			brtMigrator.BRTExecutor(table, this);
		} catch (Exception e) {
			throw e.getCause();
		}
	}

}
