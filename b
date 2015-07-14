#!/bin/sh

unset GEM_HOME
unset GEM_PATH

$(dirname $0)/tools/bin/go.jruby -J-Xmx2048m -S buildr $*
