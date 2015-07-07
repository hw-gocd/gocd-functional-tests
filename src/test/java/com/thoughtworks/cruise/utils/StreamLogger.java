package com.thoughtworks.cruise.utils;

import java.io.InputStream;

import org.apache.log4j.Level;
import org.apache.log4j.Logger;

import com.thoughtworks.cruise.util.command.StreamConsumer;
import com.thoughtworks.cruise.util.command.StreamPumper;

/**
 * Logs the content of a Stream line by line.
 */
public final class StreamLogger implements StreamConsumer {
    private Logger logger;
    private Level level;

    private StreamLogger(Logger log, Level level) {
        this.logger = log;
        this.level = level;
    }

    public static StreamConsumer getInfoLogger(Logger log) {
        return new StreamLogger(log, Level.INFO);
    }

    public static StreamPumper getInfoPumper(Logger log, InputStream info) {
        return new StreamPumper(info, new StreamLogger(log, Level.INFO));
    }

    public static StreamPumper getInfoPumper(Logger log, Process process) {
        return getInfoPumper(log, process.getInputStream());
    }

    public static StreamConsumer getWarnLogger(Logger log) {
        return new StreamLogger(log, Level.WARN);
    }

    public static StreamPumper getWarnPumper(Logger log, InputStream warn) {
        return new StreamPumper(warn, new StreamLogger(log, Level.WARN));
    }

    public static StreamPumper getWarnPumper(Logger log, Process process) {
        return getWarnPumper(log, process.getErrorStream());
    }

    /** {@inheritDoc} */
    public void consumeLine(String line) {
        logger.log(level, line);
    }
}