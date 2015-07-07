package com.thoughtworks.cruise.api.response;

import java.util.List;

public class PipelineHistory {
	List<PipelineInstance> pipelines;
	Pagination pagination;

	public PipelineHistory(List<PipelineInstance> pipelines,
			Pagination pagination) {
		super();
		this.pipelines = pipelines;
		this.pagination = pagination;
	}

	public List<PipelineInstance> getPipelines() {
		return pipelines;
	}

	public void setPipelines(List<PipelineInstance> pipelines) {
		this.pipelines = pipelines;
	}

	public Pagination getPagination() {
		return pagination;
	}

	public void setPagination(Pagination pagination) {
		this.pagination = pagination;
	}
}
