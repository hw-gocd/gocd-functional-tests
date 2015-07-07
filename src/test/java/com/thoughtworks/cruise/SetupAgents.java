package com.thoughtworks.cruise;

//This class exists so that CruiseAgents object can be injected to it as a scenario state
public class SetupAgents {

    public static final String AGENT_2_4 = "agent_2_4";
    private final CruiseAgents cruiseAgents;

    public SetupAgents(CruiseAgents cruiseAgents) {
        this.cruiseAgents = cruiseAgents;
    }
    
    @com.thoughtworks.gauge.Step("Start <numberOfAgents> agents with uUID <uuid>")
	public void startAgentsWithUUID(int numberOfAgents, String uuid) throws Exception {
        cruiseAgents.startAgentsWithUUID(numberOfAgents, uuid);
    }

    @com.thoughtworks.gauge.Step("Restart agent <index> using a new uUID")
	public void restartAgentUsingANewUUID(int index) throws Exception {
        cruiseAgents.restartAgentUsingANewUUID(index);
    }

    public void setUpAndStartAnAgentOlderThanGoVersion12_3WithUUID(String uuid) throws Exception {
        cruiseAgents.copyAndStartOldAgentWithUUID(AGENT_2_4, uuid);
    }

    public void stopWithUUID(String agentUuid) throws Exception {
        cruiseAgents.stopAgentWithUUID(agentUuid);
    }

    public void upgrade2_4AgentToLatestAndStartWithUUID(String uuid) throws Exception {
        cruiseAgents.startAgentWithUUID(AGENT_2_4, uuid, null);
    }
    
}
