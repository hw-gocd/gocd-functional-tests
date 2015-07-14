package com.thoughtworks.cruise.preconditions;

import java.io.File;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

import org.apache.commons.io.FileUtils;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.Urls;
import com.thoughtworks.cruise.util.SystemUtil;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigFileEditor;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigUtil;

public class ServerIsRunning extends ProcessIsRunning {
    private CruiseConfigUtil configFile;
    private boolean twistStartedServer;
    private boolean fanInTurnedOff;

    public ServerIsRunning() {
        configFile = new CruiseConfigUtil(new CruiseConfigFileEditor());
    }

    public void start() throws Exception {
        twistStartedServer = !isAlreadyRunning();
        forceStart();
    }

    public void forceStart() throws IOException, Exception {
        if (!(fanInTurnedOff)) {
            configFile.resetCruiseConfig();
        }

        if (!isAlreadyRunning()) {
            copyLog4jProperties();
            super.start();
            waitForServerToStart();
        }
    }

    private void copyLog4jProperties() throws IOException {
        File agentLog4j = new File(RuntimePath.getServerConfigPath(), "log4j.properties");
        FileUtils.copyFile(new File(RuntimePath.pathFor("properties"), "server-log4j.properties"), agentLog4j);
    }

    public void stop() throws Exception {
        if (twistStartedServer) {
            forceStop();
        }
    }

    public void forceStop() throws Exception {
        super.stop();
    }

    public static boolean isAlreadyRunning() {
        try {
            return head(Urls.urlFor("/admin/agent")).success();
        } catch (Exception e) {
            return false;
        }
    }

    protected boolean isProcessStopped() {
        if (SystemUtil.isWindows()) {
            return isProcessStoppedOnWindows("cruise server - server.cmd");
        } else {
            return isProcessStoppedOnLinux();
        }
    }

    private void waitForServerToStart() throws Exception {
        Assertions.waitUntil(Timeout.TEN_MINUTES, new Assertions.Predicate() {
            public boolean call() {
                return isAlreadyRunning();
            }
        });
    }

    protected String getWorkingDir() {
        return RuntimePath.getServerRoot();
    }

    public File fileFor(String relPath) {
        return new File(getWorkingDir(), relPath);
    }

    protected Map<String, String> getStartEnvVariables() {
        String extraDBParams = additionalDBParametersIfPostgresqlIsToBeUsed();
        StringBuilder extraParams = new StringBuilder(extraDBParams);
        if ("Y".equals(System.getenv("USE_JETTY_6"))){
            extraParams.append(" -Dapp.server=com.thoughtworks.go.server.Jetty6Server");
        }
        HashMap<String, String> env = new HashMap<String, String>();
        env.put("GO_SERVER_SYSTEM_PROPERTIES",
                "-Dalways.reload.config.file=true " +
                        "-Dcruise.buildCause.producer.interval=10000 " +
                        "-Dmaterial.update.idle.interval=10000 " +
                        "-Dcruise.xmpp.port=61221 " +
                        "-Dcruise.agent.service.refresh.interval=5000 " +
                        "-Dcruise.shine.sparql.url=http://localhost:8253/go/shine/sparql.xml " +
                        "-Dcruise.shine.stage.feed=http://localhost:8253/go/api/feeds/stages.xml " +
                        "-Dagent.connection.timeout=50 " +
                        "-Dcruise.unresponsive.job.warning=1 " +
                        "-Dcruise.pipelineStatus.cache.interval=800 " +
                        "-Dcommand.repo.warning.timeout=30000 " +
                        "-Dnew.plugins.framework.enabled=Y " +
                        "-DDB_DEBUG_MODE=true" +
                        extraParams.toString());
        env.put("GO_SERVER_PORT", Urls.SERVER_PORT);
        env.put("GO_SERVER_SSL_PORT", Urls.SSL_PORT);
        String serverMem = System.getenv("TWIST_GO_SERVER_MEM") != null ? System.getenv("TWIST_GO_SERVER_MEM") : "256m";
        String serverMaxMem = System.getenv("TWIST_GO_SERVER_MAX_MEM") != null ? System.getenv("TWIST_GO_SERVER_MAX_MEM") : "512m";
        env.put("SERVER_MEM", serverMem);
        env.put("SERVER_MAX_MEM", serverMaxMem);
        env.put("JVM_DEBUG", "true");
        if (fanInTurnedOff) {
            String addFaninJVMArg = env.get("GO_SERVER_SYSTEM_PROPERTIES") + " -Dresolve.fanin.revisions=N";
            env.put("GO_SERVER_SYSTEM_PROPERTIES", addFaninJVMArg);
        }
        String useNewRails = System.getenv("USE_NEW_RAILS");
        if (useNewRails != null && useNewRails.equals("N")) {
            String addRails4JVMArg = env.get("GO_SERVER_SYSTEM_PROPERTIES") + " -Duse.new.rails=N";
            env.put("GO_SERVER_SYSTEM_PROPERTIES", addRails4JVMArg);
        }
        return env;
    }


    private String additionalDBParametersIfPostgresqlIsToBeUsed() {
        if (!("Y".equals(System.getenv("USE_POSTGRESQL")))) {
            return "";
        }
        return String.format(" -Duse.postgresql.db=Y -Dgo.database.provider=com.thoughtworks.go.postgresql.PostgresqlDatabase -Ddb.host=%s -Ddb.user=%s -Ddb.password=%s -Ddb.name=%s -Ddb.port=%s",
                System.getenv("POSTGRES_DB_HOST_TO_USE"), "postgres", "postgres", System.getenv("POSTGRES_DB_NAME_TO_USE").toLowerCase(), "5432");
    }

    protected String startCommand() {
        return SystemUtil.isWindows() ? "start-server.bat" : "./server.sh";
    }

    protected String stopCommand() {
        return SystemUtil.isWindows() ? "stop-server.bat" : "./stop-server.sh";
    }

    @Override
    protected boolean pumpOutputStream() {
        return false;
    }

    @Override
    protected boolean pumpErrorStream() {
        return true;
    }

    public void setFanInOff(boolean fanInTurnedOff) {
        this.fanInTurnedOff = fanInTurnedOff;
    }
}
