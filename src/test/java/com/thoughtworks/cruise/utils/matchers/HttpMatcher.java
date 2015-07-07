package com.thoughtworks.cruise.utils.matchers;

import java.io.IOException;

import org.apache.commons.httpclient.HttpClient;
import org.apache.commons.httpclient.methods.GetMethod;
import org.hamcrest.Description;
import org.hamcrest.TypeSafeMatcher;

public class HttpMatcher {
    public static TypeSafeMatcher<HttpClient> get200(final GetMethod get) {
        return new TypeSafeMatcher<HttpClient>() {
            private int i;

            public boolean matchesSafely(HttpClient client) {
                try {
                    i = client.executeMethod(get);
                    return i == 200;
                } catch (IOException e) {
                    return false;
                }
            }

            public void describeTo(Description description) {
                description.appendText("expected 200 but the response is " + i);
            }
        };
    }
}
