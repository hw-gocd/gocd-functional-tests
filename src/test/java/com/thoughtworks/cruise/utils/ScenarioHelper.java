package com.thoughtworks.cruise.utils;

import com.thoughtworks.cruise.CruiseAgents;
import com.thoughtworks.cruise.preconditions.AgentLauncher;

public class ScenarioHelper {
	private final CruiseAgents createdAgents;

	public ScenarioHelper(CruiseAgents createdAgents) {
		this.createdAgents = createdAgents;
	}
	
	@com.thoughtworks.gauge.Step("Stop <numberOfJobs> jobs that are waiting for file to exist")
	public void stopJobsThatAreWaitingForFileToExist(int numberOfJobs) throws Exception {
		createdAgents.stopRunTillFileExistsJobs(numberOfJobs, true);    	
	}

	@com.thoughtworks.gauge.Step("Kill all agents")
	public void killAllAgents() throws Exception {
		for (int i = 0; i < createdAgents.count(); i++) {
			AgentLauncher agent = createdAgents.get(i);
			System.err.println("Attempting to stop agent in dir: " + agent.getWorkingDirectory());
			try {
				agent.destroy();
			} catch (Exception e) {
				System.err.println("ignoring exception when stopping agent: ");
				e.printStackTrace();
			}
		}
	}

	@com.thoughtworks.gauge.Step("Restart all agents")
	public void restartAllAgents() throws Exception {
		for (int i = 0; i < createdAgents.count(); i++) {
			AgentLauncher agent = createdAgents.get(i);
			agent.start();
		}
	}

	public void deleteStopjobFileOnAllAgents() throws Exception {
		createdAgents.deleteStopjobFileOnAllAgents();
	}

	public void waitSeconds(Integer seconds) throws Exception {
		Thread.sleep(seconds * 1000);
	}

	@com.thoughtworks.gauge.Step("Fail <numberOfJobs> jobs that are waiting for file to exist")
	public void failJobsThatAreWaitingForFileToExist(int numberOfJobs) throws Exception {
		createdAgents.stopRunTillFileExistsJobs(numberOfJobs, false);
	}
}
