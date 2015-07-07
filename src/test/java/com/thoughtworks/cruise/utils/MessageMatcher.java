package com.thoughtworks.cruise.utils;

import java.io.IOException;

import javax.mail.Message;
import javax.mail.MessagingException;

/**
 * Created by IntelliJ IDEA.
 * User: skizz
 * Date: Oct 6, 2009
 * Time: 2:56:58 PM
 * To change this template use File | Settings | File Templates.
 */
public interface MessageMatcher {
    boolean matches(Message message) throws IOException, MessagingException;
}
