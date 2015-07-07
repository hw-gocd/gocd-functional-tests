package com.thoughtworks.cruise.materials;

public class TfsServer {
	public String getUrl(){
    	return System.getenv("TFS_SERVER_URL")!=null ? System.getenv("TFS_SERVER_URL") : "http://sifystdgobgr101.thoughtworks.com:8080/tfs/";
	}

	public String getDefaultTfsCollectionUrl() {
		return getUrl() + "twist_tests";
	}	
}

