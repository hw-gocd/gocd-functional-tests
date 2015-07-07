package com.thoughtworks.cruise.util;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import org.apache.commons.lang.ArrayUtils;

public class ArrayUtil {
    private ArrayUtil() {
    }

    @SuppressWarnings("unchecked")
    public static <T> T[] addToArray(T[] array, T nextOne) {
        return (T[]) ArrayUtils.add(array, nextOne);
    }

    @SuppressWarnings("unchecked")
    public static <T> T[] pushToArray(T firstOne, T[] array) {
        return (T[]) ArrayUtils.add(array, 0, firstOne);
    }

    public static <T> String join(T[] array) {
        return join(array, ",");
    }

    public static <T> String join(T[] array, String separator) {
        StringBuffer buffer = new StringBuffer();
        for (int i = 0; i < array.length; i++) {
            T t = array[i];
            buffer.append(t.toString());
            if (i < array.length - 1) {
                buffer.append(separator);
            }
        }
        return buffer.toString();
    }

    public static <T> String joinWithQuotes(T[] array) {
        StringBuffer buffer = new StringBuffer();
        for (int i = 0; i < array.length; i++) {
            T t = array[i];
            buffer.append('\'').append(t.toString()).append('\'');
            if (i < array.length - 1) {
                buffer.append(',');
            }
        }
        return buffer.toString();
    }

    /*
     * Much like Arrays.asList, except the list is not fixed size.
     */
    public static <T> List<T> asList(T... a) {
        if (a == null) { return new ArrayList<T>(); }
        
        ArrayList<T> list = new ArrayList<T>(a.length);
        list.addAll(Arrays.asList(a));
        return list;
    }
}
