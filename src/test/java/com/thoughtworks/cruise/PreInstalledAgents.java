package com.thoughtworks.cruise;

import java.io.File;
import java.io.IOException;

import com.thoughtworks.cruise.preconditions.AgentLauncher;
import com.thoughtworks.cruise.util.FileUtil;

public class PreInstalledAgents implements Agents {

	private void ignoringMessage(String message) {
		System.err.println("IGNORING(running in preinstalled agents mode) -> " + message);
	}

	@Override
	public void addAgent(AgentLauncher workingDirectory) {
		ignoringMessage("adding agents to working dir " + workingDirectory);
	}

	@Override
	public int count() {
		ignoringMessage("count of agents, returning 0");
		return 0;
	}

	@Override
	public void deleteStopjobFileOnAllAgents() {
		throw new UnsupportedOperationException("delete stop job file not implemented for pre installed agent.");
	}

    public void createStopJobFileForAllAgents(boolean shouldPass) {
        String dir = RuntimePath.getTwistAgentPath();
		try {
			String content = "";
			if (!shouldPass) {
				content += "\nstopjob.fail=ANYTHING\n";
			}
			FileUtil.writeContentToFile(content, new File(dir, STOP_JOB_FILE));
		} catch (IOException e) {
			throw new RuntimeException("Could not create file " + STOP_JOB_FILE, e);
		}
    }

    @Override
	public AgentLauncher get(int index) {
		ignoringMessage("getting agent by index " + index + ", returning null");
		return null;
	}
    
    @Override
    public AgentLauncher get(String uuid) {
        ignoringMessage("getting agent by uuid " + uuid + ", returning null");
        return null;
    }

	@Override
	public void stopRunTillFileExistsJobs(int numberOfJobs, boolean shouldPass) {
		if (numberOfJobs > 1) {
            throw new IllegalArgumentException("Running against installed agent must have maximum less than or equal to one(1) job waiting for file to exist.");
        }
        createStopJobFileForAllAgents(shouldPass);
	}

    @Override
    public void removeAgentFromList(AgentLauncher agent) {
        ignoringMessage("removing agent " + agent.getUuid());
    }

    
}
