package com.thoughtworks.cruise.util.command;

import java.util.Arrays;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;

public class CompositeConsumer implements StreamConsumer {
    private List<StreamConsumer> consumers = new LinkedList<StreamConsumer>();

    /**
     * Creates a new instance of CompositeConsumer.
     */
    public CompositeConsumer(StreamConsumer... consumers) {
        this.consumers.addAll(Arrays.asList(consumers));
    }

    /** {@inheritDoc} */
    public void consumeLine(String line) {
        Iterator i = consumers.iterator();
        while (i.hasNext()) {
            ((StreamConsumer) i.next()).consumeLine(line);
        }
    }
}