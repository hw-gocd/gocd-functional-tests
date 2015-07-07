package com.thoughtworks.cruise.util.command;

import static com.thoughtworks.cruise.util.ListUtil.join;

import java.util.ArrayList;
import java.util.List;

public class ConsoleResult {
    private int returnValue;
    private List<String> output;
    private List<String> error;
    private boolean failOnNonZeroReturn;

    public ConsoleResult(int returnValue, List<String> output, List<String> error) {
        this(returnValue, output, error, true);
    }

    public ConsoleResult(int returnValue, List<String> output, List<String> error, boolean failOnNonZeroReturn) {
        this.returnValue = returnValue;
        this.output = output;
        this.error = error;
        this.failOnNonZeroReturn = failOnNonZeroReturn;
    }

    public List<String> output() {
        return output;
    }

    public List<String> error() {
        return error;
    }

    public int returnValue() {
        return returnValue;
    }

    public String outputAsString() {
        return join(output(), "\n");
    }

    public String errorAsString() {
        return join(error(), "\n");
    }

    public boolean failed() {
        // Some git commands return non-zero return value for a "successfull" command (e.g. git config --get-regexp)
        // In such a scenario, we can't simply rely on return value to tell whether a command is successful or not
        return failOnNonZeroReturn ? returnValue() != 0 : false;
    }

    public String describe() {
        return "--OUTPUT ---\n" + outputAsString() + "\n"
                + "--- ERROR ---\n" + errorAsString() + "\n"
                + "---\n"; 
    }

    public static ConsoleResult unknownResult() {
        ArrayList<String> list = new ArrayList<String>();
        list.add("Unknown result.");
        return new ConsoleResult(-1, new ArrayList<String>(), list);
    }
}
