package com.thoughtworks.cruise.state;

import java.io.File;

public class ArtifactFilesystem {
    public final File fileSystem = new File(System.getProperty("java.io.tmpdir"), "filesystem.img");
    
    
}
