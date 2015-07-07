package com.thoughtworks.cruise.api.response;

import java.util.List;

public class StageHistory {
	List<StageInstance> stages;
	Pagination pagination;

	public StageHistory(List<StageInstance> stages, Pagination pagination) {
		super();
		this.stages = stages;
		this.pagination = pagination;
	}

	public List<StageInstance> getStages() {
		return stages;
	}

	public void setStages(List<StageInstance> stages) {
		this.stages = stages;
	}

	public Pagination getPagination() {
		return pagination;
	}

	public void setPagination(Pagination pagination) {
		this.pagination = pagination;
	}
}
