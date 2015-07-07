package com.thoughtworks.cruise.api.response;

public class JobHistoryItem {
	private int id;
	private String name;
	private String state;
	private String result;
	private long scheduled_date;

	public JobHistoryItem(int id, String name, String state, String result,
			long scheduledDate) {
		super();
		this.id = id;
		this.name = name;
		this.state = state;
		this.result = result;
		this.scheduled_date = scheduledDate;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getResult() {
		return result;
	}

	public void setResult(String result) {
		this.result = result;
	}

	public long getScheduledDate() {
		return scheduled_date;
	}

	public void setScheduledDate(long scheduledDate) {
		this.scheduled_date = scheduledDate;
	}
}
