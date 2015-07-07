package com.thoughtworks.cruise.api.response;

public class Pagination {
	private int offset;
	private int total;
	private int page_size;

	public Pagination(int offset, int total, int pageSize) {
		super();
		this.offset = offset;
		this.total = total;
		this.page_size = pageSize;
	}

	public int getOffset() {
		return offset;
	}

	public void setOffset(int offset) {
		this.offset = offset;
	}

	public int getTotal() {
		return total;
	}

	public void setTotal(int total) {
		this.total = total;
	}

	public int getPageSize() {
		return page_size;
	}

	public void setPageSize(int pageSize) {
		this.page_size = pageSize;
	}
}
