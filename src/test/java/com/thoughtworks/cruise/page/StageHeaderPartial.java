package com.thoughtworks.cruise.page;

import static com.thoughtworks.cruise.Regex.matches;
import static com.thoughtworks.cruise.Regex.wholeWord;
import static java.lang.String.format;
import static org.hamcrest.MatcherAssert.assertThat;
import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import org.hamcrest.core.Is;

import com.thoughtworks.cruise.state.ScenarioState;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Function;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class StageHeaderPartial {

	private final CruisePage page;
	private final Browser browser;

	public static final String ACTION_XPATH = "//div[contains(@id, 'stage_bar_') and ./*[contains(@class, 'stage_name') and .='%s']]/div[contains(@class, 'operate')]";
	public static final String RE_RUN = "Rerun";
	public static final String TRIGGER = "Trigger";
	public static final String CANCEL = "Cancel";

	public StageHeaderPartial(ScenarioState scenarioState, CruisePage page, Browser browser) {
		this.page = page;
		this.browser = browser;
	}
	
	private void triggerAction(final String stage, final String actionName) {
		Assertions.waitUntil(Timeout.TWO_MINUTES, new Predicate() {
			@Override
			public boolean call() throws Exception {
				page.reloadPage();
				ElementStub action;
				if(TRIGGER.equals(actionName)) {
					action = browser.link(wholeWord(String.format("stage_bar_trigger_%s", stage)));
					if (!action.exists()) {
						return false;
					}
				} else {
					action = getAction(stage);
					if (!isAction(action, actionName)) {
					    return false;
					}
					action = getActionLink(stage);
				}
				action.click();
				return true;
			}

		});
	}

    private boolean isAction(ElementStub actionElement, final String actionName) {
        return actionElement.isVisible() && actionElement.fetch("className").contains(format("action_%s", actionName.toLowerCase()));
    }            

	private ElementStub getActionLink(String stage) {
		return browser.link(wholeWord("stage_action")).in(getAction(stage));
	}
	
	private ElementStub getAction(String stage) {
        return browser.div(matches(format("operate_%s", stage)));
	}

	public void rerunStage(String stage) {
		triggerAction(stage, RE_RUN);
	}
	
	public void cancel(String stage) throws Exception {
		triggerAction(stage, CANCEL);
	}
	
	public void triggerStage(String stage) throws Exception {
        triggerAction(stage, TRIGGER);
    }   
	
	public void verifyStageHasAction(final String stage, final String actionName) throws Exception {
		Assertions.waitUntil(Timeout.TEN_SECONDS, new Predicate() {			
			public boolean call() throws Exception {
				page.reloadPage();
			    if (!stageHasAction(stage, actionName)) {
			        return false;
			    }
			    return true;
			}
		});
	}

	public void verifyStageDoesNotHaveAction(String stage, String actionName) {
    	assertThat(stageHasAction(stage, actionName), Is.is(false));
	}
	
    public void verifyStageDoesNotHaveAnyAction(final String stage) throws Exception {
        Assertions.waitUntil(Timeout.TEN_SECONDS, new Predicate() {

            @Override
            public boolean call() throws Exception {
                page.reloadPage();
                return noActionsPresent(stage);
            }
        });
        Assertions.assertOverTime(Timeout.TEN_SECONDS, new Function<Boolean>() {

            @Override
            public Boolean call() {
                page.reloadPage();
                return noActionsPresent(stage);
            }
        });
    }
	
    private boolean stageHasAction(final String stage, final String actionName) {
        return isAction(getAction(stage), actionName);
    }

	private boolean noActionsPresent(final String stage) {
		return (stageHasAction(stage, TRIGGER) || stageHasAction(stage, CANCEL) || stageHasAction(stage, RE_RUN)) == false;
	}
}
