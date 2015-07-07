package com.thoughtworks.cruise.util;

import net.sf.sahi.client.ElementStub;

public class ElementUtil {
	public static String getAttribute(ElementStub element, String attributeName) {
		String elementHTML = element.fetch("outerHTML");
		return elementHTML.replaceAll("(?ms).*" + attributeName + "=\"([^\"]*)\".*", "$1");
	}
}
