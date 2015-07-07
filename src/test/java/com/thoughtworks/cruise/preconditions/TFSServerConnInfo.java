package com.thoughtworks.cruise.preconditions;

public class TFSServerConnInfo {
    public String serverUrl;
    public String username;
    public String password;

    public TFSServerConnInfo(String serverUrl, String username, String password) {
        this.serverUrl = serverUrl;
        this.username = username;
        this.password = password;
    }

    String loginArg() {
        return "-login:" + username + "," + password;
    }

    String serverArg() {
        return "-server:" + serverUrl;
    }
}