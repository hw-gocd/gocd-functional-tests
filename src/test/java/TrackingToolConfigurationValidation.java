
import org.junit.Assert;

import com.thoughtworks.cruise.editpipelinewizard.AlreadyOnProjectManagementPage;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.Assertions.Predicate;

public class TrackingToolConfigurationValidation {

    private AlreadyOnProjectManagementPage alreadyOnProjectManagementPage;

    private String trackingToolURL;

    private String regexValue;

    public TrackingToolConfigurationValidation(AlreadyOnProjectManagementPage alreadyOnProjectManagementPage) {
        this.alreadyOnProjectManagementPage = alreadyOnProjectManagementPage;
    }

    public void setMessageForRegex(String messageForRegex) throws Exception {
        Assert.assertTrue("Error message on URL not present or different.",
                alreadyOnProjectManagementPage.isMessagePresent(messageForRegex));
    }

    public void setMessageForSaveStatus(final String messageForSaveStatus) throws Exception {
        Assertions.waitUntil(Timeout.THIRTY_SECONDS, new Predicate() {
            public boolean call() throws Exception {
                alreadyOnProjectManagementPage.enterForTrackingToolURL(trackingToolURL);
                alreadyOnProjectManagementPage.enterTrackingToolRegex(regexValue);
                alreadyOnProjectManagementPage.clickSave();
                return alreadyOnProjectManagementPage.isMessagePresent(messageForSaveStatus);
            }
        });
    }

    public void setMessageForURL(String messageForURL) throws Exception {
        Assert.assertTrue("Error message on URL not present or different.", alreadyOnProjectManagementPage.isMessagePresent(messageForURL));
    }

    public void setRegexValue(String regexValue) throws Exception {
        this.regexValue = regexValue;
    }

    public void setURLValue(String urlValue) throws Exception {
        this.trackingToolURL = urlValue;
    }

	@com.thoughtworks.gauge.Step("TrackingToolConfigurationValidation <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Throwable {
		com.thoughtworks.twist.migration.brt.BRTMigrator brtMigrator = new com.thoughtworks.twist.migration.brt.BRTMigrator();
		try {
			brtMigrator.BRTExecutor(table, this);
		} catch (Exception e) {
			throw e.getCause();
		}
	}

}