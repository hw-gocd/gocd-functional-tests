package com.thoughtworks.cruise.utils;

import java.io.Serializable;

public abstract class CommandArgument implements Serializable {
    public abstract String forCommandline();
    public abstract String forDisplay();

    public final String toString() {
        return forDisplay();
    }

    public int hashCode() {
        return this.forCommandline().hashCode();
    }

    public boolean equals(Object that) {
        if (that == null) return false;
        if (this == that) return true;
        if (that.getClass()!=this.getClass()) return false;
        return equal((CommandArgument)that);
    }

    protected boolean equal(CommandArgument that) {
        return this.forCommandline().equals(that.forCommandline());
    }

    public String replaceSecretInfo(String line) {
        if(forCommandline().length() > 0){
            line = line.replace(forCommandline(), forDisplay());
        }
        
        return line;
    }
}
