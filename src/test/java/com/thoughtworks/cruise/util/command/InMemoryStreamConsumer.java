package com.thoughtworks.cruise.util.command;

import java.util.List;

public class InMemoryStreamConsumer extends ConsoleOutputStreamConsumer<InMemoryConsumer, InMemoryConsumer> {

    public InMemoryStreamConsumer() {
        super(new InMemoryConsumer(), new InMemoryConsumer());
    }

    public String getStdError() {
        return getErrorConsumer().toString();
    }

    public String getStdOut() {
        return getStdConsumer().toString();
    }

    public String getAllOutput() {
        return getStdOut() + "\n"
                + getStdError();

    }

    public List<String> getStdLines() {
        return getStdConsumer().asList();
    }
    public List<String> getErrLines() {
        return getErrorConsumer().asList();
    }
}
