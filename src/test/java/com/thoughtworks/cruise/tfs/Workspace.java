package com.thoughtworks.cruise.tfs;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

import com.thoughtworks.xstream.annotations.XStreamAlias;
import com.thoughtworks.xstream.annotations.XStreamAsAttribute;
import com.thoughtworks.xstream.annotations.XStreamImplicit;

/**
* @understands
*/
@XStreamAlias("workspace")
public class Workspace {
    @XStreamAsAttribute
    private String name;

    @XStreamAsAttribute
    private String owner;

    @XStreamAsAttribute
    private String computer;

    @XStreamAsAttribute
    private String comment;

    @XStreamAsAttribute
    @XStreamAlias("server")
    private String url;

    @XStreamAlias("working-folder")
    @XStreamImplicit
    private List<WorkingFolder> workingFolders;


    public Workspace(String name, String owner, String computer, String comment, String url, List<WorkingFolder> workingFolders) {
        this.name = name;
        this.owner = owner;
        this.computer = computer;
        this.comment = comment;
        this.url = url;
        this.workingFolders = workingFolders;
    }

    public Workspace(String name, String owner, String computer, String comment, String url) {
        this(name, owner, computer, comment, url, new ArrayList<WorkingFolder>());
    }

    public Workspace(String workspaceName) {
        this(workspaceName, "", "", "", "");
    }

    public Workspace() {
        this("");
    }

    public boolean matchesName(String workspaceName) {
        return name != null ? name.equals(workspaceName) : workspaceName == null;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        Workspace workspace = (Workspace) o;

        if (comment != null ? !comment.equals(workspace.comment) : workspace.comment != null) {
            return false;
        }
        if (computer != null ? !computer.toLowerCase().equals(workspace.computer.toLowerCase()) : workspace.computer != null) {
            return false;
        }
        if (hasDifferentAttributes(workspace)) {
            return false;
        }
        return !(workingFolders != null ? !workingFolders.equals(workspace.workingFolders) : workspace.workingFolders != null);

    }

    private boolean hasDifferentAttributes(Workspace workspace) {
        if (name != null ? !name.equals(workspace.name) : workspace.name != null) {
            return true;
        }
        if (owner != null ? !owner.equals(workspace.owner) : workspace.owner != null) {
            return true;
        }
        if (url != null ? !url.equals(workspace.url) : workspace.url != null) {
            return true;
        }
        return false;
    }

    @Override
    public int hashCode() {
        int result = name != null ? name.hashCode() : 0;
        result = 31 * result + (owner != null ? owner.hashCode() : 0);
        result = 31 * result + (computer != null ? computer.hashCode() : 0);
        result = 31 * result + (comment != null ? comment.hashCode() : 0);
        result = 31 * result + (url != null ? url.hashCode() : 0);
        result = 31 * result + (workingFolders != null ? workingFolders.hashCode() : 0);
        return result;
    }

    @Override public String toString() {
        return "Workspace{" +
                "name='" + name + '\'' +
                ", owner='" + owner + '\'' +
                ", computer='" + computer + '\'' +
                ", comment='" + comment + '\'' +
                ", url='" + url + '\'' +
                ", workingFolder=" + workingFolders +
                '}';
    }

    public String getName() {
        return name;
    }



    public boolean hasWorkFolder(File workingDir) {
        for (WorkingFolder workingFolder : workingFolders) {
            if (workingFolder.matchesLocalDir(workingDir)) {
                return true;
            }
        }
        return false;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }

    public void setComputer(String computer) {
        this.computer = computer;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public void setUrl(String server) {
        this.url = server;
    }

    public void addWorkingFolder(WorkingFolder workingFolder) {
        this.workingFolders.add(workingFolder);
    }
    
    public List<WorkingFolder> getWorkingFolders(){
        return workingFolders;
    }
   
}
