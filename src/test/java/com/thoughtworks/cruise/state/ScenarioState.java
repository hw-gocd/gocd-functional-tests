package com.thoughtworks.cruise.state;

import static com.thoughtworks.cruise.util.ExceptionUtils.bomb;

import java.io.File;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import org.dom4j.Attribute;

import com.thoughtworks.cruise.HttpContext;
import com.thoughtworks.cruise.HttpContext.ApiTransport;
import com.thoughtworks.cruise.utils.RuntimeVariableSubstituter;
import com.thoughtworks.cruise.utils.RuntimeVariableSubstituter.Replacer;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public class ScenarioState implements Replacer, CurrentUsernameProvider {
	
	private Map<String, String> pipelineNameMappings = new HashMap<String, String>();
	private Map<String, Set<String>> agentsUnderEnvironments = new HashMap<String, Set<String>>();
	private Map<String, String> pipelineInstanceUrls = new HashMap<String, String>();
	private Map<String, String> agentsByAlias= new HashMap<String, String>();
	private Map<String, String> packageRepositoryURIMappings = new HashMap<String, String>();

	private String currentPipeline;
	private String currentUserName;

	public static final String USER_ADMIN = "user-admin";
	public static final String USER_OPERATOR = "user-operator";
	public static final String USER_VIEWER = "user-viewer";
	public static final String USER_NO_PERMISSION = "user-no-permission";
	public static final String DEFAULT_GROUP = "defaultGroup";
	private Map<String, CruiseConfigDom> validConfigurations = new HashMap<String, CruiseConfigDom>();
	private ApiTransport httpScheme;
    private Map<String,File> artifactNameToFile = new HashMap<String, File>();
    private Map<String, String> keyValueStore = new HashMap<String, String>();
	
	
	public ScenarioState() {
		new HttpContext(this).using(ApiTransport.HTTP.toString());
	}	
	
	public CruiseConfigDom getValidConfigNamed(String name) {
		return validConfigurations.get(name);
	}

	public void storeAsValidConfigNamed(String name, CruiseConfigDom validConfig) {
		validConfigurations.put(name, validConfig);
	}
	
	public String logicalPipelineName(String runtimePipelineName) {
		for (String key : pipelineNameMappings.keySet()	) {
			if(pipelineNameMappings.get(key).equals(runtimePipelineName)){
				return key;
			}
		}	
		throw bomb("No pipeline found with runtime name: " + runtimePipelineName);
	}

	public String pipelineNamed(String pipelineName) {
		if (pipelineNameMappings.containsKey(pipelineName)) {
			return pipelineNameMappings.get(pipelineName);
		}
		if (pipelineNameMappings.values().contains(pipelineName)) { // the pipelineName is already the runtime name so don't bomb
			return pipelineName;
		}
		throw bomb("No pipeline found with name: " + pipelineName);
	}

	public String packageRepositoryNamed(String packageRepositoryName)
	{
		if(packageRepositoryURIMappings.containsKey(packageRepositoryName)) {
			return packageRepositoryURIMappings.get(packageRepositoryName);
		}
		
		if(packageRepositoryURIMappings.values().contains(packageRepositoryName)){
			return packageRepositoryName;
		}
		
		throw bomb("No Package Repository found with name: " + packageRepositoryName);
		
	}
	
	public void pushPipeline(String key, String value) {
		pipelineNameMappings.put(key, value);
	}

	public void addAgentsByEnvironment(Set<String> agentUuids, String environment) {
		if (agentsUnderEnvironments.containsKey(environment)) {
			agentsUnderEnvironments.get(environment).addAll(agentUuids);
			return;
		}
		agentsUnderEnvironments.put(environment, agentUuids);
	}

	public Set<String> agentsUnderEnvironment(String environmentName) {
		return agentsUnderEnvironments.get(environmentName);
	}

	public String currentPipeline() {
		return currentPipeline;
	}
	
	public String currentRuntimePipelineName() {
		return pipelineNamed(currentPipeline());
	}

	public void usingPipeline(String pipeline) {
		this.currentPipeline = pipeline;
	}

	public boolean hasPipeline(String pipeline) {
		return pipelineNameMappings.containsKey(pipeline);
	}

	public Collection<String> getAllRuntimePipelineNames() {
		return pipelineNameMappings.values();
	}

	public void knownPipelineInstanceUrl(String pipelineName, Attribute url) {
		pipelineInstanceUrls.put(pipelineName, url.getValue());
	}

	public String knownPipelineInstanceUrl(String pipelineName) {
		if (! pipelineInstanceUrls.containsKey(pipelineName)) {
			throw new IllegalArgumentException(String.format("no url known for pipeline named [%s]", pipelineName));
		}
		return pipelineInstanceUrls.get(pipelineName);
	}

	public void loggedInAs(String userName) {
		this.currentUserName = userName;
	}

	public void logOut() {
		this.currentUserName = null;		
	}

	public String loggedInUser() {
		return this.currentUserName;
	}
	
	public void removeAgentsByEnvironment(Set<String> agentUuids, String environment) {
		if (agentsUnderEnvironments.containsKey(environment)) {
			agentsUnderEnvironments.get(environment).removeAll(agentUuids);
			return;
		}
		agentsUnderEnvironments.put(environment, agentUuids);
	}

	@Override
	public String replacementFor(String variable) {
		return variable.startsWith("runtime_package_repo_uri") ? packageRepositoryNamed(variable.substring("runtime_package_repo_uri:".length()).trim()) : variable.startsWith("runtime_name:") ? pipelineNamed(variable.substring("runtime_name:".length()).trim()) : null;
	}
	
	public String expand(String stageLocator) {	
		return new RuntimeVariableSubstituter(this).replaceRuntimeVariables(stageLocator);
	}

	public void setApiTransportScheme(ApiTransport apiTransport) {
		this.httpScheme = apiTransport;		
	}
	
	public ApiTransport getApiTransportScheme() {
		return this.httpScheme;		
	}

	public void rememberAgentByAlias(String agentAlias, String agentDetails) {
		agentsByAlias.put(agentAlias, agentDetails);
	}

	public String getAgentByAlias(String agentAlias) {
		return agentsByAlias.get(agentAlias);
	}

    public void storeArtifact(String artifactName, File createTempFile) {
        this.artifactNameToFile.put(artifactName, createTempFile);
    }

    public File artifactNamed(String artifactHandle) {
        return this.artifactNameToFile.get(artifactHandle);
    }
    
    public String getValueFromStore(String key) {
    	return keyValueStore.get(key);
    }
    
    public void putValueToStore(String key, String value) {
    	keyValueStore.put(key, value);
    }

	public void pushPackageRepositoryURI(String key, String value) {
		packageRepositoryURIMappings.put(key, value);
		
	}
}