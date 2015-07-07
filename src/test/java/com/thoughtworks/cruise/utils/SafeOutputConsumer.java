package com.thoughtworks.cruise.utils;

import java.util.ArrayList;
import java.util.List;

public class SafeOutputConsumer extends ConsoleOutputStreamConsumer {
    private List<CommandArgument> arguments = new ArrayList<CommandArgument>();

    public SafeOutputConsumer(ConsoleOutputStreamConsumer consumer) {
        super(consumer.getStdConsumer(), consumer.getErrorConsumer());
    }

    public void addArgument(CommandArgument argument) {
        arguments.add(argument);
    }

    public void stdOutput(String line) {
        line = replaceSecretInfo(line);

        super.stdOutput(line);
    }

    public void errOutput(String line) {
        line = replaceSecretInfo(line);

        super.errOutput(line);
    }

    private String replaceSecretInfo(String line) {
        for (CommandArgument argument : arguments) {
            line = argument.replaceSecretInfo(line);
        }
        return line;
    }

    public void addArguments(List<CommandArgument> arguments) {
        this.arguments.addAll(arguments);
        }
    }
