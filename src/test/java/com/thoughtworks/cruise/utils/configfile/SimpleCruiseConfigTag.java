package com.thoughtworks.cruise.utils.configfile;

import java.util.HashMap;
import java.util.Iterator;
import java.util.LinkedHashMap;
import java.util.Map;

import org.dom4j.Element;
import org.dom4j.tree.DefaultElement;

public class SimpleCruiseConfigTag extends CruiseConfigTag {
    protected final String tagName;
    private final String content;
    protected Map<String, String> attributes;

    public SimpleCruiseConfigTag(String tagName) {
        this(tagName, "");
    }

    public SimpleCruiseConfigTag(String tagName, String content) {
        this(tagName, content, new HashMap<String, String>());
    }

    public SimpleCruiseConfigTag(String tagName, final String attributeName, final String attributeValue) {
        this(tagName, toMap(attributeName, attributeValue));
    }

    public SimpleCruiseConfigTag(String tagName, String content, String attributeName, String attributeValue) {
        this(tagName, content, toMap(attributeName, attributeValue));
    }

    public SimpleCruiseConfigTag(String tagName, Map<String, String> attributes) {
        this(tagName, "", attributes);
    }

    public SimpleCruiseConfigTag(String tagName, String content, Map<String, String> attributes) {
        this.tagName = tagName;
        this.content = content;
        this.attributes = attributes;
    }

    public Element convertToDomElement() {
        Element result = new DefaultElement(tagName);
        if (content.length() > 0) {
            result.setText(content);
        }
        
        for (Map.Entry<String, String> entry : attributes.entrySet()) {
            result.addAttribute(entry.getKey(), entry.getValue());
        }

        return result;
    }

    protected String startTag() {
        StringBuilder builder = new StringBuilder();
        builder.append("<").append(tagName);
        if (hasAttribute()) {
            builder.append(" ");
        }
        builder.append(generateAttributes());
        builder.append(">");
        return builder.toString();
    }

    private boolean hasAttribute() {
        return !attributes.isEmpty();
    }

    protected String endTag() {
        return "</" + tagName + ">";
    }

    protected String asString() {
        return startTag() + content + endTag() + "\n";
    }

    private String generateAttributes() {
        StringBuilder builder = new StringBuilder();
        Iterator<Map.Entry<String, String>> iterator = attributes.entrySet().iterator();
        while (iterator.hasNext()) {
            Map.Entry<String, String> attr = iterator.next();
            builder.append(attr.getKey()).append("=\"").append(attr.getValue()).append("\"");
            if (iterator.hasNext()) {
                builder.append(" ");
            }
        }
        return builder.toString();
    }

    public String toString() {
        return asString();
    }

    private static Map<String, String> toMap(String key, String value) {
        LinkedHashMap<String, String> map = new LinkedHashMap<String, String>();
        map.put(key, value);
        return map;
    }
}
