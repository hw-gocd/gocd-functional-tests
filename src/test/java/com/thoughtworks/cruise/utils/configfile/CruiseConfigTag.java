package com.thoughtworks.cruise.utils.configfile;

public abstract class CruiseConfigTag {
    protected abstract String startTag();
    protected abstract String endTag();
    protected abstract String asString();
}
