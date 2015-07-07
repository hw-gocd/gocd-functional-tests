package com.thoughtworks.cruise.utils;

public class ConsoleOutputStreamConsumer<T extends StreamConsumer, T2 extends StreamConsumer> {
    private T stdConsumer;
    private T2 errorConsumer;

    public ConsoleOutputStreamConsumer(T stdConsumer, T2 errorConsumer) {
        this.errorConsumer = errorConsumer;
        this.stdConsumer = stdConsumer;
    }

    protected T getStdConsumer() {
        return stdConsumer;
    }

    protected T2 getErrorConsumer() {
        return errorConsumer;
    }

    public void stdOutput(String line) {
        getStdConsumer().consumeLine(line);
    }

    public void errOutput(String line) {
        getErrorConsumer().consumeLine(line);
    }

}

