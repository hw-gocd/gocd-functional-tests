package com.thoughtworks.cruise.state;

import java.util.HashMap;
import java.util.Map;

public class EnvironmentState {
    
    Map<String,Map<String,String>> currentlyDeployed = new HashMap<String,Map<String,String>>();
    public void setCurrentlyDeployed(String pipeline,String material,String revision) {
        Map<String, String> materialMap = materialMap(pipeline);
        materialMap.put(material, revision);
    }
    
    public String currentlyDeployed(String pipeline,String material) {
        return materialMap(pipeline).get(material);
    }
    
    private Map<String, String> materialMap(String pipeline) {
        Map<String,String> materialMap = currentlyDeployed.get(pipeline);
        if(materialMap==null) {
            materialMap = new HashMap<String,String>();
            currentlyDeployed.put(pipeline, materialMap);
        }
        return materialMap;
    }
}
