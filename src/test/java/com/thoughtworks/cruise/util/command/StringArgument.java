package com.thoughtworks.cruise.util.command;

import java.util.ArrayList;
import java.util.List;

public class StringArgument extends CommandArgument {
    private String value;

    public StringArgument(String value) {
        this.value = value;
    }

    public String forCommandline() {
        return value;
    }

    /**
     * This is final to prevent subclasses from exposing data they shouldn't in logs etc.
     */
    public String forDisplay() {
        return value;
    }

    public static CommandArgument[] toArgs(Object... inputs) {
        List<CommandArgument> args = new ArrayList<CommandArgument>();
        for (int i = 0; i < inputs.length; i++) {
            if (inputs[i] instanceof CommandArgument) {
                args.add((CommandArgument) inputs[i]);
            }
            else {
                args.add(new StringArgument(inputs[i].toString()));
            }
        }
        return args.toArray(new CommandArgument[0]);
    }
}
