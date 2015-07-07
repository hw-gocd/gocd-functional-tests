package com.thoughtworks.cruise.materials;

import static com.thoughtworks.cruise.util.FileUtil.deleteFolder;

import java.io.File;

import org.apache.commons.io.FileUtils;

/**
 * @understands repo helping
 */
public class RepositoryHelper {

	public static File createFileIn(File folder, String fileName) {
		return writeToFile(folder, fileName, "content added to " + fileName);
	}
	
	public static File modifyFileIn(File folder, String fileName) {
	    return writeToFile(folder, fileName, "modifying file " + fileName);
	}

	public static File modifyFileInFolderWithText(File folder, String fileName, String text) {
		return writeToFile(folder, fileName, text);
	}

	private static File writeToFile(File folder, String fileName, String message) {
		File file = new File(folder, fileName);
		try {
			FileUtils.writeStringToFile(file, message);
		} catch (Exception e) {
			throw new RuntimeException(e);
		}
		return file;
	}

	public static void cleanup(File repositoryFolder) {
        if (repositoryFolder.exists()) {
            deleteFolder(repositoryFolder);
        }
	}

}
