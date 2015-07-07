package com.thoughtworks.cruise.utils.configfile;

import org.dom4j.Document;

import com.thoughtworks.cruise.RuntimePath;
import com.thoughtworks.cruise.util.StringUtil;

public class PackageRepository {

	public static String getPackageRepositoryLocation()
	{
		return System.getProperty("java.io.tmpdir") + "/packagerepos/";
	}
	
	public static String getYumRepoFilesLocation()
	{
		return RuntimePath.absolutePathFor("test-repos/yumrepo/rpmfiles/");
	}
	
	public static String getPackageRepositoryURI(String repoId) {
    	repoId = repoId.replace("$", "");
		return getPackageRepositoryLocation()  + repoId + StringUtil.shortUUID();
	}
	
	
	
}