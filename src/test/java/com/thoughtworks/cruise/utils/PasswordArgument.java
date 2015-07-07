package com.thoughtworks.cruise.utils;

public class PasswordArgument extends CommandArgument {
    private String secret;

    public PasswordArgument(String secret) {
        this.secret = secret;
    }

    public String forCommandline() {
        return secret;
    }

    public String forDisplay() {
        return "******";
    }
}
