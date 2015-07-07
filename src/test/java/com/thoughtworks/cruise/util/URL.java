package com.thoughtworks.cruise.util;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

import org.apache.commons.httpclient.URI;

public class URL {

	private URI uri;

	public URL(String url) {
		try {
			uri = new URI(url, true);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	public void addParameter(String param, String value) {
		Map<String, String> paramToValues = parameters();
		paramToValues.put(param, value);
		setQuery(paramToValues);
	}

	private void setQuery(Map<String, String> paramToValues) {
		try {
			String query = "";
			for (Entry<String, String> entry : paramToValues.entrySet()) {
				query += "&" + entry.getKey() + "=" + entry.getValue();
			}
			uri.setQuery(query.substring(1));
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}

	private Map<String, String> parameters() {
		try {
			Map<String, String> paramToValues = new HashMap<String, String>();
			String query = uri.getQuery();
			if (query == null) {
				return paramToValues;
			}
			String[] paramValues = query.split("&");
			for (String paramValue : paramValues) {
				String[] paramAndValue = paramValue.split("=");
				paramToValues.put(paramAndValue[0], paramAndValue[1]);
			}
			return paramToValues;
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
	}
	
	@Override
	public String toString() {
		return uri.getEscapedURI();
	}
}
