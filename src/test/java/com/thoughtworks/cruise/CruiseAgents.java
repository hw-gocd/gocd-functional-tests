package com.thoughtworks.cruise;

import java.io.File;

import com.thoughtworks.cruise.preconditions.AgentLauncher;


public class CruiseAgents implements Agents {

	private Agents agents;

	public CruiseAgents() {
	    if (System.getenv("TWIST_AGENT_PATH") == null){
	        this.agents = new CreatedAgents();
	    } else{
	        this.agents = new PreInstalledAgents();
	    }
	}

	public void stopRunTillFileExistsJobs(int numberOfJobs, boolean shouldPass) {
		agents.stopRunTillFileExistsJobs(numberOfJobs, shouldPass);
	}

	@Override
	public void addAgent(AgentLauncher launcher) {
		agents.addAgent(launcher);
	}

	@Override
	public int count() {
		return agents.count();
	}

	@Override
	public void deleteStopjobFileOnAllAgents() {
		agents.deleteStopjobFileOnAllAgents();
	}

	@Override
	public AgentLauncher get(int index) {
		return agents.get(index);
	}

    public void startAgentsWithUUID(int agentCount, String uuid) throws Exception {
        for (int i = 0; i < agentCount; i++) {
            startAgentWithUUID("agent-with-hardcoded-uuid", uuid, null);
        }
    }

    public void restartAgentUsingANewUUID(int index) throws Exception {
        AgentLauncher launcher = get(index);
        launcher.destroy();
        launcher.deleteUUID();
        launcher.start();
    }

    public void createStopJobFileForAllAgents(boolean shouldPass) {
        agents.createStopJobFileForAllAgents(shouldPass);
    }

    public void copyAndStartOldAgentWithUUID(String agentDir, String uuid) throws Exception {
        startAgentWithUUID(agentDir, uuid, RuntimePath.getOldAgentPath());
    }

    public void startAgentWithUUID(String agentDir, String uuid, String srcDir) throws Exception {
        addAgent(AgentLauncher.startAgentWithUUID(agentDir, uuid, srcDir));
    }

    public void stopAgentWithUUID(String agentUuid) {
        AgentLauncher agent = agents.get(agentUuid);
        try {
            agent.destroy();
        } catch (Exception e) {
            System.err.println("ignoring exception when stopping agent: ");
            e.printStackTrace();
        }
        agent.deleteDirectory();
        agents.removeAgentFromList(agent);
    }

    @Override
    public AgentLauncher get(String uuid) {
        return agents.get(uuid);
    }

    @Override
    public void removeAgentFromList(AgentLauncher agent) {
        agents.removeAgentFromList(agent);
    }

    

//    public void upgradeAgentAndStart() throws Exception {
//        //Get agent-bootstrapper of the latest agent.
//        AgentLauncher.startNewAgent("agent_2_4", RuntimePath.getAgentRoot()));
//    }
}
