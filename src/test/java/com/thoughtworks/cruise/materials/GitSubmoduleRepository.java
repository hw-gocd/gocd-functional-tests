package com.thoughtworks.cruise.materials;

import java.io.File;
import java.util.List;

import org.dom4j.Element;

import com.thoughtworks.cruise.client.TalkToCruise;
import com.thoughtworks.cruise.util.TestFileUtil;

public class GitSubmoduleRepository implements Repository {
	private GitRepository parentRepo;
	private GitRepository referencedRepo;
	

	public GitSubmoduleRepository(Element material, String parentBundlePath, String submoduleBundlePath) {
		File folder = TestFileUtil.prepareFolderInsideTempFolder("sub-module-repos");
		folder.mkdirs();
		this.parentRepo = new GitRepository(material, parentBundlePath, new File(folder,"parent-repo"));
		this.referencedRepo = new GitRepository(material,submoduleBundlePath, new File(folder,"referenced-submodule"));

		this.parentRepo.initSubmodule(referencedRepo);
	}

	public void cleanup() {
		parentRepo.cleanup();
		referencedRepo.cleanup();
	}

	public void createNewFile(String fileName, String userName) {
		parentRepo.createNewFile(fileName, userName);
	}

	public void checkin(String comment) {
		parentRepo.checkin(comment);
	}

	public void checkin(String username, String comment) {
		parentRepo.checkin(username, comment);
	}

    @Override
    public String head() {
        throw new RuntimeException("not implemented");
    }

    public String getUrl() {
		return parentRepo.getUrl();
	}

	@Override
	public String getDestinationFolder() {
		return parentRepo.getDestinationFolder(); 
	}

	@Override
	public String getRevisionFromComment(String checkinComment) {
		return parentRepo.getRevisionFromComment(checkinComment);
	}

	@Override
	public boolean isForMaterial(Element material){
		return false;
	}
	
	@Override
	public boolean belongsTo(String runtimePipeline){
		return parentRepo.belongsTo(runtimePipeline);
	}
	
	public String getMaterialName() {
		return parentRepo.getMaterialName();
	}

    @Override
    public List<String> recentCommits() {
        throw new RuntimeException("Not implemented yet!");
    }

    public Repository externalRepo() {
		return referencedRepo;
	}

	@Override
	public void addFile(File file) {
		throw new UnsupportedOperationException("The material GitSubmoduleRepository is currently unable to add a file.");
	}
	
	@Override
	public void addFile(File file, String destFolder) {
		throw new UnsupportedOperationException("The material GitSubmoduleRepository is currently unable to add a file.");
	}
	
	@Override
	public Revision latestRevision() {
		return parentRepo.latestRevision();
	}

	public void updateAndCommitSubmoduleReference() {
		parentRepo.updateAndCommitSubmoduleReference(referencedRepo);
	}

	@Override 
    public void setUrl(Element element){
    	if (element.attribute("url") == null)
            return;
        element.attribute("url").setValue(getUrl());
    }

	@Override
	public void deleteFile(String fileName, String userName) {
		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public String latestRevisionString() {
		throw new UnsupportedOperationException("not implemented yet");
	}

	@Override
	public void modifyFile(String fileName, String userName) {
		throw new UnsupportedOperationException("not implemented yet");
	}

    @Override
    public void initatePostCommitHook(TalkToCruise talkToCruise) {
        throw new UnsupportedOperationException();
    }

//    @Override
//    public String getMaterialAttribute(String attribute) {
//        // TODO Auto-generated method stub
//        return null;
//    }
}