package com.thoughtworks.cruise.preconditions;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintStream;

public class NewStreamPumper {
    public static Thread pump(final InputStream inputStream, final String streamName, final PrintStream out) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                try {
                    BufferedReader sysout = new BufferedReader(new InputStreamReader(inputStream));
                    String line = null;
                    while ((line = sysout.readLine()) != null) {
                        out.println(streamName + ": " + line);
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        });
        thread.setDaemon(true);
        thread.start();

        return thread;
    }
}
