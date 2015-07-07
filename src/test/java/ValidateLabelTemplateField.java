import net.sf.sahi.client.Browser;

public class ValidateLabelTemplateField {

	private Browser browser;

	private String enteredValue;

	private String message;

	public ValidateLabelTemplateField(Browser browser) {
		this.browser = browser;
	}

	public void setEnteredValue(String enteredValue) throws Exception {
		this.enteredValue = enteredValue;
	}

	public void setMessage(String message) throws Exception {
		this.message = message;
	}

	public void setUp() throws Exception {
		//Put the code to be executed before execution of each row
	}

	public void tearDown() throws Exception {
		//Put the code to be executed after execution of each row
	}

}