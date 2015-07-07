package com.thoughtworks.cruise.matchers;

import org.hamcrest.Description;
import org.junit.matchers.TypeSafeMatcher;

import com.thoughtworks.cruise.util.SystemUtil;

public abstract class ResourceMatcher extends TypeSafeMatcher<String> {

    public static final ResourceMatcher RESOURCE_EXISTS = new ResourceMatcher() {
        public boolean matchesSafely(String item) {
            return true;
        }

        public void describeTo(Description description) {
            description.appendText("resource exists");
        }
    };

    public static final ResourceMatcher VALID_CONFIG_FILE = new ResourceMatcher() {
        private String current;

        public boolean matchesSafely(String item) {
            this.current = item;
            return !item.contains("FlashMessageLauncher.error(");
        }

        public void describeTo(Description description) {
            System.err.println("config file:\n" + current);
            description.appendText("valid config file");
        }
    };

    public static TypeSafeMatcher<Boolean> portIsOccupied(final int port) {
        return new TypeSafeMatcher<Boolean>() {
            public boolean matchesSafely(Boolean exptected) {
                return SystemUtil.isLocalPortOccupied(port) == exptected;
            }

            public void describeTo(Description description) {
                description.appendText("port [" + port + "] is free, probably means "
                        + "the application did start up correcly");
            }
        };
    }

}
