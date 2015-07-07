package com.thoughtworks.cruise.util.command;

import static com.thoughtworks.cruise.util.ListUtil.join;

import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.concurrent.ConcurrentLinkedQueue;

import org.apache.log4j.Logger;

public class InMemoryConsumer implements StreamConsumer {
    private Queue<String> lines = new ConcurrentLinkedQueue<String>();
    private static final Logger LOG = Logger.getLogger(InMemoryConsumer.class);

    public void consumeLine(String line) {
        try {
            lines.add(line);
        } catch (RuntimeException e) {
            LOG.error("Problem consuming line [" + line + "]", e);
        }
    }

    public List<String> asList() {
        return new ArrayList<String>(lines);
    }

    public boolean contains(String message) {
        return toString().contains(message);
    }

    public String toString() {
        return join(asList(), "\n");
    }
}
