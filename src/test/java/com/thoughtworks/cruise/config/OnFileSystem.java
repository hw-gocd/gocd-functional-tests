package com.thoughtworks.cruise.config;

// JUnit Assert framework can be used for verification

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public class OnFileSystem {
	private final Configuration configuration;

	public OnFileSystem(Configuration configuration) {
		this.configuration = configuration;
	}

	@com.thoughtworks.gauge.Step("Add user <adminName> as admin")
	public void addUserAsAdmin(String adminName) throws Exception {
		CruiseConfigDom dom = configuration.provideDom();
		dom.addAdmins(adminName);
		configuration.setDomOnFileSystem(dom);
	}

}
