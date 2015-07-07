package com.thoughtworks.cruise;

import java.util.ArrayList;
import java.util.List;

import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.Assertions.Predicate;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

public class SahiBrowserWrapper {
	
	private final Browser browser;

	public SahiBrowserWrapper(Browser browser) {
		this.browser = browser;
	}

	public List<ElementStub> collectIn(String type, String identifier, ElementStub inEl) {
		List<ElementStub> list = new ArrayList<ElementStub>();
		for (int i = 0; i < 100; i++) {
			ElementStub element = new ElementStub(type, browser, String.format("%s[%d]", identifier, i));
			if (inEl != null) element = element.in(inEl);
			if (!element.exists()) break;
			list.add(element);
		}
		return list;
	}
	
	public List<ElementStub> collectNear(String type, String identifier, ElementStub nearEl) {
		List<ElementStub> list = new ArrayList<ElementStub>();
		for (int i = 0; i < 100; i++) {
			ElementStub element = new ElementStub(type, browser, String.format("%s[%d]", identifier, i));
			if (nearEl != null) element = element.near(nearEl);
			if (!element.exists(true)) break;
			list.add(element);
		}
		return list;
	}

	public List<ElementStub> collect(String type, String identifier) {
		return collectIn(type, identifier, null);
	}

	public void reload() {
		browser.navigateTo(getCurrentUrl(), true);
	}

	public String getCurrentUrl() {
		return browser.fetch("top.location.href");
	}

	public boolean isEnabled(ElementStub element) {
		return element.exists() && element.fetch("disabled").equals("false");
	}

	public boolean isAutoRefresh() {
		return !getCurrentUrl().endsWith("autoRefresh=false");
	}
}
