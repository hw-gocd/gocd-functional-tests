package com.thoughtworks.cruise.context;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.apache.commons.lang.exception.ExceptionUtils;
import org.joda.time.DateTime;

import net.sf.sahi.client.Browser;

import com.thoughtworks.cruise.CruiseAgents;
import com.thoughtworks.cruise.SahiBrowserWrapper;
import com.thoughtworks.cruise.page.OnAgentsPage;
import com.thoughtworks.cruise.preconditions.AgentLauncher;
import com.thoughtworks.cruise.preconditions.ProcessIsRunning;
import com.thoughtworks.cruise.util.ProcessUtils;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Assertions.ReattemptFailureException;
import com.thoughtworks.cruise.utils.Timeout;

public class WithLiveAgentsInDirectory {
    private List<AgentLauncher> agents = new ArrayList<AgentLauncher>();
    protected final OnAgentsPage agentPage;
    private static int scenarioNumber = 0;
    private final CruiseAgents createdAgents;
    private final Browser browser;

    // The dependency on Configuration enforces that this be added after a configuration context
    public WithLiveAgentsInDirectory(Configuration configuration, OnAgentsPage agentPage, CruiseAgents createdAgents, Browser browser) {
        this.agentPage = agentPage;
        this.createdAgents = createdAgents;
        this.browser = browser;
    }

    @com.thoughtworks.gauge.Step("With <numberOfAgents> live agents in directory <directory> - setup")
	public void setUp(int numberOfAgents, String directory) throws Exception {
        if (System.getenv("DONT_LAUNCH_AGENTS") == null) {
            stopAnyOldAgentsLeftBehind();
            createAgents(numberOfAgents, scenarioDirectoryName(directory));
            waitForEnabledAgents(numberOfAgents + numberOfMissingAgents(), numberOfAgents);
        } else {
            waitForEnabledAgents(1 + numberOfMissingAgents(), 1);
        }
    }

    private void waitForEnabledAgents(final int expected, final int numberOfLiveAgents) {
        agentPage.open();
        try {
            Assertions.waitUntil(Timeout.FIVE_MINUTES, new Predicate() {
                public boolean call() {
                    boolean success = agentPage.numberOfEnabledAgents() >= expected && agentPage.numberOfAvailableAgents() >= numberOfLiveAgents;
                    if (!success) {
                        System.err.println(toString() + " (as shown below)");
                        agentPage.printSummary();
                        System.err.println();
                    }
                    return success;
                }

                public String toString() {
                    String expectedStr = String.format("Expected agents: [%s],  Expected live: [%s]", expected, numberOfLiveAgents);
                    try {
                        return expectedStr
                                + String.format(" but Actual agents: [%s], Actual live [%s]. On page [%s]", agentPage.numberOfAvailableAgents(), agentPage.numberOfEnabledAgents(),
                                        new SahiBrowserWrapper(browser).getCurrentUrl());
                    } catch (Exception e) {
                        e.printStackTrace();
                        return expectedStr + " Failed to retrive actuals";
                    }
                }
            });
        } catch (ReattemptFailureException e) {
            captureGoStateAndRethrowException(e);
        }
    }

    private void captureGoStateAndRethrowException(RuntimeException originalException) {
        try {
            new CaptureGoState(browser).generateReportWithAgentData("WITH_LIVE_AGENTS", "FAILED_TO_START");
        } catch (IOException e) {
            throw new RuntimeException("Failed to generate report after catching original exception: " + ExceptionUtils.getFullStackTrace(e), e);
        }
        throw originalException;
    }

    @com.thoughtworks.gauge.Step("With <integer1> live agents in directory <string2> - teardown")
	public void tearDown(Integer integer1, String string2) throws Exception {
        if (System.getenv("DONT_LAUNCH_AGENTS") == null) {
            destroyAgents();
        }
    }

    private String scenarioDirectoryName(String directory) {
        return String.format("scn-%02d", (++scenarioNumber));
    }

    protected int numberOfMissingAgents() {
        return 1;
    }

    private void createAgents(int numberOfAgents, String directory) throws Exception {
        System.err.println("Creating " + numberOfAgents + " agents");
        for (int i = 0; i < numberOfAgents; i++) {
            AgentLauncher agent = AgentLauncher.startNewAgent(directory, null);
            agents.add(agent);
            createdAgents.addAgent(agent);
        }
    }

    private void destroyAgents() {
        for (AgentLauncher agent : agents) {
            try {
                agent.destroy();
            } catch (Exception e) {
                System.err.println("Ignoring error when destroying " + agent + " : " + e.getMessage());
            }
        }
        stopAnyOldAgentsLeftBehind();
    }

    private void stopAnyOldAgentsLeftBehind() {
        System.out.println(new DateTime() + " ==================================");
        System.out.println(new DateTime() + " List agents before sending a kill:");
        System.out.println(ProcessUtils.pgrep("go.twist.agent"));

        ProcessUtils.pkill("go.twist.agent");
        ProcessUtils.pkillForcibly("go.twist.agent");

        System.out.println(new DateTime() + " List agents after sending a kill:");
        System.out.println(ProcessUtils.pgrep("go.twist.agent"));
        System.out.println(new DateTime() + " ==================================");
    }

    public AgentLauncher getAgent(int i) {
        return agents.get(i);
    }
}
