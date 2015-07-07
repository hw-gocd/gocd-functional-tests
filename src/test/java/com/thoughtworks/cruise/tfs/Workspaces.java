package com.thoughtworks.cruise.tfs;

import java.util.ArrayList;
import java.util.List;

import com.thoughtworks.xstream.annotations.XStreamAlias;
import com.thoughtworks.xstream.annotations.XStreamImplicit;

/**
* @understands
*/
@XStreamAlias("workspaces")
public class Workspaces {
    @XStreamImplicit
    private List<Workspace> workspaces;

    public Workspaces(List<Workspace> workspaces) {
        this.workspaces = workspaces;
    }

    public Workspaces(){
        this(new ArrayList<Workspace>());
    }

    public boolean hasWorkspace(String workspaceName) {
        return getWorkspace(workspaceName) != null;
    }

    public void add(Workspace workspace) {
        workspaces.add(workspace);
    }

    public Workspace getWorkspace(String workspaceName) {
        if (workspaces == null) { return null; }
        for (Workspace workspace : workspaces) {
            if (workspace.matchesName(workspaceName)) {
                return workspace;
            }
        }
        return null;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        Workspaces that = (Workspaces) o;

        if (workspaces != null ? !workspaces.equals(that.workspaces) : that.workspaces != null) {
            return false;
        }

        return true;
    }

    @Override
    public int hashCode() {
        return workspaces != null ? workspaces.hashCode() : 0;
    }

    @Override public String toString() {
        return "Workspaces{" +
                "workspaces=" + workspaces +
                '}';
    }

    public List<Workspace> getWorkspaces() {
        return workspaces;
    }

    public Workspace last() {
        return workspaces.get(workspaces.size() - 1);
    }
}
