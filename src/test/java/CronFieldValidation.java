import com.thoughtworks.cruise.editpipelinewizard.AlreadyOnGeneralOptionsPage;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class CronFieldValidation {

	
	private final AlreadyOnGeneralOptionsPage alreadyOnGeneralPage;
	private String cronTimeSpecifierValue;

	
	public CronFieldValidation(AlreadyOnGeneralOptionsPage alreadyOnGeneralPage) {
		this.alreadyOnGeneralPage = alreadyOnGeneralPage;
	}


	public void setCronFieldValue(String cronTimeSpecifierValue) throws Exception {
		this.cronTimeSpecifierValue = cronTimeSpecifierValue;
	}

	public void setValid(final boolean isValid) throws Exception {
		Assertions.waitUntil(Timeout.THIRTY_SECONDS, new Predicate() {
			public boolean call() throws Exception {
				alreadyOnGeneralPage.enterForCronTimeSpecifier(cronTimeSpecifierValue);
				alreadyOnGeneralPage.clickSave();
				return alreadyOnGeneralPage.isSavedSuccessfully() == isValid;
			}
		});
	}


	@com.thoughtworks.gauge.Step("CronFieldValidation <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Exception {
		com.thoughtworks.twist.migration.brt.BRTMigrator.BRTExecutor(table, this);
	
	}

}