#!/usr/bin/env python
from diff_lib import *

args = parseArguments()

if args.verbose:
    print "Workspace {0}".format(args.workspace)

print "Values of {0} ".format(args.key)

show_diff(args, ["dev","qa","staging", "prod"])
