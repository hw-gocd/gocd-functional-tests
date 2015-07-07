package com.thoughtworks.cruise.utils.configfile;

/**
 * Understands how to read and write the content of a config file
 */
public abstract class ConfigFileContents {
    public final String read() {
        return fixSingleClosedTags(currentContents());
    }

    public abstract void write(String newContents);

    public abstract void reset();

    protected abstract String currentContents();

    private String fixSingleClosedTags(String contents) {
        return contents.replaceAll("<(\\w+)([^>]*?)\\s*/>", "<$1$2></$1>");
    }
}
