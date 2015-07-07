package com.thoughtworks.cruise.materials;

import static com.thoughtworks.cruise.util.command.CommandLine.createCommandLine;

import java.io.File;
import java.util.UUID;

import org.dom4j.Element;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.util.SystemUtil;
import com.thoughtworks.cruise.util.TestFileUtil;
import com.thoughtworks.cruise.util.command.CommandLine;
import com.thoughtworks.twist.core.utils.FileUtils;

public class TfsRepository extends AbstractRepository {

    private File repositoryFolder;
    private String workspaceName;
    
    public static final String DEFAULT_PASSWORD = "BXrQ51uhU";
    public static final String DEFAULT_USER_DOMAIN = "corporate\\cruise_builder";

    public TfsRepository(Element material) {
        super(material);
        workspaceName = "test_workspace_" + UUID.randomUUID();
        initializeTestWorkspace();
        mapTestDirectory();
        getFiles();
    }

    private void initializeTestWorkspace() {
        CommandLine cmd = createCommandLine(tfCommand()).withArgs("workspace", "-new", "-noprompt", serverArg(), loginArg(), workspaceName + ";cruise_builder");
        cmd.getArguments();
        cmd.runOrBomb();
    }

    private void mapTestDirectory() {
        // create workspace and map folder
        repositoryFolder = TestFileUtil.prepareFolderInsideTempFolder("testTfsFolder");
        FileUtils.mkdirs(repositoryFolder);
        createCommandLine(tfCommand()).withArgs("workfold", "-map", "-workspace:" + workspaceName, serverArg(), loginArg(), getMaterialAttribute("projectPath"), repositoryFolder.getAbsolutePath())
                .runOrBomb();
    }

    private void getFiles() {
        createCommandLine(tfCommand()).withWorkingDir(repositoryFolder)
        .withArgs("get", repositoryFolder.getAbsolutePath(), "-recursive", "-noprompt", "-all", serverArg(), loginArg(), getMaterialAttribute("projectPath"))
        .runOrBomb();
        createCommandLine(tfCommand()).withArgs("checkout", "*", loginArg()).withWorkingDir(repositoryFolder).runOrBomb();
    }
    
    private String loginArg() {
        return String.format("-login:%s\\%s,%s", getMaterialAttribute("domain"), getMaterialAttribute("username"), DEFAULT_PASSWORD);
    }

    private String serverArg() {
        return "-server:" + getUrl();
    }

    @Override
    public String getUrl() {
        return new TfsServer().getDefaultTfsCollectionUrl();
    }

    @Override
    public void cleanup() {
        // unmap workspace
        createCommandLine(tfCommand())
        .withArgs("workfold", "-unmap", "-workspace:" + workspaceName, serverArg(), loginArg(), repositoryFolder.getAbsolutePath()).runOrBomb(); 
        // delete folder
        RepositoryHelper.cleanup(repositoryFolder);
        // delete workspace
        createCommandLine(tfCommand())
        .withArgs("workspace", "-delete", workspaceName, serverArg(), loginArg()).runOrBomb(); 

    }

    @Override
    public void createNewFile(String fileName, String userName) {
        tfsAdd(RepositoryHelper.createFileIn(repositoryFolder, fileName));

    }

    private void tfsAdd(File file) {
        createCommandLine(tfCommand()).withArgs("add", file.getAbsolutePath(), loginArg()).withWorkingDir(repositoryFolder).runOrBomb();
    }

    @Override
    public void checkin(String message) {
        // TODO Auto-generated method stub

    }

    @Override
    public void checkin(String username, String message) {
        createCommandLine(tfCommand()).withArgs("checkin", "-comment:" + message, "-noprompt", loginArg()).withWorkingDir(repositoryFolder).runOrBomb();
    }

    @Override
    public String getRevisionFromComment(String checkinComment) {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public Revision latestRevision() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public String latestRevisionString() {
        // TODO Auto-generated method stub
        return null;
    }

    @Override
    public void modifyFile(String fileName, String userName) {
    	// checkout for edit
    	createCommandLine(tfCommand()).withArgs("checkout", fileName, loginArg()).withWorkingDir(repositoryFolder).runOrBomb();
        // then edit the file.
        RepositoryHelper.modifyFileInFolderWithText(repositoryFolder, fileName, "adding text " + UUID.randomUUID());
    }

    @Override
    public void deleteFile(String fileName, String userName) {
        throw new UnsupportedOperationException();

    }

    public static String tfCommand() {
        if(SystemUtil.isWindows()){
            return RuntimePath.absolutePathFor("tfs-tool") + "\\tf.cmd";
        }
        else{
            return RuntimePath.absolutePathFor("tfs-tool") + "/tf";
        }
    }

    @Override
    public void initatePostCommitHook(TalkToCruise talkToCruise) {
        throw new UnsupportedOperationException();
    }

}
