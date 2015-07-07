package com.thoughtworks.cruise;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

import org.dom4j.Document;
import org.dom4j.Element;

import com.thoughtworks.cruise.util.XmlUtil;
import com.thoughtworks.twist.core.reporting.HttpCommunication;

public class FailedTestSparkline {
    private static Map<String, List<Integer>> nameToCounters = new HashMap<String, List<Integer>>();

    private static List<Document> downloadOneArtifact(String artifactUrl) {
        List<Document> elements = new ArrayList<Document>();
        ZipInputStream stream = null;
        HttpCommunication httpCommunication = new HttpCommunication("10.4.8.253", 8153, "both", "badger");
        try {
            stream = new ZipInputStream(httpCommunication.getMethodBodyAsStream(artifactUrl));
            ZipEntry entry = null;
            while ((entry = stream.getNextEntry()) != null) {
                if (entry.getName().endsWith(".xml")) {
                    String xmlContent = readZipEntry(stream);
                    Document document = XmlUtil.parse(xmlContent);
                    elements.add(document);
                }
            }
        } catch (Exception e) {
//            System.out.println("Caught an exception: " + e.getMessage());
        } finally {
            try {
                if (stream != null) {
                    stream.close();
                }
            } catch (IOException e) {
            }
        }
        return elements;
    }

    private static String readZipEntry(ZipInputStream stream) throws IOException {
        StringBuilder builder = new StringBuilder();
        BufferedReader reader = new BufferedReader(new InputStreamReader(stream));
        String line = null;
        while ((line = reader.readLine()) != null) {
            builder.append(line);
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        int latest = 1540;
        int count = 300;
        for (int i = 0; i < count; i++) {
            int counter = latest - i;
            List<Document> docs = downloadOneArtifact("/go/files/acceptance-flaky/" + counter + "/twist/1/firefox/xml.zip");
            for (Document doc : docs) {
                Element node = (Element) doc.selectSingleNode("//testsuite");
                String name = node.attributeValue("name");
                List<Integer> counts = nameToCounters.get(name);
                if (counts == null) {
                    counts = new ArrayList<Integer>();
                    nameToCounters.put(name, counts);
                }
                if (!(node.attributeValue("errors").equals("0") && node.attributeValue("failures").equals("0"))) {
                    counts.add(counter);
                }
            }
        }
        for (Entry<String, List<Integer>> entry : nameToCounters.entrySet()) {
            System.out.println(entry.getKey() + ": " + entry.getValue());
        }
    }
}
