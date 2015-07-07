package com.thoughtworks.cruise.materials;

import java.io.File;
import java.util.List;

import org.dom4j.Element;

import com.thoughtworks.cruise.client.TalkToCruise;

public interface Repository {	
	String getUrl();
	void cleanup();
	void createNewFile(String file, String userName);
	void addFile(File file);
	void addFile(File file, String destFolder);
	void checkin(String message);
	void checkin(String username, String message);
    String head();
	String getDestinationFolder();
	String getRevisionFromComment(String checkinComment);	
	String getMaterialName();
    List<String> recentCommits();
	boolean belongsTo(String runtimePipeline);
	boolean isForMaterial(Element material);
	Repository externalRepo();
    Revision latestRevision();
    String latestRevisionString();
    void setUrl(Element element);
	void modifyFile(String fileName, String userName);
	void deleteFile(String fileName, String userName);
    //String getMaterialAttribute(String attribute);
    void initatePostCommitHook(TalkToCruise talkToCruise);
}
