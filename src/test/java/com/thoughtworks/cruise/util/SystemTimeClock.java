package com.thoughtworks.cruise.util;

import java.io.Serializable;
import java.util.Date;

public class SystemTimeClock implements Clock, Serializable {
    public Date currentTime() {
        return new Date();
    }

    public long currentTimeMillis() {
        return System.currentTimeMillis();
    }

    public void sleepForSeconds(long seconds) throws InterruptedException {
        sleepForMillis(seconds * 1000);
    }

    public void sleepForMillis(long millis) throws InterruptedException {
        Thread.sleep(millis);
    }
}
