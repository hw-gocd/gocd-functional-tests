import com.thoughtworks.cruise.editpipelinewizard.AlreadyOnGeneralOptionsPage;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class LabelTemplateValidations {

	private String labelTemplateValue;
	
	private final AlreadyOnGeneralOptionsPage alreadyOnGeneralPage;

	public LabelTemplateValidations(AlreadyOnGeneralOptionsPage alreadyOnGeneralPage) {
		this.alreadyOnGeneralPage = alreadyOnGeneralPage;
	}

	public void setFieldValue(String fieldValue) throws Exception {
		this.labelTemplateValue = fieldValue;
	}

	public void setValid(final boolean isValid) throws Exception {
		Assertions.waitUntil(Timeout.THIRTY_SECONDS, new Predicate() {
			public boolean call() throws Exception {
				alreadyOnGeneralPage.enterForLabelTemplate(labelTemplateValue);
				alreadyOnGeneralPage.clickSave();
				return alreadyOnGeneralPage.isSavedSuccessfully() == isValid;
			}
		});

	}

	@com.thoughtworks.gauge.Step("LabelTemplateValidations <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Exception {
		com.thoughtworks.twist.migration.brt.BRTMigrator.BRTExecutor(table, this);
	
	}

	
}