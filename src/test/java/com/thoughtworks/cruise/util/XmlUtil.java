package com.thoughtworks.cruise.util;

import java.io.StringReader;
import java.net.URISyntaxException;

import org.dom4j.Document;
import org.dom4j.DocumentException;
import org.dom4j.io.SAXReader;
import org.xml.sax.SAXException;

public class XmlUtil {
    public static Document parse(String xml) throws DocumentException, SAXException, URISyntaxException {
        SAXReader builder = new SAXReader();
        Document dom = null;
        try {
            dom = builder.read(new StringReader(xml));
        } catch (Exception e) {
            throw new RuntimeException("XML invalid. " + xml, e);
        }
        return dom;
    }
}
