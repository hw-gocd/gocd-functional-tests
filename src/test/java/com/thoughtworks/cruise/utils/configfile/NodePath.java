package com.thoughtworks.cruise.utils.configfile;

import static com.thoughtworks.cruise.util.ExceptionUtils.bombIf;

import java.util.ArrayList;

public class NodePath {
    private ArrayList<Entry<CruiseConfigTag>> queue;

    public NodePath(CruiseConfigTag... nodes) {
        queue = new ArrayList<Entry<CruiseConfigTag>>(nodes.length);
        for (CruiseConfigTag node : nodes) {
            queue.add(wrap(node));
        }
    }

    public CruiseConfigTag first() {
        if (queue.isEmpty()) {
            return null;
        }
        return queue.get(0).obj;
    }

    public CruiseConfigTag next(CruiseConfigTag node) {
        int i = queue.indexOf(wrap(node));
        bombIf(i < 0, "Illegal argument");
        if (i + 1 < queue.size()) {
            return queue.get(i + 1).obj;
        }
        return null;
    }
    public CruiseConfigTag childOf(Entry<CruiseConfigTag> wrap) {
        int i = queue.indexOf(wrap);
        bombIf(i < 0, "Illegal argument");
        if (i + 1 < queue.size()) {
            return queue.get(i + 1).obj;
        }
        return null;
    }

    private Entry<CruiseConfigTag> wrap(CruiseConfigTag node) {
        return new Entry<CruiseConfigTag>(node);
    }

    public Entry<CruiseConfigTag> get(int index) {
        return queue.get(index - 1);
    }

    private static class Entry<T> {
        T obj;

        private Entry(T obj) {
            this.obj = obj;
        }

        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }

            Entry entry = (Entry) o;
            return obj == entry.obj;
        }

        public int hashCode() {
            return obj.hashCode();
        }
    }

}
