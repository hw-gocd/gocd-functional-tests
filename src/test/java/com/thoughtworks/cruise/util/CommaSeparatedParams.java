package com.thoughtworks.cruise.util;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class CommaSeparatedParams implements Iterable<String> {

	private List<String> params = new ArrayList<String>(); 
	
	public CommaSeparatedParams(String param) {
		param = param.trim();
		String[] split = param.split(",");
		for (String string : split) {
			params.add(string.trim());
		}
	}

	@Override
	public Iterator<String> iterator() {
		return params.iterator();
	}
	
	public int size() {
	    return params.size();
	}

    public String get(int i) {
        return params.get(i);
    }
}
