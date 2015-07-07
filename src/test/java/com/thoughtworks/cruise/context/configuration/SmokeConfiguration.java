package com.thoughtworks.cruise.context.configuration;

import java.io.File;
import java.io.IOException;

import net.sf.sahi.client.Browser;

import org.dom4j.Element;

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.ScenarioHelper;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public class SmokeConfiguration extends AbstractConfiguration {
	public SmokeConfiguration(Configuration config, ScenarioState state, RepositoryState repositoryState, ScenarioHelper scenarioHelper, Browser browser) throws Exception {
	    super("/config/secure-cruise-config.xml", config, state, repositoryState, scenarioHelper, browser);
        this.config = config;
	}
	
	private Configuration config;
    
    @com.thoughtworks.gauge.Step("SmokeConfiguration - setup")
	@Override
    public void setUp() throws Exception {
        super.setUp();
    }

    @Override
    protected boolean deleteAllUsersOnSetup() {
        return false;
    }

    @Override
    protected void postProcess(CruiseConfigDom dom) throws IOException {
        pointPasswordFileToAbsolutePath(dom);
    }

    private void pointPasswordFileToAbsolutePath(CruiseConfigDom dom) throws IOException {
        File destination = config.copyPasswordFile(getClass().getResource("/config/password.properties"));
        Element passwordFile = dom.getPasswordFile();
        passwordFile.attribute("path").setValue(destination.getCanonicalPath());
    }

    @com.thoughtworks.gauge.Step("SmokeConfiguration - teardown")
	@Override
    public void tearDown() throws Exception {
        super.tearDown();
    }
}