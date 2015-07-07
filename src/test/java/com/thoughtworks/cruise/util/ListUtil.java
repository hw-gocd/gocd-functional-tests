package com.thoughtworks.cruise.util;

import static com.thoughtworks.cruise.util.ExceptionUtils.bombIf;
import static java.util.Arrays.asList;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Iterator;
import java.util.List;

public final class ListUtil {
    private ListUtil() { }

    public static String join(Collection c) {
        return join(c, ", ");
    }

    public static String join(Collection c, String join) {
        StringBuffer sb = new StringBuffer();
        for (Iterator<Object> iter = c.iterator(); iter.hasNext();) {
            sb.append(iter.next());
            if (iter.hasNext()) {
                sb.append(join);
            }
        }
        return sb.toString();
    }

    public static <T> boolean addAllTo(List<T> list, T... args) {
        return list.addAll(asList(args));
    }

    public static List<List<String>> split(List<String> list, String splitOn) {
        ArrayList<List<String>> splittedStrings = new ArrayList<List<String>>();
        if (list.isEmpty()) { return splittedStrings; }
        splittedStrings.add(new ArrayList<String>());
        for (String line : list) {
            if (line.equals(splitOn)) {
                splittedStrings.add(new ArrayList<String>());
            } else {
                last(splittedStrings).add(line);
            }
        }
        return splittedStrings;

    }

    public static <T> T last(List<T> list) {
        bombIf(list.isEmpty(), "Unable to get last of empty list");
        return list.get(list.size() - 1);
    }

    public static <T> T removeLast(List<T> list) {
        bombIf(list.isEmpty(), "Unable to remove last of empty list");
        return list.remove(list.size() - 1);
    }

    public static <T, S extends Collection<T>> S filterInto(S results, Collection<T> source, Filter<T> filter) {
        for (T model : source) {
            if (filter.matches(model)) {
                results.add(model);
            }
        }
        return results;
    }

}
