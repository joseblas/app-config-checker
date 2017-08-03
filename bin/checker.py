#!/usr/bin/env python
from checker_lib import *

args = parseArguments()

if args.verbose:
    print "Workspace {0}".format(args.workspace)

diff(args, args.envA, args.envB)



