package com.thoughtworks.cruise.util.command;

public interface Script {

    /**
     * exitCode is what is returned from running the script
     * @param result
     */
    public void setExitCode(int result);
    public int getExitCode();

}