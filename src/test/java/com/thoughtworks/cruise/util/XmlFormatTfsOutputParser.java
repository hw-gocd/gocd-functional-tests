package com.thoughtworks.cruise.util;

import com.thoughtworks.cruise.tfs.Workspaces;
import com.thoughtworks.cruise.util.command.ConsoleResult;
import com.thoughtworks.xstream.XStream;

/**
 * @understands: how to parse xml output from tfs command
 */
public class XmlFormatTfsOutputParser {

    public Workspaces parseWorkspaces(ConsoleResult consoleResult) {
        return (Workspaces) deserialize(consoleResult);
    }


    private Object deserialize(ConsoleResult consoleResult) {
        XStream xStream = xstream();
        return xStream.fromXML(unwindowfy(consoleResult.outputAsString()));
    }

    private String unwindowfy(String windowfiedXml) {
        int startOfXml = windowfiedXml.indexOf("<?xml");
        return windowfiedXml.substring(startOfXml);
    }   

    private static XStream xstream() {
        XStream xStream = new XStream();
        xStream.alias("workspaces", Workspaces.class);
        xStream.autodetectAnnotations(true);
        return xStream;
    }

}
