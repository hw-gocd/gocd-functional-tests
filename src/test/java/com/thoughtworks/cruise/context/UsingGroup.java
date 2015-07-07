package com.thoughtworks.cruise.context;

import java.util.ArrayList;

import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.util.ListUtil;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public class UsingGroup {

	private CruiseConfigDom dom;
	private final Configuration configuration;
	private final UsingPipeline usingPipeline;
	private final ScenarioState scenarioState;

	public UsingGroup(Configuration configuration, UsingPipeline usingPipeline,ScenarioState scenarioState) {
		this.configuration = configuration;
		this.usingPipeline = usingPipeline;
		this.scenarioState = scenarioState;		
        this.dom = configuration.provideDom();
	}

	@com.thoughtworks.gauge.Step("Using group <joinedGroups> - setup")
	public void setUp(String joinedGroups) throws Exception {
		String[] groups = joinedGroups.split("\\s*,\\s*");
		waitUntilDOMHasGroups(groups);
		String pipelines = covertToLogical(configuration.provideDom().pipelinesFor(groups));
		usingPipeline.setUp(pipelines);
	}

	private String covertToLogical(ArrayList<String> pipelines) {
		ArrayList<String> logicalNames = new ArrayList<String>();
		for (String runtimename : pipelines) {
			logicalNames.add(scenarioState.logicalPipelineName(runtimename));
		}				
		return ListUtil.join(logicalNames,",");
	}

	private void waitUntilDOMHasGroups(final String[] groups) {
		Assertions.waitUntil(Timeout.TWO_MINUTES, new Predicate() {			
			public boolean call() throws Exception {				
				return configuration.provideDom().containsGroups(groups);
			}
		});
		this.dom = configuration.provideDom();
	}

	@com.thoughtworks.gauge.Step("Using group <string1> - teardown")
	public void tearDown(String string1) throws Exception {
	
	}	
}
