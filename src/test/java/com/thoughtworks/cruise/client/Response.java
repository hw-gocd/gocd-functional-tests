package com.thoughtworks.cruise.client;

public class Response {
    private int returnCode;
    private String responseBody;

    public Response(int returnCode, String responseBody) {
        this.returnCode = returnCode;
        this.responseBody = responseBody;
    }

    public int getReturnCode() {
        return returnCode;
    }

    public String getResponseBody() {
        return responseBody;
    }

    public boolean success() {
        return returnCode >= 200 && returnCode < 300;
    }
}

