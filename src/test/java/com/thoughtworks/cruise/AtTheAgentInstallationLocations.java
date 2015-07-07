package com.thoughtworks.cruise;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

import java.io.File;

import com.thoughtworks.cruise.state.ScenarioState;

public class AtTheAgentInstallationLocations {

    private String currentAgent;
    private String currentPipeline;
    private final ScenarioState scenarioState;
    private final CruiseAgents createdAgents;

    public AtTheAgentInstallationLocations(CruiseAgents createdAgents, ScenarioState scenarioState) {
        this.createdAgents = createdAgents;
        this.scenarioState = scenarioState;
    }
    
    @com.thoughtworks.gauge.Step("Looking at first agent for pipeline <pipelineName>")
	public void lookingAtFirstAgentForPipeline(String pipelineName) throws Exception {
        this.currentPipeline = pipelineName;
        currentAgent = createdAgents.get(0).getWorkingDirectory();
    }

    @com.thoughtworks.gauge.Step("Verify <materialFolderName> is checked out under the pipelines folder")
	public void verifyIsCheckedOutUnderThePipelinesFolder(String materialFolderName) throws Exception {
        assertThat(new File(codeFolder(), materialFolderName).exists(), is(true));
    }

    private String codeFolder() {
        return currentAgent + "/pipelines/" + currentPipeline() ;
    }

    private String currentPipeline() {
        return currentPipeline == null ? scenarioState.currentRuntimePipelineName() : scenarioState.pipelineNamed(currentPipeline);
    }

    @com.thoughtworks.gauge.Step("Verify code for <materialFolderName> material is removed")
	public void verifyCodeForMaterialIsRemoved(String materialFolderName) throws Exception {
        assertThat(new File(codeFolder(), materialFolderName).exists(), is(false));
    }
}
