#!/usr/bin/env python
from checker_lib import *
import collections


args = parseArguments()

print "Workspace {0}".format(args.workspace)

# dev = "{0}/app-config-{1}/{2}.yaml".format( args.workspace, "dev",args.projectName)


diff(args, args.envA, args.envB)



