package com.thoughtworks.cruise.materials;

import org.dom4j.Element;

import com.thoughtworks.cruise.RuntimePath;

public class RepositoryFactory {

    public static Repository create(Element material) {
        String type = material.getName();
        if ("hg".equals(type)) {
            return "hg-remote".equals(material.attributeValue("dest")) ? 
                    new HgRemoteRepository(material, RuntimePath.pathFor("test-repos/real_connectfour.hgbundle")) : 
                    new HgRepository(material, RuntimePath.pathFor("test-repos/real_connectfour.hgbundle"));
        } else if ("git".equals(type)) {
            if ("git-submodule".equals(material.attributeValue("dest")) ||
                "git-submodule".equals(material.attributeValue("materialName"))) {
                return new GitSubmoduleRepository(material, RuntimePath.pathFor("test-repos/git/git-3-revisions.git"), RuntimePath
                        .pathFor("test-repos/git/referenced-submodule.git"));
            }
            return new GitRepository(material, RuntimePath.pathFor("test-repos/git/git-3-revisions.git"));
        } else if ("svn".equals(type)) {
        	if ("true".equals(material.attributeValue("checkexternals"))) {
                return new SvnExternalRepository(material, RuntimePath.pathFor("test-repos/svnrepo/end2end"), RuntimePath.pathFor("test-repos/svnrepo/connect4.net"));
            }
            return new SvnRepository(material, RuntimePath.pathFor("test-repos/svnrepo/end2end"));
        } else if ("p4".equals(type)) {
            return new P4Repository(material, RuntimePath.pathFor("test-repos/p4repo"));
        } else if("tfs".equals(type)){
            return new TfsRepository(material);
        }
        else {
            throw new UnsupportedOperationException("Implement me");
        }
    }

    
    public static boolean isRepository(String type) {
        return !type.equals("pipeline") && !type.equals("package");
    }
}
