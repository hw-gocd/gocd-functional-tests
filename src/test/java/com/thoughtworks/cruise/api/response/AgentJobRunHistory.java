package com.thoughtworks.cruise.api.response;

import java.util.List;

public class AgentJobRunHistory {
	List<JobInstance> jobs;
	Pagination pagination;

	public AgentJobRunHistory(List<JobInstance> jobs, Pagination pagination) {
		super();
		this.jobs = jobs;
		this.pagination = pagination;
	}

	public List<JobInstance> getJobs() {
		return jobs;
	}

	public void setJobs(List<JobInstance> jobs) {
		this.jobs = jobs;
	}

	public Pagination getPagination() {
		return pagination;
	}

	public void setPagination(Pagination pagination) {
		this.pagination = pagination;
	}
}
