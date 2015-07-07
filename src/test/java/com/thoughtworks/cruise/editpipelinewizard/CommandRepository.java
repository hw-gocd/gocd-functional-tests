package com.thoughtworks.cruise.editpipelinewizard;

import static com.thoughtworks.twist.core.execution.TwistVerification.verifyEquals;
import static junit.framework.Assert.assertNull;
import static junit.framework.Assert.assertTrue;
import static org.junit.Assert.assertThat;

import org.hamcrest.core.Is;

import net.sf.sahi.client.Browser;

public class CommandRepository {

	private final Browser browser;

	public CommandRepository(Browser browser) {
		this.browser = browser;
	}

	public void verifySnippetDetailsAreShownWithNameDescriptionAuthorWithAuthorlinkAndMoreInfo(String baseXPath, String name, String description, String author, String authorLink, String moreInfoLink) throws Exception {
		String xPathForSnippetDetailsSection = "//div[contains(@class, 'snippet_details')]";
		verifyEquals(name, browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='name']/span[@class='value']").getText());
		verifyEquals(description, browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='description']/span[@class='value']").getText());
		verifyEquals(author, browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='author']/span[@class='value-with-link']/a").getText());
		verifyEquals(authorLink, browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='author']/span[@class='value-with-link']/a").fetch("href"));
		verifyEquals(moreInfoLink, browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='more-info']/span[@class='value-with-link']/a").fetch("href"));
	}
	
	public void verifySnippetDetailsAreShownWithNameOnly(String baseXPath, String name) throws Exception {
		String xPathForSnippetDetailsSection = "//div[contains(@class, 'snippet_details')]";
		verifyEquals(name, browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='name']/span[@class='value']").getText());
		verifyEquals("No description available.", browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='description']/span[@class='value']").getText());
        assertTrue("Author is visible!", !browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='author']").isVisible());
        assertTrue("More info is visible!", !browser.byXPath(baseXPath + xPathForSnippetDetailsSection + "//div[@class='more-info']/span[@class='value-with-link']/a").isVisible());
	}

}
