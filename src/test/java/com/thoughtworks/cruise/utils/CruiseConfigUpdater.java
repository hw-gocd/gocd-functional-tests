package com.thoughtworks.cruise.utils;

import com.thoughtworks.cruise.utils.configfile.CruiseConfigDom;

public interface CruiseConfigUpdater {
    void update(CruiseConfigDom dom);
}
