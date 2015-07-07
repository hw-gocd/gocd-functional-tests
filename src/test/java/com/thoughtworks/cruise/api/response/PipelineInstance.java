package com.thoughtworks.cruise.api.response;

import java.util.List;

public class PipelineInstance {
	private int id;
	private String name;
	private int counter;
	private float natural_order;
	private String label;
	private boolean can_run;
	private boolean preparing_to_schedule;
	private List<StageHistoryItem> stages;

	public PipelineInstance(int id, String name, int counter,
			float naturalOrder, String label, boolean canRun,
			boolean preparingToSchedule, List<StageHistoryItem> stages) {
		super();
		this.id = id;
		this.name = name;
		this.counter = counter;
		this.natural_order = naturalOrder;
		this.label = label;
		this.can_run = canRun;
		this.preparing_to_schedule = preparingToSchedule;
		this.stages = stages;
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

	public int getCounter() {
		return counter;
	}

	public void setCounter(int counter) {
		this.counter = counter;
	}

	public float getNaturalOrder() {
		return natural_order;
	}

	public void setNaturalOrder(float naturalOrder) {
		this.natural_order = naturalOrder;
	}

	public String getLabel() {
		return label;
	}

	public void setLabel(String label) {
		this.label = label;
	}

	public boolean isCanRun() {
		return can_run;
	}

	public void setCanRun(boolean canRun) {
		this.can_run = canRun;
	}

	public boolean isPreparingToSchedule() {
		return preparing_to_schedule;
	}

	public void setPreparingToSchedule(boolean preparingToSchedule) {
		this.preparing_to_schedule = preparingToSchedule;
	}

	public List<StageHistoryItem> getStages() {
		return stages;
	}

	public void setStages(List<StageHistoryItem> stages) {
		this.stages = stages;
	}
}
