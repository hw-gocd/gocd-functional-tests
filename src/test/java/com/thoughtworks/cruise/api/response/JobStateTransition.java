package com.thoughtworks.cruise.api.response;

public class JobStateTransition {
	private int id;
	private String state;
	private long state_change_time;

	public JobStateTransition(int id, String state, long stateChangeTime) {
		super();
		this.id = id;
		this.state = state;
		this.state_change_time = stateChangeTime;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public long getStateChangeTime() {
		return state_change_time;
	}

	public void setStateChangeTime(long stateChangeTime) {
		this.state_change_time = stateChangeTime;
	}
}
