package com.thoughtworks.cruise.tfs;

import java.io.File;

import com.thoughtworks.xstream.annotations.XStreamAlias;
import com.thoughtworks.xstream.annotations.XStreamAsAttribute;

/**
* @understands
*/
@XStreamAlias("workspace-folder")
public class WorkingFolder {
    public static final String DEPTH_FULL = "full";

    public static final String TYPE_MAP = "map";

    @XStreamAsAttribute
    @XStreamAlias("server-item")
    private String serverItem;

    @XStreamAsAttribute
    @XStreamAlias("local-item")
    private String localItem;

    @XStreamAsAttribute
    private String type;

    @XStreamAsAttribute
    private String depth;

    public WorkingFolder(String serverItem, String localItem, String type, String depth) {
        this(serverItem, localItem);
        this.type = type;
        this.depth = depth;
    }

    public WorkingFolder(String projectPath, String absolutePath) {
        this.serverItem = projectPath;
        this.localItem = absolutePath;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        WorkingFolder that = (WorkingFolder) o;

        if (hasDifferentAttributes(that)) {
            return false;
        }
        if (type != null ? !type.equals(that.type) : that.type != null) {
            return false;
        }

        return true;
    }

    private boolean hasDifferentAttributes(WorkingFolder that) {
        if (depth != null ? !depth.equals(that.depth) : that.depth != null) {
            return true;
        }
        if (localItem != null ? !localItem.equals(that.localItem) : that.localItem != null) {
            return true;
        }
        if (serverItem != null ? !serverItem.equals(that.serverItem) : that.serverItem != null) {
            return true;
        }
        return false;
    }

    @Override
    public int hashCode() {
        int result = serverItem != null ? serverItem.hashCode() : 0;
        result = 31 * result + (localItem != null ? localItem.hashCode() : 0);
        result = 31 * result + (type != null ? type.hashCode() : 0);
        result = 31 * result + (depth != null ? depth.hashCode() : 0);
        return result;
    }

    @Override public String toString() {
        return "WorkingFolder{" +
                "serverItem='" + serverItem + '\'' +
                ", localItem='" + localItem + '\'' +
                ", type='" + type + '\'' +
                ", depth='" + depth + '\'' +
                '}';
    }

    public boolean matchesLocalDir(File workingDir) {
        return localItem.equals(workingDir.getAbsolutePath());
    }
    
    public String getLocalFolder(){
        return localItem;
    }
}
