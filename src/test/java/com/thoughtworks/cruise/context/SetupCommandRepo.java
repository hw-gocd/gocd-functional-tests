package com.thoughtworks.cruise.context;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.hamcrest.core.Is;
import org.junit.Assert;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;

public class SetupCommandRepo {
	File task_repo_location = new File(RuntimePath.getServerRoot() + "/db/command_repository");
	private final TalkToCruise talkToCruise;
	
	public SetupCommandRepo(TalkToCruise talkToCruise){
		this.talkToCruise = talkToCruise;
		
	}
	
	@com.thoughtworks.gauge.Step("Setup command repo - setup")
	public void setUp() throws Exception {	
		moveDefaultDirectory("/default", "/default_backup");

		File default_repo = new File(getClass().getResource("/command-repo/default").getFile());
		FileUtils.copyDirectoryToDirectory(default_repo, task_repo_location);		
		
		File custom_repo = new File(getClass().getResource("/command-repo/custom").getFile());
		FileUtils.copyDirectoryToDirectory(custom_repo, task_repo_location);	
		CruiseResponse response = talkToCruise.post(Urls.urlFor("/api/admin/command-repo-cache/reload"));
		Assert.assertThat(response.getStatus(), Is.is(200));
		
	}

	@com.thoughtworks.gauge.Step("Setup command repo - teardown")
	public void tearDown() throws Exception {
		FileUtils.deleteQuietly(new File(task_repo_location.getPath() + "/default"));
		FileUtils.deleteQuietly(new File(task_repo_location.getPath() + "/custom"));
		moveDefaultDirectory("/default_backup", "/default");
		
	}
	
	private void moveDefaultDirectory(String srcDir, String destDir) throws IOException {
		File sourceDir = new File(task_repo_location.getPath() + srcDir);
		FileUtils.moveDirectory(sourceDir, new File(task_repo_location.getPath() + destDir));
	}
}
