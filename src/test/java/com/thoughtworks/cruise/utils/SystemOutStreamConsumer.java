package com.thoughtworks.cruise.utils;

import org.apache.log4j.Logger;

public class SystemOutStreamConsumer extends ConsoleOutputStreamConsumer {

    public SystemOutStreamConsumer(Class clazz) {
        super(new StandardOutConsumer(clazz.getName()), new StandardOutConsumer(clazz.getName()));
    }

    private static class StandardOutConsumer implements StreamConsumer{

        private Logger log;
        
        public StandardOutConsumer(String name) {
            this.log = Logger.getLogger(name);
        }

        @Override
        public void consumeLine(String line) {
            log.info(line);  
        }
    }
}
