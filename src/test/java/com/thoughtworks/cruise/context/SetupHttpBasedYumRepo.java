package com.thoughtworks.cruise.context;

import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;
import java.util.Iterator;

import org.apache.commons.io.FileUtils;
import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;

public class SetupHttpBasedYumRepo {
	private File yumRepoLocation = new File(RuntimePath.pathFor("../tools/jetty-8/webapps/yumrepo"));
	private File jettyRootDir = new File(RuntimePath.pathFor("../tools/jetty-8/"));
	private Process jettyServer;
	public SetupHttpBasedYumRepo() {
	}

	@com.thoughtworks.gauge.Step("Setup http based yum repo - setup")
	public void setUp() throws Exception {
		FileUtils.deleteQuietly(yumRepoLocation);
		cleanupRepoqueryCacheDirectory();		
		copyFilesFromDirectory("test-repos/yumrepo/revision-one");
		execute(yumRepoLocation, "createrepo", ".");
		jettyServer = startJettyServer();
	}
	
	private void cleanupRepoqueryCacheDirectory() throws IOException{
		File[] cacheFiles = new File("/var/tmp/").listFiles(new FilenameFilter() {			
			@Override
			public boolean accept(File dir, String name) {
				String currentUser = System.getProperty("user.name") != null ? System.getProperty("user.name") : "go";
				return name.startsWith(String.format("yum-%s-", currentUser));
			}
		});
		for(File cacheFile : cacheFiles){
			FileUtils.forceDelete(cacheFile);
		}
	}

	private Process startJettyServer() throws Exception{		
		ProcessBuilder processBuilder = new ProcessBuilder("java", "-jar", "start.jar", "jetty.port=8081");
		processBuilder.directory(jettyRootDir);
		return processBuilder.start();		
	}

	@com.thoughtworks.gauge.Step("Publish new artifact")
	public void publishNewArtifact() throws Exception {
		copyFilesFromDirectory("test-repos/yumrepo/revision-two");
		execute(yumRepoLocation, "createrepo", "--update", ".");
	}

	@com.thoughtworks.gauge.Step("Setup http based yum repo - teardown")
	public void tearDown() throws Exception {
		if(jettyServer != null) jettyServer.destroy();		
		FileUtils.deleteQuietly(new File(yumRepoLocation.getPath()));
	}

	private void copyFilesFromDirectory(String sourceDirectory)
			throws IOException {
		File yumRepo = new File(RuntimePath.absolutePathFor(sourceDirectory));
		Iterator iterateFiles = FileUtils.iterateFiles(yumRepo,
				new String[] { "rpm" }, false);
		while (iterateFiles.hasNext()) {
			File file = (File) iterateFiles.next();
			FileUtils.copyFileToDirectory(file, yumRepoLocation);
		}

	}

	private void execute(File workingDir, String... args) throws IOException,
			InterruptedException {
		ProcessBuilder processBuilder = new ProcessBuilder(args);
		processBuilder.directory(workingDir);
		Process process = processBuilder.start();
		process.waitFor();
	}
}
