package com.thoughtworks.cruise.api.response;

public class Modification {
	private int id;
	private String revision;
	private String comment;
	private long modified_time;
	private String user_name;
	private String email_address;

	public Modification(int id, String revision, String comment,
			long modifiedTime, String userName, String emailAddress) {
		super();
		this.id = id;
		this.revision = revision;
		this.comment = comment;
		this.modified_time = modifiedTime;
		this.user_name = userName;
		this.email_address = emailAddress;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getRevision() {
		return revision;
	}

	public void setRevision(String revision) {
		this.revision = revision;
	}

	public String getComment() {
		return comment;
	}

	public void setComment(String comment) {
		this.comment = comment;
	}

	public long getModifiedTime() {
		return modified_time;
	}

	public void setModifiedTime(long modifiedTime) {
		this.modified_time = modifiedTime;
	}

	public String getUserName() {
		return user_name;
	}

	public void setUserName(String userName) {
		this.user_name = userName;
	}

	public String getEmailAddress() {
		return email_address;
	}

	public void setEmailAddress(String emailAddress) {
		this.email_address = emailAddress;
	}
}
