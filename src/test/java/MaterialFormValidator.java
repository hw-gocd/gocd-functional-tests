import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.editpipelinewizard.AlreadyOnEditMaterialPopup;
import com.thoughtworks.cruise.editpipelinewizard.AlreadyOnMaterialListingPage;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;

public class MaterialFormValidator {

    private Browser browser;

    private String field;

    private String elementType;

    private AlreadyOnEditMaterialPopup materialPopup;

    private AlreadyOnMaterialListingPage materialListingPage;

    private final CurrentPageState currentPageState;

    private final ScenarioState scenarioState;

    public MaterialFormValidator(Browser browser, CurrentPageState currentPageState, ScenarioState scenarioState, Configuration configuration) {
        this.browser = browser;
        this.currentPageState = currentPageState;
        this.scenarioState = scenarioState;
        materialListingPage = new AlreadyOnMaterialListingPage(currentPageState, scenarioState, browser, configuration);
    }

    private ElementStub element() {
        return new ElementStub(elementType, browser, this.field);
    }

    public String message() throws Exception {
        materialPopup = new AlreadyOnEditMaterialPopup(currentPageState, scenarioState, browser);
        materialPopup.clickSave();
        return browser.div("form_error").in(element().parentNode().parentNode()).getText();
    }

    public void setElementType(String elementType) throws Exception {
        this.elementType = elementType;
    }

    public void setField(String field) throws Exception {
        this.field = String.format("material[%s]", field);
    }

    public void setMaterialName(String materialName) throws Exception {
        materialListingPage.editMaterial(materialName);
    }

    public void setUp() throws Exception {
    }

    public void setValue(String value) throws Exception {
        element().setValue(value);
    }

    public void tearDown() throws Exception {
        materialPopup.close();
    }

	@com.thoughtworks.gauge.Step("MaterialFormValidator <table>")
	public void brtMethod(com.thoughtworks.gauge.Table table) throws Throwable {
		com.thoughtworks.twist.migration.brt.BRTMigrator brtMigrator = new com.thoughtworks.twist.migration.brt.BRTMigrator();
		try {
			brtMigrator.BRTExecutor(table, this);
		} catch (Exception e) {
			throw e.getCause();
		}
	}
}