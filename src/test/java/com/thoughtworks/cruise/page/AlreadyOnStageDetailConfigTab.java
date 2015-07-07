package com.thoughtworks.cruise.page;

import java.io.ByteArrayInputStream;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;

import org.dom4j.DocumentException;
import org.dom4j.Element;
import org.hamcrest.core.Is;
import org.junit.Assert;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.InputSource;
import org.xml.sax.SAXException;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.CruiseConfigVerification;
import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.state.CurrentPageState;
import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public class AlreadyOnStageDetailConfigTab extends CruisePage {
	
	private CurrentPageState currentPageState;
	private final Configuration configuration;

	public AlreadyOnStageDetailConfigTab(CurrentPageState currentPageState, ScenarioState scenarioState, Browser browser, Configuration configuration) {
		super(scenarioState, true, browser);
        this.currentPageState = currentPageState;
		this.configuration = configuration;
		currentPageState.assertCurrentPageIs(CurrentPageState.Page.STAGE_DETAIL_CONFIG_TAB);
	}

	@Override
	protected String url() {
		return null;
	}
	
	@com.thoughtworks.gauge.Step("Verify notification message has <message>")
	public void verifyNotificationMessageHas(String message) throws Exception {
		ElementStub notificationContainer = browser.div("notification");
		String actualMessage = notificationContainer.getText();
		Assert.assertThat("Notification message did not match.", actualMessage.contains(message), Is.is(true));
	}

	@com.thoughtworks.gauge.Step("Verify config is visible")
	public void verifyConfigIsVisible() throws Exception {
		Assert.assertThat("Config container was not found", configContainer().exists(), Is.is(true));
	}

	public void verifyConfigShownIsTheCurrentUsedConfiguration() throws Exception {
		CruiseConfigDom currentConfigDom = configuration.provideDomAsAdmin();
		String shownConfig = configContainer().getText();
		Assert.assertThat(isCurrentConfigurationEqualsShownConfiguration(currentConfigDom, shownConfig), Is.is(true));
	}
	
	private ElementStub configContainer() {
		return browser.preformatted("content_container");
	}
	
	private boolean isCurrentConfigurationEqualsShownConfiguration(CruiseConfigDom currentConfigDom, String shownConfig) {
		DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
    	factory.setNamespaceAware(true);
    	factory.setCoalescing(true);
    	factory.setIgnoringElementContentWhitespace(true);
    	factory.setIgnoringComments(true);
    	DocumentBuilder builder;
		try {
			builder = factory.newDocumentBuilder();
			org.w3c.dom.Document doc1 = builder.parse(new InputSource(new ByteArrayInputStream(currentConfigDom.asXml().getBytes("utf-8"))));
			doc1.normalizeDocument();
			
			org.w3c.dom.Document doc2 = builder.parse(new InputSource(new ByteArrayInputStream(shownConfig.getBytes("utf-8"))));
			doc2.normalizeDocument();
			
			
		
			Node pipelines = doc1.getElementsByTagName("pipelines").item(0);
			Node otherPipelines = doc2.getElementsByTagName("pipelines").item(0);
			return pipelines.isEqualNode(otherPipelines);
		} catch (Exception e) {
			return false;
		}
	}

	@com.thoughtworks.gauge.Step("Verify <taskType> task <attributes> exists for <jobName> in <stageName> in <pipelineName> for the shown config")
	public void verifyTaskExistsForInInForTheShownConfig(String taskType, String attributes, String jobName, String stageName, String pipelineName) throws Exception {
		Assert.assertThat(getTasks(taskType, attributes, jobName, stageName, pipelineName).isEmpty(), Is.is(false));
	}
	
	@com.thoughtworks.gauge.Step("Verify <taskType> task <attributes> does not exist for <jobName> in <stageName> in <pipelineName> for the shown config")
	public void verifyTaskDoesNotExistForInInForTheShownConfig(String taskType, String attributes, String jobName, String stageName, String pipelineName) throws Exception {
		Assert.assertThat(getTasks(taskType, attributes, jobName, stageName, pipelineName).isEmpty(), Is.is(true));
	}

	private List getTasks(String taskType, String attributes, String jobName,
			String stageName, String pipelineName) throws DocumentException,
			SAXException, URISyntaxException {
		CruiseConfigDom cruiseConfigDom = new CruiseConfigDom(configContainer().getText());
		Element job = cruiseConfigDom.getJob(scenarioState.expand(pipelineName), stageName, jobName);
		List tasks = job.selectNodes(String.format("./tasks/%s%s", taskType, conditions(attributes)));
		return tasks;
	}
	
	private static Pattern TUPLE_FORM = Pattern.compile("^\\s*(.+?)\\s*:\\s*(.+?)\\s*$");
	
	private String conditions(String attributes) {
        StringBuilder builder = new StringBuilder();
        for (String attributeValueTuple : split(attributes)) {
            Matcher matcher = TUPLE_FORM.matcher(attributeValueTuple);
            if (matcher.matches()) {
                String attributeValue = matcher.group(2);
                attributeValue = scenarioState.expand(attributeValue);
                builder.append("[").
                        append(matcher.group(1)).
                        append("=").
                        append("'").append(attributeValue).append("'").
                        append("]");
            }
        }
        return builder.toString();
    }
	
	private String[] split(String runIfs) {
        String[] strings = runIfs.split("\\s*,\\s*");
        List<String> fragments = new ArrayList<String>();
        for (String string : strings) {
            fragments.add(string.trim());
        }
        return fragments.toArray(new String[0]);
    }
}
