package com.thoughtworks.cruise.util.command;

public class CheckedCommandLineException extends CruiseControlException {
    public CheckedCommandLineException(String s) {
        super(s);
    }

    public CheckedCommandLineException(String s, Throwable t) {
        super(s, t);
    }
}