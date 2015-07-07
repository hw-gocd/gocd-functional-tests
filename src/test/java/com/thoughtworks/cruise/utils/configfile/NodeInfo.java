package com.thoughtworks.cruise.utils.configfile;

public class NodeInfo {
    private String content;
    private int startingInsertionPoint;
    private int endingInsertionPoint;

    public NodeInfo(String content, int startingInsertionPoint, int endingInsertionPoint) {
        this.content = content;
        this.startingInsertionPoint = startingInsertionPoint;
        this.endingInsertionPoint = endingInsertionPoint;
    }

    public String getContent() {
        return content;
    }

    public int getStartingInsertionPoint() {
        return startingInsertionPoint;
    }

    public int getEndingInsertionPoint() {
        return endingInsertionPoint;
    }
}
