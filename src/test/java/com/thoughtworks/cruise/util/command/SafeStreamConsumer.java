package com.thoughtworks.cruise.util.command;

import java.util.List;

public class SafeStreamConsumer implements StreamConsumer {
    private final StreamConsumer consumer;
    private final List<CommandArgument> arguments;

    public SafeStreamConsumer(StreamConsumer consumer, List<CommandArgument> arguments) {
        this.consumer = consumer;
        this.arguments = arguments;
    }

    public void consumeLine(String line) {
        consumer.consumeLine(replaceSecretInfo(line));
    }

    private String replaceSecretInfo(String line) {
        for (CommandArgument argument : arguments) {
            line = line.replace(argument.forCommandline(), argument.forDisplay());
        }
        return line;
    }


}
