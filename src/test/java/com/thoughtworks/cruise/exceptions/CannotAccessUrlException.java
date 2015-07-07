package com.thoughtworks.cruise.exceptions;

import com.thoughtworks.cruise.client.TalkToCruise.CruiseResponse;

public class CannotAccessUrlException extends RuntimeException {

	private final CruiseResponse cruiseResponse;

	public CannotAccessUrlException(CruiseResponse cruiseResponse) {
		this.cruiseResponse = cruiseResponse;
	}

	private static final long serialVersionUID = 1L;

	public CruiseResponse getCruiseResponse() {
		return cruiseResponse;
	}
}
