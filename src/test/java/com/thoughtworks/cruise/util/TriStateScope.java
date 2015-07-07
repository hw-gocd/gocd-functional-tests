package com.thoughtworks.cruise.util;

import static org.junit.Assert.assertThat;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import org.apache.commons.lang.StringUtils;
import org.hamcrest.Matchers;
import org.hamcrest.core.Is;

import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;

public class TriStateScope {
    private String scope;
    private final Browser browser;
    private List<String> fieldNames;

    public TriStateScope(Browser browser, String scope, String... fieldNames) {
        this.browser = browser;
        this.scope = scope;
        this.fieldNames = new ArrayList<String>();
        this.fieldNames.add("selections");
        this.fieldNames.addAll(Arrays.asList(fieldNames));
    }
    
    public void set(String stateMap) throws Exception {
        for (String resourceWithState : stateMap.split(", ")) {
            String[] resourceStatusArray = resourceWithState.split(":");
            String resourceName = resourceStatusArray[0];
            String state = resourceStatusArray[1];
            do {
                clickElem(resourceName);
            } while (!getMicrocontentTriStateElement(resourceName).fetch("className").contains(state));
            assertThat(valueHolder(resourceName) .getValue(), Matchers.is(state));
        }
    }
    
    public void clickElem(final String triStateName) throws Exception {
        clickElem(triStateName, true);
    }

    private void clickElem(final String triStateName, final boolean assertStateChange) throws Exception {
        final String initialValue = valueHolder(triStateName).getValue();

        Assertions.waitUntil(Timeout.TWENTY_SECONDS, new Predicate() {
            public boolean call() throws Exception {
                getMicrocontentTriStateElement(triStateName).click();
                if (assertStateChange) {
                    Assertions.waitUntil(Timeout.TEN_SECONDS, new Predicate() {
                        public boolean call() throws Exception {
                            ElementStub refreshedValueHolderElement = valueHolder(triStateName);
                            return !initialValue.equals(refreshedValueHolderElement.getValue());
                        }
                    });
                }
                return true;
            }
        });
    }
    
    public void assertTransitions(final String triStateName, String states) throws Exception {
        String[] expectedStateChangeSequence = states.split(", ");
        List<String> actualStateChangeSequence = new ArrayList<String>();
        for (String ignore : expectedStateChangeSequence) {
            clickElem(triStateName);
            actualStateChangeSequence.add(valueHolder(triStateName).getValue());
        }
        assertThat(StringUtils.join(actualStateChangeSequence, ", "), Matchers.is(states));
    }
    
    public void assertShows(String triStatesMap) throws Exception {
        for (String resourceWithState : triStatesMap.split(", ")) {
            String[] resourceStatusArray = resourceWithState.split(":");
            ElementStub selectBox = valueHolder(resourceStatusArray[0]);
            assertThat(selectBox.getValue(), Matchers.is(resourceStatusArray[1]));
        }
    }
    
    private ElementStub valueHolder(String triStateName) throws Exception {
        for (String fieldName : fieldNames) {
            ElementStub elem = browser.select(String.format("%s[%s]", fieldName, triStateName)).in(scope());
            if (elem.exists()) {
                return elem;
            }
        }
        throw new RuntimeException(String.format("tri-state select with name '%s' not found under field names '%s'", triStateName, StringUtils.join(fieldNames, ',')));
    }

    private ElementStub scope() {
        return browser.div(scope);
    }

    private ElementStub getMicrocontentTriStateElement(String triStateName) {
        return browser.span(triStateName).in(scope());
    }

    public void assertDisabledWithMessage(String triStateName, String message) throws Exception {
        ElementStub valueHolder = valueHolder(triStateName);
        ElementStub messagePane = browser.div("tristate_disabled_message").in(valueHolder.parentNode());
        assertThat(messagePane.text(), Is.is(message));
        //ensure value doesn't change
        String value = valueHolder.value();
        clickElem(triStateName, false);
        assertThat(valueHolder.value(), Is.is(value));
    }

    public void assertEnabled(String triStateName) {
        
    }
}
