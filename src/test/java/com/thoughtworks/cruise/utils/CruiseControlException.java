package com.thoughtworks.cruise.utils;

@Deprecated
public class CruiseControlException extends Exception {

    public CruiseControlException() {
        super();
    }

    public CruiseControlException(String message) {
        super(message);
    }

    public CruiseControlException(Throwable cause) {
        super(cause);
    }

    public CruiseControlException(String message, Throwable cause) {
        super(message, cause);
    }

}