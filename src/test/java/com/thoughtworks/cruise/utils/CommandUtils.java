package com.thoughtworks.cruise.utils;

import static com.thoughtworks.cruise.util.ExceptionUtils.bomb;

import java.io.BufferedReader;
import java.io.File;
import java.io.IOException;
import java.io.InputStreamReader;

public class CommandUtils {
    
    public static String exec(String... commands) {
        return exec(null, commands);
    }

    public static String exec(File workingDirectory, String... commands) {
        try {
            Process process = Runtime.getRuntime().exec(commands, null, workingDirectory);
            return captureOutput(process).toString();
        } catch (Exception e) {
            throw bomb(e);
        }
    }

    private static StringBuilder captureOutput(Process process) throws IOException, InterruptedException {
        BufferedReader output = new BufferedReader(new InputStreamReader(process.getInputStream()));
        BufferedReader error = new BufferedReader(new InputStreamReader(process.getErrorStream()));        
        StringBuilder result = new StringBuilder();
        result.append("output:\n");
        dump(output, result);
        result.append("error:\n");
        dump(error, result);
        process.waitFor();
        return result;
    }

    private static StringBuilder dump(BufferedReader reader, StringBuilder builder) throws IOException {
        String line;
        while ((line = reader.readLine()) != null) {
            builder.append(line + "\n");
        }
        reader.close();
        return builder;
    }

}
