package com.thoughtworks.cruise.page.admin;

import net.sf.sahi.client.Browser;

public interface Predicate {
	public Object invoke(Browser browser);
}
