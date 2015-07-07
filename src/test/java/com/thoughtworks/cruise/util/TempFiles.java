package com.thoughtworks.cruise.util;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.UUID;

public class TempFiles {

    private List<File> createdFiles = new ArrayList<File>();
    private Clock clock;

    private Runnable cleanupHook = new Runnable() {
        public void run() {
            cleanUp();
        }
    };

    public TempFiles() {
        this.clock = new SystemTimeClock();
        Runtime.getRuntime().addShutdownHook(new Thread(cleanupHook));
    }

    public File createFile(String fileName) throws IOException {
        File file = new File(tempFolder(), fileName);
        file.getParentFile().mkdirs();
        file.createNewFile();
        createdFiles.add(file);
        return file;
    }

    public void cleanUp() {
        for (File file : createdFiles) {
            if (file.isDirectory()) {
                FileUtil.deleteFolder(file);
            } else {
                file.delete();
            }
        }
    }

    public File mkdir(String dirName) {
        File file = new File(tempFolder(), dirName);
        file.mkdirs();
        createdFiles.add(file);
        return file;
    }

    private static File tempFolder() {
        File cruiseTmpDir = new File(System.getProperty("java.io.tmpdir"), "cruise");
        cruiseTmpDir.mkdirs();
        return cruiseTmpDir;
    }

    public File createUniqueFile(String prefix) {
        return new File(tempFolder(), prefix + "-" + UUID.randomUUID());
    }

    public File createUniqueFolder(String folder) {
        return mkdir(folder + clock.currentTimeMillis());
    }

    public void setClock(Clock clock) {
        this.clock = clock;
    }
}
