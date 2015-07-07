package com.thoughtworks.cruise.config;

import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public interface ModifyCommand {

    void modify(CruiseConfigDom dom);
}
