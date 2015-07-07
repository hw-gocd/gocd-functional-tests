package com.thoughtworks.cruise;

import java.io.File;

import com.thoughtworks.cruise.preconditions.ServerIsRunning;

public class SetupServer{

    private final ServerIsRunning serverIsRunning;

    public SetupServer(ServerIsRunning serverIsRunning){
        this.serverIsRunning = serverIsRunning;
        
    }
    
    @com.thoughtworks.gauge.Step("Stop server")
	public void stopServer() throws Exception {
        serverIsRunning.stop();
    }
    
    @com.thoughtworks.gauge.Step("Start server with fanin turned off")
	public void startServerWithFaninTurnedOff() throws Exception {
        serverIsRunning.setFanInOff(true);
        serverIsRunning.start();
    }
    
	@com.thoughtworks.gauge.Step("Create a directory <dirName> without permissions in the command _ repository location <commandRepoLocation>")
	public void createADirectoryWithoutPermissionsInTheCommand_RepositoryLocation(
			String dirName, String commandRepoLocation) throws Exception {
		String dirWithoutPermissionLocation = String.format("/db/command_repository/%s/%s", commandRepoLocation, dirName);
		File dirWithoutPermissions = new File(RuntimePath.getServerRoot()+ dirWithoutPermissionLocation);
    	dirWithoutPermissions.mkdir();
    	dirWithoutPermissions.setReadable(false);
	}

	@com.thoughtworks.gauge.Step("Cleanup directory <dirName> in the command _ repository location <commandRepoLocation>")
	public void cleanupDirectoryInTheCommand_RepositoryLocation(String dirName,
			String commandRepoLocation) throws Exception {
		String dirLocation = String.format("/db/command_repository/%s/%s", commandRepoLocation, dirName);
		File dir = new File(RuntimePath.getServerRoot()+ dirLocation);
		dir.delete();
	}

	@com.thoughtworks.gauge.Step("Start server")
	public void startServer() throws Exception {
		serverIsRunning.start();
	}
}
