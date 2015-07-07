package com.thoughtworks.cruise.preconditions;

import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.springframework.beans.factory.InitializingBean;

public class DeleteTwistAgentDirectories implements InitializingBean {

	@Override
	public void afterPropertiesSet() throws Exception {
		deleteAgentDirs();
	}

	private void deleteAgentDirs() throws IOException {
		FileUtils.deleteDirectory(AgentLauncher.TWIST_AGENTS_DIR);
		AgentLauncher.TWIST_AGENTS_DIR.mkdirs();
	}

}
