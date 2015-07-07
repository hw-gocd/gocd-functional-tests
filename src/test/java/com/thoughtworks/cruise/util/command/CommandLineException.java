package com.thoughtworks.cruise.util.command;

public class CommandLineException extends RuntimeException {
    private final ConsoleResult result;

    public CommandLineException(String message) {
        super(message);
        this.result = ConsoleResult.unknownResult();
    }

    public CommandLineException(String message, Exception ex) {
        super(message, ex);
        this.result = ConsoleResult.unknownResult();
    }

    public CommandLineException(CommandLine command, ConsoleResult result) {
        super("Error performing command: " + command.describe() + "\n" + result.describe());
        this.result = result;
    }


    public ConsoleResult getResult() {
        return result;
    }
}