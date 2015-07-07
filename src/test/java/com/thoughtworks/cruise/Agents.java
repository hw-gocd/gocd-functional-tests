package com.thoughtworks.cruise;

import java.io.File;

import com.thoughtworks.cruise.preconditions.AgentLauncher;

public interface Agents {
	static final String STOP_JOB_FILE = "stopjob";
    static final String WAITING_FOR_STOP_JOB_FILE = "waiting_for_stopjob";

	public abstract void addAgent(AgentLauncher workingDirectory);

	public abstract AgentLauncher get(int index);

	public abstract AgentLauncher get(String uuid);

	public abstract void stopRunTillFileExistsJobs(int numberOfJobs, boolean shouldPass);

	public abstract int count();

	public abstract void deleteStopjobFileOnAllAgents();

    void createStopJobFileForAllAgents(boolean shouldPass);

    public abstract void removeAgentFromList(AgentLauncher agent);
}