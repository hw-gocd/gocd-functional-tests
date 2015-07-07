package com.thoughtworks.cruise.util;

public interface Filter<T> {
    boolean matches(T element);
}
