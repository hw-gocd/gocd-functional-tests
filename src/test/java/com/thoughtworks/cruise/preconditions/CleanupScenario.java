package com.thoughtworks.cruise.preconditions;

import java.util.ArrayList;
import java.util.Collection;

import net.sf.sahi.client.Browser;

import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;

import com.thoughtworks.cruise.CruiseAgents;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigFileEditor;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigUtil;

public class CleanupScenario implements DisposableBean, InitializingBean {
	private static Collection<AgentLauncher> agentLaunchers = new ArrayList<AgentLauncher>();
	private final CruiseAgents createdAgents;
	private Browser browser;

	public CleanupScenario(CruiseAgents createdAgents, Browser browser) {
		this.createdAgents = createdAgents;
		this.browser = browser;
	}
	
	public static void stopAgentOnShutdown(AgentLauncher agentLauncher) {
		agentLaunchers.add(agentLauncher);
	}

	@Override
	public void destroy() throws Exception {
		stopJobsWaitingForFileToExist();
		logout();
		resetCruiseConfig();
		stopAgents();
	}

	private void stopJobsWaitingForFileToExist() {
		createdAgents.createStopJobFileForAllAgents(true);
	}

	@Override
	public void afterPropertiesSet() throws Exception {
		logout();
		AgentLauncher.cleanup();
	}

	private void logout() {
		try {
			if (!browser.title().contains("Login") && browser.link("nav-logout").exists(true)){
				browser.link("nav-logout").click();
			}
		} catch (Exception ignore) {
			System.err.println("Ignoring exception when logging out in CleanupScenario: " + ignore.getMessage());
		}
	}

	private void resetCruiseConfig() throws Exception {
		new CruiseConfigUtil(new CruiseConfigFileEditor()).resetCruiseConfig();
	}

	private void stopAgents() {
		for (AgentLauncher agent : agentLaunchers) {
			System.err.println("Attempting to destroy agent in dir: " + agent.getWorkingDir());
			try {
				agent.destroy();
			} catch (Exception e) {
				System.err.println("Ignoring exception when stopping agent: ");
				e.printStackTrace();
			}
		}
		agentLaunchers.clear();
	}

}
