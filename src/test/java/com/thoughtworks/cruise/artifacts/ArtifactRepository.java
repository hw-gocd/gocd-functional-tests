package com.thoughtworks.cruise.artifacts;

// JUnit Assert framework can be used for verification

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

import java.io.BufferedOutputStream;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

import net.sf.sahi.client.Browser;

import org.apache.commons.collections.map.SingletonMap;
import org.apache.commons.io.IOUtils;
import org.apache.commons.lang.StringUtils;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.preconditions.NewStreamPumper;
import com.thoughtworks.cruise.state.ArtifactFilesystem;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.twist.core.utils.OsUtils;

public class ArtifactRepository {

    private final ArtifactFilesystem artifactFilesystem;
    private final Configuration configuration;

    public ArtifactRepository(Browser browser, ArtifactFilesystem artifactFilesystem, Configuration configuration) {
        this.artifactFilesystem = artifactFilesystem;
        this.configuration = configuration;
    }
    
    public static void fileWithSize(int sizeOfArtifactInMB, File artifact) throws FileNotFoundException, IOException {
        BufferedOutputStream out = new BufferedOutputStream(new FileOutputStream(artifact));
        byte[] block = block();
        for (int i = 0; i < sizeOfArtifactInMB * 1024 / 4; i++) {
            out.write(block);
            out.flush();
        }
        out.close();
    }

    private static byte[] block() {
        byte [] bytes = new byte[4 * 1024];
        for (int i=0; i < 4 * 1024; i++) bytes[i] = 0;
        return bytes;
    }

    @SuppressWarnings("unchecked")
    public void pointTheArtifactRepositoryToAPartitionOfSizeMB(int sizeInMB) throws Exception {
        if (OsUtils.isLinux()) {          
            File file = artifactFilesystem.fileSystem.getAbsoluteFile();
            fileWithSize(sizeInMB, file);
            run(new ByteArrayInputStream("y".getBytes()), "mkfs.ext3", file.getAbsolutePath(), "-m", "0");
            run(new SingletonMap("SUDO_ASKPASS", new File(RuntimePath.pathFor("../manual-testing/twist/echo_password.sh")).getAbsolutePath()), new ByteArrayInputStream("".getBytes()), 
                    "sudo", "-A", "/bin/mount", "-t", "ext3", "-o", "loop", file.getAbsolutePath(), RuntimePath.getArtifactPath(configuration.provideDom().getArtifactsDir()));
        } else {
            throw new UnsupportedOperationException("Not supported on non GNU/Linux environments yet");
        }
    }
    
    public static void run(InputStream processInput, String...commandAndArgs) throws IOException, InterruptedException {
        run(new HashMap<String, String>(), processInput, commandAndArgs);
    }

    public static void run(Map<String, String> envVars, InputStream processInput, String...commandAndArgs) throws IOException, InterruptedException {
        ProcessBuilder processBuilder = new ProcessBuilder(commandAndArgs);
        for(Entry<String, String> envVar : envVars.entrySet()) {
            processBuilder.environment().put(envVar.getKey(), envVar.getValue());
        }
        processBuilder.redirectErrorStream(true);
        Process process = processBuilder.start();
        NewStreamPumper.pump(process.getInputStream(), "out", System.out);
        OutputStream outputStream = process.getOutputStream();
        IOUtils.copy(processInput, outputStream);
        outputStream.close();
        int returnCode = process.waitFor();
        assertThat(String.format("Failed executing commad: %s", StringUtils.join(commandAndArgs, " ")), returnCode, is(0));
    }

    public static void run(String... commandAndArgs) throws IOException, InterruptedException {
        run(new ByteArrayInputStream("".getBytes()), commandAndArgs);
    }

    public void waitTillTheFreeSpaceIsMoreThanMB(final int freeSpaceInMB) throws Exception {
        
        Assertions.waitUntil(Timeout.THREE_MINUTES, new Predicate() {
            
            @Override
            public boolean call() throws Exception {
                return artifactRepoFreeSpace() > (freeSpaceInMB * 1024 * 1024L);
            }

            public long artifactRepoFreeSpace() {
                return new File(RuntimePath.getArtifactPath(configuration.provideDom().getArtifactsDir())).getFreeSpace();
            }
            
            public double artifactRepoFreeSpaceInMB() {
                return artifactRepoFreeSpace() / 1024 / 1024;
            }
            
            public String toString() {
                return String.format("Expected the free space on the artifact repo to increase beyond '%s' MB. Actually, it was: %s", freeSpaceInMB, artifactRepoFreeSpaceInMB());
            };
        });
    }
}
