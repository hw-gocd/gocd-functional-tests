package com.thoughtworks.cruise.api.response;

import java.util.List;

public class MaterialRevision {
	private Material material;
	private boolean changed;
	private List<Modification> modifications;

	public MaterialRevision(Material material, boolean changed,
			List<Modification> modifications) {
		super();
		this.material = material;
		this.changed = changed;
		this.modifications = modifications;
	}

	public Material getMaterial() {
		return material;
	}

	public void setMaterial(Material material) {
		this.material = material;
	}

	public boolean isChanged() {
		return changed;
	}

	public void setChanged(boolean changed) {
		this.changed = changed;
	}

	public List<Modification> getModifications() {
		return modifications;
	}

	public void setModifications(List<Modification> modifications) {
		this.modifications = modifications;
	}
}
