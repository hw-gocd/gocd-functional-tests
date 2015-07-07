package com.thoughtworks.cruise.context;

// JUnit Assert framework can be used for verification

import java.io.ByteArrayInputStream;
import java.io.File;

import org.apache.commons.collections.map.SingletonMap;
import org.apache.commons.io.FileUtils;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.artifacts.ArtifactRepository;
import com.thoughtworks.cruise.state.ArtifactFilesystem;

import net.sf.sahi.client.Browser;

public class UnmountArtifactsDirectory {

    private Browser browser;
    private final ArtifactFilesystem artifactFilesystem;
    private final Configuration configuration;

    public UnmountArtifactsDirectory(Browser browser, Configuration configuration, ArtifactFilesystem artifactFilesystem) {
        this.browser = browser;
        this.configuration = configuration;
        this.artifactFilesystem = artifactFilesystem;
    }

    @com.thoughtworks.gauge.Step("Unmount artifacts directory - setup")
	public void setUp() throws Exception {
    }

    @com.thoughtworks.gauge.Step("Unmount artifacts directory - teardown")
	public void tearDown() throws Exception {
        if (artifactFilesystem.fileSystem.exists()) {
            ArtifactRepository.run(new SingletonMap("SUDO_ASKPASS", new File(RuntimePath.pathFor("../manual-testing/twist/echo_password.sh")).getAbsolutePath()), 
                    new ByteArrayInputStream("".getBytes()), 
                    "sudo", "-A", "/bin/umount", "-l", RuntimePath.getArtifactPath(configuration.provideDom().getArtifactsDir()));
            FileUtils.deleteQuietly(artifactFilesystem.fileSystem);
        }
    }
}
