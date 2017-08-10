import argparse
from checker_lib import get_keys_from_enviroment


def show_diff(args, envs):
    for env in envs:
        # print "{0}  {1}:{2}".format(env, args.key, get_keys_from_enviroment(args, env) )
        print "{0}  {1}: '{2}'".format(env.ljust(10), args.key, get_keys_from_enviroment(args, env).get(args.key))

def parseArguments():
    parser = argparse.ArgumentParser(description='Library for checking config k eys')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print debug output')
    parser.add_argument('workspace', type=str, help='Where all the app-configs are')
    parser.add_argument('projectName', type=str, help='The jenkins build of the repo we want to tag')
    parser.add_argument('key', type=str, help='Key to lookup')
    # parser.add_argument('version', nargs='?', type=str, help='The jenkins build of the repo we want to tag')
    # parser.add_argument('env', nargs='?', type=str, help='Environment to deploy')
    args = parser.parse_args()
    return args

