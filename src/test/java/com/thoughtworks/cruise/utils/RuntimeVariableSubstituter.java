package com.thoughtworks.cruise.utils;

import com.thoughtworks.cruise.util.ExceptionUtils;

import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;



public class RuntimeVariableSubstituter {
	private static final Pattern RUNTIME_PATTERN = Pattern.compile(".*?\\$\\{(.+?)\\}.*");

    public static interface Replacer{
		String replacementFor(String variable);
	}
	
	private final Replacer replacer;
	
	public RuntimeVariableSubstituter(Replacer replacer){
		this.replacer = replacer;
	}
	
	public String replaceRuntimeVariables(String value) {
        Matcher matcher = RUNTIME_PATTERN.matcher(value);
        String replacement = value;
        while(matcher.matches()) {
            String variable = matcher.group(1);
            String varReplacement = replacer.replacementFor(variable);
            replacement = substitute(replacement, variable, varReplacement);
            ExceptionUtils.bombIfNull(replacement, String.format("replacement for '%s' could not be found in '%s'", variable, value));
            matcher = RUNTIME_PATTERN.matcher(replacement);
        }
        return replacement;
    }


    private String substitute(String value, String token, String replacement) {
        return value.replaceFirst(String.format("\\$\\{%s\\}", token), replacement);
    }

    public static void main(String[] args) {
        String quux = new RuntimeVariableSubstituter(new Replacer() {
            private Map<String, String> foo;

            {
                foo.put("foo", "bar");
                foo.put("baz", "quux");
            }

            public String replacementFor(String variable) {
                return foo.get(variable);
            }
        }).replaceRuntimeVariables("${foo}/${baz}");
        System.out.println("quux = " + quux);
    }
}