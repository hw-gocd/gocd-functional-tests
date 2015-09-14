package com.thoughtworks.cruise.context;

import org.apache.commons.lang.RandomStringUtils;

import com.thoughtworks.cruise.plugin.YumHttpRepository;
import com.thoughtworks.cruise.state.ScenarioState;

public class SetupHttpBasedYumRepo {
    private static final String DEFAULT_HTTP_REPO_URL_NAME_IN_CONFIG = "http_repo1";
    private ScenarioState scenarioState;
    private YumHttpRepository yumRepository;

    public SetupHttpBasedYumRepo(ScenarioState scenarioState) {
        this.scenarioState = scenarioState;
        this.yumRepository = new YumHttpRepository(scenarioState);
    }

    @com.thoughtworks.gauge.Step("Setup http based yum repo - setup")
	public void setUp() throws Exception {
        if (!scenarioState.hasPackageRepositoryHttpRepoNamed(DEFAULT_HTTP_REPO_URL_NAME_IN_CONFIG)) {
            scenarioState.pushPackageRepositoryHttpRepoName(DEFAULT_HTTP_REPO_URL_NAME_IN_CONFIG, "pkgrepo-" + RandomStringUtils.randomAlphanumeric(10));
        }
        yumRepository.create(this.scenarioState.packageRepositoryHttpRepoNamed(DEFAULT_HTTP_REPO_URL_NAME_IN_CONFIG));
    }

    @com.thoughtworks.gauge.Step("Setup http based yum repo - teardown")
	public void tearDown() throws Exception {
        yumRepository.remove(this.scenarioState.packageRepositoryHttpRepoNamed(DEFAULT_HTTP_REPO_URL_NAME_IN_CONFIG));
    }
}
