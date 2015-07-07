package com.thoughtworks.cruise.utils;

import java.io.StringReader;
import java.util.HashMap;

import org.dom4j.Document;
import org.dom4j.DocumentFactory;
import org.dom4j.io.SAXReader;

public class DomUtil {
	public static Document getDomFor(String xml) {
	    registerNamespace();
		SAXReader builder = new SAXReader();
        builder.setValidation(false);
        Document dom = null;
        try {
            dom = builder.read(new StringReader(xml));
        } catch (Exception e) {
            throw new RuntimeException("XML invalid. " + xml, e);
        }
        return dom;
	}

    private static void registerNamespace() {
        HashMap<String, String> map = new HashMap<String, String>();
        map.put("atom", "http://www.w3.org/2005/Atom");
        DocumentFactory instance = DocumentFactory.getInstance();
        instance.setXPathNamespaceURIs(map);
    }
}
