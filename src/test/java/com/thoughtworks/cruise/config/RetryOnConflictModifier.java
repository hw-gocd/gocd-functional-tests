package com.thoughtworks.cruise.config;

import com.thoughtworks.cruise.context.Configuration;
import com.thoughtworks.cruise.utils.Assertions;
import com.thoughtworks.cruise.utils.Assertions.Predicate;
import com.thoughtworks.cruise.utils.Timeout;
import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public class RetryOnConflictModifier implements ConfigModifier {

    private final Configuration configuration;

    public RetryOnConflictModifier(Configuration configuration) {
        this.configuration = configuration;
    }
    
    @Override
    public void modifyConfig(final ModifyCommand command) {
        Assertions.waitUntil(Timeout.TWO_MINUTES, new Predicate() {
            
            @Override
            public boolean call() throws Exception {
                CruiseConfigDom configDom = getDom();
                command.modify(configDom);
                writeToConfigFile(configDom);
                return true;
            }
        });
    }
    
    private CruiseConfigDom getDom() {
        return configuration.provideDom();
    }       
    
    private void writeToConfigFile(CruiseConfigDom dom) {
        configuration.setDom(dom);
    }
}
