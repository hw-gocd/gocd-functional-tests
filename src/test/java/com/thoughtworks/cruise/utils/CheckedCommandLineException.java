package com.thoughtworks.cruise.utils;

public class CheckedCommandLineException extends CruiseControlException {
    public CheckedCommandLineException(String s) {
        super(s);
    }

    public CheckedCommandLineException(String s, Throwable t) {
        super(s, t);
    }
}