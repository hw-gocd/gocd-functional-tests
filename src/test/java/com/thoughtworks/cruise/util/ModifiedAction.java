package com.thoughtworks.cruise.util;

public enum ModifiedAction {
    added,
    modified,
    deleted,
    unknown;

    public static ModifiedAction parseSvnAction(char action) {
        switch (action) {
            case 'A':
                return added;
            case 'M':
                return modified;
            case 'D':
                return deleted;
            default:
                return unknown;
        }
    }

    public static ModifiedAction parseP4Action(String action) {
        if ("add".equals(action))    { return ModifiedAction.added; }
        if ("edit".equals(action))   { return ModifiedAction.modified; }
        if ("delete".equals(action)) { return ModifiedAction.deleted; }
        return ModifiedAction.unknown;
    }

    public static ModifiedAction parseGitAction(char action) {
        return parseSvnAction(action);
    }
}
