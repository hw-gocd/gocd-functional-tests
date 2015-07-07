package com.thoughtworks.cruise.editpipelinewizard;


import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class ArtifactsValidation {

	
	
	private String source;

	private String destination;

	private String messageForSource;

	private String messageForDestination;

	private String saveStatus;

	private boolean expected;
	
	private final String escapedCharacter = "|";
	
	private final String escapeCharacter = ":";

	private AlreadyOnArtifactsListingPage artifactsPage;

	public ArtifactsValidation(AlreadyOnArtifactsListingPage alreadyOnArtifactsListingPage)
	{
		this.artifactsPage = alreadyOnArtifactsListingPage;
		
	}
	
	
	public void setDestination(final String destination) throws Exception {
		this.destination = destination;		
			
	}

	public void setExpected(final boolean expected) throws Exception {
		this.expected = expected;
		
		Assertions.waitUntil(Timeout.THIRTY_SECONDS, new Predicate() {

			public boolean call() throws Exception {
				
				artifactsPage.enterArtifactDetail(1, source, destination, "Build Artifact");
				artifactsPage.clickSave();
					
				return (( artifactsPage.isMessagePresent(messageForDestination) && artifactsPage.isMessagePresent(messageForSource) && artifactsPage.isMessagePresent(saveStatus)) == expected);			
				
						
			}
		});
	}

	public void setMessageForDestination(final String messageForDestination)
			throws Exception {
		this.messageForDestination = messageForDestination.replaceAll(escapeCharacter, escapedCharacter);
		System.out.println(this.messageForDestination);
	}

	public void setMessageForSource(final String messageForSource) throws Exception {
		this.messageForSource = messageForSource.replaceAll(escapeCharacter, escapedCharacter);
		System.out.println(this.messageForSource);
	}

	public void setSaveStatus(final String saveStatus) throws Exception {
		this.saveStatus = saveStatus;
	}

	public void setSource(final String source) throws Exception {
		this.source = source;
	}


	@com.thoughtworks.gauge.Step("ArtifactsValidation <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Exception {
		com.thoughtworks.twist.migration.brt.BRTMigrator.BRTExecutor(table, this);
	
	}

	
}
