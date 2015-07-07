package com.thoughtworks.cruise.editpipelinewizard;

import static com.thoughtworks.twist.core.execution.TwistVerification.verify;
import static com.thoughtworks.twist.core.execution.TwistVerification.verifyEquals;

import java.util.ArrayList;
import java.util.List;

import net.sf.sahi.client.Browser;
import net.sf.sahi.client.ElementStub;

import com.thoughtworks.cruise.Regex;
import com.thoughtworks.cruise.SahiBrowserWrapper;

public class AutoCompleteSuggestions {

    private final Browser browser;
    private final SahiBrowserWrapper browserWrapper;

    public AutoCompleteSuggestions(Browser browser, SahiBrowserWrapper browserWrapper) {
        this.browser = browser;
        this.browserWrapper = browserWrapper;
    }

    public void autoCompleteShouldNotHave(String suggestion) {
        List<ElementStub> listOfSelectedSuggestions = firstSuggestion();
        for (ElementStub element : listOfSelectedSuggestions) {
            if (element.exists() && suggestion.equals(element.getText().trim())) {
            	verify(String.format("Suggestion '%s' is found, but was not expected", suggestion), false);
            }
        }
    }

    public List<ElementStub> firstSuggestion() {
        return browserWrapper.collectIn("listItem", Regex.wholeWord("ac_over"), browser.div("ac_results"));
    }
    
    public List<ElementStub> allSuggestion(int zeroBasedTextboxIndex) {
        return getSuggestionDropdown(getContainerDiv(zeroBasedTextboxIndex));
    }

    public List<String> allSuggestionTexts(int zeroBasedTextboxIndex) {
        List<String> texts = new ArrayList<String>();
        for (ElementStub suggestion : allSuggestion(zeroBasedTextboxIndex)) {
            texts.add(suggestion.getText());
        }
        return texts;
    }

    public void autoCompletesShouldShowSuggestion(String suggestion) { 
        autoCompletesShouldShowSuggestion(0, new FindSuggestion(suggestion));
    }

    public void autoCompletesShouldShowSuggestion(int zeroBasedTextboxIndex, String suggestion) {
        autoCompletesShouldShowSuggestion(zeroBasedTextboxIndex, new FindSuggestion(suggestion));
    }

    public void autoCompletesShouldShowSuggestion(int textboxIndex, final SuggestionHandler handler) {
        final String containerDiv = getContainerDiv(textboxIndex);
        List<ElementStub> listOfSelectedSuggestions = getSuggestionDropdown(containerDiv);
        for (ElementStub element : listOfSelectedSuggestions) {
            if (handler.matches(element.getText().trim())) {
                return;
            }
        }
        verify(handler.notFoundError() + " - Suggestions found: " + allSuggestionTexts(textboxIndex), false);
    }

    private List<ElementStub> getSuggestionDropdown(final String containerDiv) {
		return browserWrapper.collectIn("listItem", Regex.startsWith("ac_"), browser.div(containerDiv));
	}

    public void selectFirstOption() {
       selectOption(0, 0); 
    }
    
    public void selectOption(int suggestionIndex, int textboxIndex) {
        String containerDiv = getContainerDiv(textboxIndex);
        getSuggestionDropdown(containerDiv).get(suggestionIndex).click();
    }

    private String getContainerDiv(int index) {
        return index == 0 ? "ac_results" : String.format("ac_results[%s]", index);
    }

    public static class FindSuggestion implements SuggestionHandler {
        private String suggestion;

        public FindSuggestion(String suggestion) {
            this.suggestion = suggestion;
        }

        public boolean matches(String givenSuggestion) {
            return suggestion.equals(givenSuggestion);
        }

        @Override
        public String notFoundError() {
            return String.format("Suggestion '%s' is not found", suggestion);
        }
    }
    
    public static class CountSuggestion implements SuggestionHandler {
        private int total;
        private final int expectedTotal;

        public CountSuggestion(int total) {
            expectedTotal = total;
            this.total = total;
            
        }

        public boolean matches(String givenSuggestion) {
            return --total == 0;
        }

        @Override
        public String notFoundError() {
            return String.format("Expected atleast %s suggestion, found %s.", expectedTotal, expectedTotal - total);
        }
    }

    public static interface SuggestionHandler {
        boolean matches(String givenSuggestion);

        String notFoundError();
    }
}
