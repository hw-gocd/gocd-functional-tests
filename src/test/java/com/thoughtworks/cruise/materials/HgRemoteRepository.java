package com.thoughtworks.cruise.materials;

import static com.thoughtworks.cruise.utils.Assertions.assertWillHappen;

import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
import org.dom4j.Element;

import com.thoughtworks.cruise.utils.CommandLine;
import com.thoughtworks.cruise.utils.Console;
import com.thoughtworks.cruise.utils.EnvironmentVariableContext;
import com.thoughtworks.cruise.utils.SystemOutStreamConsumer;
import com.thoughtworks.cruise.utils.matchers.HttpMatcher;

public class HgRemoteRepository extends HgRepository {

	private Console hgDaemon; 

	public HgRemoteRepository(Element material, String bundlePath) {
		super(material, bundlePath);
		serve();
	}

	@Override
	public void cleanup() {
		stopHgServe();
		super.cleanup();
	}



	public void serve() {
		hgDaemon = CommandLine.createCommandLine("hg").withArgs("serve", "--port", "8008").
			withWorkingDir(repositoryFolder.getAbsoluteFile()).
			execute(new SystemOutStreamConsumer(HgRemoteRepository.class), new EnvironmentVariableContext());
		serverIsStarted();
	}
	
    public void serverIsStarted() {
        HttpClient client = new HttpClient();
        GetMethod get = new GetMethod(getUrl());
        assertWillHappen(client, HttpMatcher.get200(get));
    }

	@Override
	public String getUrl() {
		return "http://username:password@localhost:8008/";
	}

    public void stopHgServe() {
        hgDaemon.kill();
    }
}
