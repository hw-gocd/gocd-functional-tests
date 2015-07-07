package com.thoughtworks.cruise.api.feeds;

import org.dom4j.Document;

import com.thoughtworks.cruise.api.ApiHelper;
import com.thoughtworks.cruise.state.ScenarioState;

public abstract class FeedXml {
	protected final ScenarioState state;
	protected final ApiHelper apiHelper;
	private Document feed;

	protected FeedXml(ScenarioState state){
		this.state = state;
		this.apiHelper = new ApiHelper(state);
	}

	protected Document feed() {
		if (feed == null) {
			try {
				feed = apiHelper.loadXmlDocumentFromUrl(feedUrl());
				System.out.println(this.getClass().getSimpleName() + ": ");
				System.out.println(feed.asXML());
			} catch (Exception e) {	
				throw new RuntimeException(e);
			}
		}
		return feed;
	}

	protected abstract String feedUrl();

}
