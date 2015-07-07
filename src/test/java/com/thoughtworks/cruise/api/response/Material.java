package com.thoughtworks.cruise.api.response;

public class Material {
	private int id;
	private String fingerprint;
	private String type;
	private String description;

	public Material(int id, String fingerprint, String type, String description) {
		super();
		this.id = id;
		this.fingerprint = fingerprint;
		this.type = type;
		this.description = description;
	}

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getFingerprint() {
		return fingerprint;
	}

	public void setFingerprint(String fingerprint) {
		this.fingerprint = fingerprint;
	}

	public String getType() {
		return type;
	}

	public void setType(String type) {
		this.type = type;
	}

	public String getDescription() {
		return description;
	}

	public void setDescription(String description) {
		this.description = description;
	}
}
