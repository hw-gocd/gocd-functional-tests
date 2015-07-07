package com.thoughtworks.cruise;

public final class Regex {
    
    public static String wholeWord(String matchString) {
        return matches(String.format("\\b%s\\b", matchString));
    }

    public static String matches(String matchString) {
        return String.format("/%s/", matchString);
    }

    public static String startsWith(String matchString) {
        return matches(String.format("^%s", matchString));
    }
}