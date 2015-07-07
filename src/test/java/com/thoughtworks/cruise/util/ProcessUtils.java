package com.thoughtworks.cruise.util;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.util.Arrays;

import com.thoughtworks.cruise.preconditions.NewStreamPumper;

public class ProcessUtils {
    public static String pgrep(String processPattern) {
        return run("pgrep", "-lf", processPattern).output;
    }

    public static String pkill(String processPattern) {
        return run("pkill", "-f", processPattern).output;
    }

    public static String pkillForcibly(String processPattern) {
        return run("pkill", "-9", "-f", processPattern).output;
    }

    public static boolean processWithPatternExists(String processPattern) {
        return run("pgrep", "-f", processPattern).exitValue == 0;
    }

    public static boolean waitForProcessesToExitOrTimeoutToElapse(int timeoutInMilliseconds, String processPattern) {
        long startTime = System.currentTimeMillis();

        while (System.currentTimeMillis() <= (startTime + timeoutInMilliseconds) && processWithPatternExists(processPattern)) {
            try {
                Thread.sleep(500);
            } catch (InterruptedException e) {
                throw new RuntimeException(e);
            }
        }

        return processWithPatternExists(processPattern);
    }

	public static ProcessOutput run(String... commandWithOptions) {
        if (SystemUtil.isWindows()) {
            return new ProcessOutput(0, "Did not run because OS is Windows: " + Arrays.asList(commandWithOptions));
        }

        System.out.println("Running command: [" + Arrays.asList(commandWithOptions) + "]");

        ByteArrayOutputStream out = new ByteArrayOutputStream();
        PrintStream stream = new PrintStream(out);

        try {
            ProcessBuilder processBuilder = new ProcessBuilder(commandWithOptions);
            processBuilder.redirectErrorStream(true);
            Process process = processBuilder.start();
            Thread pumpThread = NewStreamPumper.pump(process.getInputStream(), "[proc]", stream);
            process.getOutputStream().close();
            process.waitFor();
            pumpThread.join();
            return new ProcessOutput(process.exitValue(), out.toString("UTF-8"));
        } catch (Exception e) {
            return new ProcessOutput(1, "ERROR: " + e.getMessage());
        }
    }

    public static class ProcessOutput {
        private final int exitValue;
        private final String output;

        public ProcessOutput(int exitValue, String output) {
            this.exitValue = exitValue;
            this.output = output;
        }
    }
}
