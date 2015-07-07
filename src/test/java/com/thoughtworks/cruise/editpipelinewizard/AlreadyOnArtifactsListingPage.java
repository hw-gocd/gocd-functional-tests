package com.thoughtworks.cruise.editpipelinewizard;

// JUnit Assert framework can be used for verification

import static junit.framework.Assert.assertEquals;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.state.ConfigState;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.state.CurrentPageState.Page;

import net.sf.sahi.client.Browser;

// JUnit Assert framework can be used for verification

public class AlreadyOnArtifactsListingPage extends AlreadyOnEditPipelineWizardPage

{

	
	public AlreadyOnArtifactsListingPage(Browser browser, CurrentPageState currentPageState, ScenarioState scenarioState) {
		super(currentPageState,scenarioState,browser);
		currentPageState.assertCurrentPageIs(Page.PIPELINE_WIZARD_ARTIFACTS_LISTING_PAGE);	
	}

	
	
	@com.thoughtworks.gauge.Step("Enter artifact detail <listingId> <source> <destination> <type>")
	public void enterArtifactDetail(Integer listingId,String source, String destination, String type)
	{
		
		String listingIdString = "";
		if(!artifactExists(listingId)) createEmptyArtifact(listingId);
		listingId = listingId -1 ;
		
		listingIdString = (listingId == 0) ? "" : "[" + listingId + "]" ;
		
		browser.textbox("job[artifactPlans][][src]" + listingIdString).setValue(source);
		browser.textbox("job[artifactPlans][][dest]" + listingIdString).setValue(destination);
		browser.select("job[artifactPlans][][artifactTypeValue]" + listingIdString).choose(type);
	}
	
	
	private void createEmptyArtifact(Integer listingId) {
		browser.link("Add").click(); 
		
	}

	private boolean artifactExists(Integer listingId) {
		
		listingId--;
		return ( (listingId == 0) ? browser.textbox("job[artifactPlans][][src]").exists() : browser.textbox("job[artifactPlans][][src][" + listingId + "]").exists());  
		

	}

	
	@com.thoughtworks.gauge.Step("Click save - Already on Artifacts Listing Page")
	public void clickSave() throws Exception {
		super.clickSave();
	}

	@com.thoughtworks.gauge.Step("Verify saved successfully - Already on Artifacts Listing Page")
	public void verifySavedSuccessfully() {
		super.verifySavedSuccessfully();
	}

	@com.thoughtworks.gauge.Step("Assert mD5 - Already On Artifacts Listing Page")
	public void assertMD5() throws Exception {
    	String md5value = scenarioState.getValueFromStore(ConfigState.md5key);
    	assertEquals(browser.hidden("config_md5").getValue(), md5value);
    }
	
	  @com.thoughtworks.gauge.Step("Go to environment variables page - Already On Artifacts Listing Page")
	public void goToEnvironmentVariablesPage() throws Exception {
	        super.goToEnvironmentVariablesPage();
	    }

}
