package com.thoughtworks.cruise.materials;

import java.util.ArrayList;
import java.util.List;

public class Revision {
    final private String revisionNumber;
    final private String comment;
    final private String author;
    private List<String> added;
    private List<String> modified;
    private List<String> deleted;

    public Revision(String revisionNumber, String comment) {
        this(revisionNumber, null, comment, new ArrayList<String>(), new ArrayList<String>(), new ArrayList<String>());
    }

    public Revision(String revisionNumber, String author, String comment, List<String> modified, List<String> added, List<String> deleted) {
        this.revisionNumber = revisionNumber;
        this.author = author;
        this.comment = comment;
        this.added = added;
        this.modified = modified;
        this.deleted = deleted;
    }

    public boolean hasRevisionNumber(String number) {
        return revisionNumber.startsWith(number);
    }

    public boolean hasComment(String comment) {
        return this.comment.equals(comment);
    }

    public boolean was(String file, String action) {
        if (action.equals("added")) {
            return added.contains(file);
        }
        if (action.equals("modified")) {
            return modified.contains(file);
        }
        if (action.equals("deleted")) {
            return deleted.contains(file);
        }
        return false;
    }

    public String revisionNumber() {
        return revisionNumber;        
    }
    
    public String author(){
    	return author;
    }

    public void addDeletedFile(String text) {
        deleted.add(text);
    }

    public void addModifiedFile(String text) {
        modified.add(text);
    }

    public void addAddedFile(String text) {
        added.add(text);
    }
}
