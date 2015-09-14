import org.junit.Assert;

import com.thoughtworks.cruise.editpipelinewizard.AlreadyOnProjectManagementPage;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.Assertions.Predicate;

public class MingleCardActivityConfigurationValidation {

    private String mingleURL;

    private String mingleProjectIdentifier;

    private final AlreadyOnProjectManagementPage alreadyOnProjectManagementPage;

    private String groupingCondition;

    public MingleCardActivityConfigurationValidation(AlreadyOnProjectManagementPage alreadyOnProjectManagementPage) {
        this.alreadyOnProjectManagementPage = alreadyOnProjectManagementPage;
    }

    public void setErrOnProjectId(String messageForMingleProjectIdentifier) throws Exception {
        Assert.assertTrue("Error on Mingle Project Identifier is not present or different", alreadyOnProjectManagementPage.isMessagePresent(messageForMingleProjectIdentifier));
    }

    public void setErrOnUrl(String messageForMingleURL) throws Exception {
        Assert.assertTrue("Error on Mingle URL is not present or different", alreadyOnProjectManagementPage.isMessagePresent(messageForMingleURL));
    }

    public void setErrOnMQL(String messageForMQLGroupingConditions) throws Exception {
        Assert.assertTrue("Error on MQL grouping conditions is not present or different", alreadyOnProjectManagementPage.isMessagePresent(messageForMQLGroupingConditions));
    }

    public void setResponseOnSave(final String messageForSaveStatus) throws Exception {
        Assertions.waitUntil(Timeout.THIRTY_SECONDS, new Predicate() {

            public boolean call() throws Exception {
                alreadyOnProjectManagementPage.enterForMingleProjectIdentifier(mingleProjectIdentifier);
                alreadyOnProjectManagementPage.enterForMingleURL(mingleURL);
                alreadyOnProjectManagementPage.enterForMQAGroupingConditions(groupingCondition);
                alreadyOnProjectManagementPage.clickSave();
                return alreadyOnProjectManagementPage.isMessagePresent(messageForSaveStatus);
            }
        });

    }

    public void setMingleProjectIdentifier(String mingleProjectIdentifier) throws Exception {
        this.mingleProjectIdentifier = mingleProjectIdentifier;
    }

    public void setMingleURL(String mingleURL) throws Exception {
        this.mingleURL = mingleURL;
    }

    public void setGroupingCondition(final String groupingCondition) throws Exception {
        this.groupingCondition = groupingCondition;
    }

	@com.thoughtworks.gauge.Step("MingleCardActivityConfigurationValidation <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Throwable {
		com.thoughtworks.twist.migration.brt.BRTMigrator brtMigrator = new com.thoughtworks.twist.migration.brt.BRTMigrator();
		try {
			brtMigrator.BRTExecutor(table, this);
		} catch (Exception e) {
			throw e.getCause();
		}
	}

}