package com.thoughtworks.cruise.util;

import java.util.Date;

public interface Clock {
    Date currentTime();

    long currentTimeMillis();

    void sleepForSeconds(long seconds) throws InterruptedException;

    void sleepForMillis(long download_sleep_millis) throws InterruptedException;
}
