package com.thoughtworks.cruise.page;

import static org.hamcrest.MatcherAssert.assertThat;
import static org.hamcrest.Matchers.containsString;
import static org.hamcrest.Matchers.not;

import org.hamcrest.core.Is;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.state.RepositoryState;
import com.thoughtworks.cruise.state.ScenarioState;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.TimeZone;

public class AlreadyOnBuildCauseSection {    
    private final ScenarioState scenarioState;    
    private final RepositoryState repoState;
	private String materialType;
	private String materialName;
	private Browser browser;
    
	public AlreadyOnBuildCauseSection(ScenarioState scenarioState, RepositoryState repoState, Browser browser) {
        this.scenarioState = scenarioState;
        this.repoState = repoState;
        this.browser = browser;
    }
	
	private String latestRevisionNumber(String materialName) {
		return repoState.getRepoByMaterialName(scenarioState.currentRuntimePipelineName(), materialName).latestRevision().revisionNumber();
	}
	
	@com.thoughtworks.gauge.Step("Verify modification <modificationOffset> has latest revision")
	public void verifyModificationHasLatestRevision(Integer modificationOffset) throws Exception {
		verifyModificationHasRevision(modificationOffset, latestRevisionNumber(materialName));
	}

	@com.thoughtworks.gauge.Step("Verify modification <modificationOffset> has revision <revision> - Already On Build Cause Section")
	public void verifyModificationHasRevision(Integer modificationOffset, String revision) throws Exception {
		ElementStub revisionElement = elementModification(modificationOffset, "revision");
		if (materialType.equals("Pipeline"))
			assertThat(revisionElement.getText().trim(), containsString(scenarioState.expand(revision)));
		else
			assertThat(revisionElement.getText().trim(), containsString(repoState.getRevisionFromAlias(revision)));
			
	}
	   
	private ElementStub elementModification(Integer modificationOffset, String part) {
		return browser.div(part).in(browser.div(String.format("change[%d]", modificationOffset)).near(browser.div(String.format("%s - %s", materialType, materialName))));
	}

	private ElementStub buildCauseMaterial() {
		materialName = scenarioState.expand(materialName);
		ElementStub material = browser.div(String.format("%s - %s", materialType, materialName)).in(browser.div(Regex.wholeWord("build_cause")));
		if (!material.fetch("className").contains("material_name")) {
			throw new RuntimeException(String.format("Cannot find the build cause with heading %s - %s", materialType, materialName));
		}
		return material;
	}

	@com.thoughtworks.gauge.Step("Verify material has changed - Already On Build Cause Section")
	public void verifyMaterialHasChanged() throws Exception {
		ElementStub materialElement = buildCauseMaterial();
		assertThat(materialElement.parentNode().fetch("className"), containsString("changed"));
	}

	@com.thoughtworks.gauge.Step("Verify modification <modificationOffset> is checked in by <username> with comment <comment>")
	public void verifyModificationIsCheckedInByWithComment(Integer modificationOffset, String username, String comment) throws Exception {
		verifyModificationHasComment(modificationOffset, comment);
        if(username.contains(" on ")){
            String[] split = username.split(" on ");
            String timeInIST = split[1];
            java.text.DateFormat formatter= new SimpleDateFormat("yyyy-MM-dd'T'HH:mm:ssXXX");
            TimeZone timeZoneOnHost = TimeZone.getDefault();
            formatter.setTimeZone(timeZoneOnHost);
            Date parse = formatter.parse(timeInIST);
            String format = formatter.format(parse);
            username = String.format("%s on %s", split[0], format);
        }
		assertThat(elementModification(modificationOffset, "modified_by").getText().trim(), containsString(username));
	}


    public void verifyModificationHasComment(Integer modificationOffset, String comment) {
        assertThat(elementModification(modificationOffset, "comment").getText().trim(), containsString(comment));
    }

	@com.thoughtworks.gauge.Step("Verify material has not changed - Already On Build Cause Section")
	public void verifyMaterialHasNotChanged() throws Exception {
		ElementStub materialElement = buildCauseMaterial();
		assertThat(materialElement.parentNode().fetch("className"), not(containsString("changed")));
	}

	@com.thoughtworks.gauge.Step("Looking at material of type <materialType> named <materialName>")
	public void lookingAtMaterialOfTypeNamed(String materialType, String materialName) throws Exception {
		this.materialType = materialType;
		this.materialName = "Pipeline".equals(materialType) ? scenarioState.expand(materialName) : materialName;	
	}

	@com.thoughtworks.gauge.Step("Save material revision into variable <key>")
	public void saveMaterialRevisionIntoVariable(String key) throws Exception {
		ElementStub materialContainer = browser.div(String.format("%s - %s", materialType, materialName)).parentNode();
		ElementStub revisionContainer = browser.div("revision").in(materialContainer);
		String revisionString = revisionContainer.text();
		scenarioState.putValueToStore(key, revisionString.split(":")[1].trim());
	}

    @com.thoughtworks.gauge.Step("Verify modification <modificationOffset> has multi line comment with paragraph content <content> - Already On Build Cause Section")
	public void verifyModificationHasMultiLineCommentWithParagraphContent(Integer modificationOffset, String content) throws Exception {
        ElementStub commentContainer = browser.div("container").in(elementModification(modificationOffset, "comment"));
        assertThat(commentContainer.containsHTML("<p>"+ content + "</p>"), Is.is(true));
    }
}

