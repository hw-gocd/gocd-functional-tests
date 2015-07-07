package com.thoughtworks.cruise.utils;

public enum Timeout {
    ZERO_SECOND(0),
    FIVE_SECONDS(5 * 1000),
    TEN_SECONDS(10 * 1000),
    NINETY_SECONDS(90 * 1000),
    TWENTY_SECONDS(20 * 1000),
    THIRTY_SECONDS(30 * 1000),
    ONE_MINUTE(60 * 1000),
    TWO_MINUTES(120 * 1000),
    THREE_MINUTES(180 * 1000),
    FIVE_MINUTES(300 * 1000), TEN_MINUTES(600 * 1000);

    private long timeout;

    private Timeout(int timeout) {
        this.timeout = timeout;
    }

    public long inMillis() {
        return timeout;
    }
}
