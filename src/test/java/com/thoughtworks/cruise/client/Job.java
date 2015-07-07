package com.thoughtworks.cruise.client;

import static org.apache.commons.lang.StringUtils.equalsIgnoreCase;

public class Job {
    public static final String DEFAULT_JOB = "defaultJob";

    private final String name;
    private final String status;
    private String path;

    public Job(String name, String status, String path) {
        this.name = name;
        this.status = status;
        this.path = path;
    }

    public boolean isScheduled() {
        return equalsIgnoreCase("scheduled", status);
    }

    public boolean isCompleted() {
        return !equalsIgnoreCase("unknown", status)
                && !equalsIgnoreCase("scheduled", status)
                && !equalsIgnoreCase("assigned", status)
                && !equalsIgnoreCase("preparing", status)
                && !equalsIgnoreCase("building", status)
                && !equalsIgnoreCase("completing", status);
    }

    public boolean hasSameName(String name) {
        return equalsIgnoreCase(this.name, name);
    }

    public String getLocator() {
        return path;
    }
}
