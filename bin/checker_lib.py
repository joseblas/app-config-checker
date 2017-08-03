import argparse
import collections
import yaml

def flatten(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


def parseArguments():
    parser = argparse.ArgumentParser(description='Library release tagger - tag non-snapshot libraries')
    parser.add_argument('-v', '--verbose', action='store_true', help='Print debug output')
    parser.add_argument('workspace', type=str, help='Where all the app-configs are')
    parser.add_argument('projectName', type=str, help='The jenkins build of the repo we want to tag')
    parser.add_argument('envA', type=str, help='The jenkins build of the repo we want to tag')
    parser.add_argument('envB', type=str, help='The jenkins build of the repo we want to tag')
    # parser.add_argument('version', nargs='?', type=str, help='The jenkins build of the repo we want to tag')
    # parser.add_argument('env', nargs='?', type=str, help='Environment to deploy')
    args = parser.parse_args()
    return args

def get_keys_from_enviroment(args, env):
    file = "{0}/app-config-{1}/{2}.yaml".format(args.workspace, env, args.projectName)
    print "File name : " + file
    with open(file, 'r') as stream:
        try:
            conf = yaml.safe_load(stream)
            new_dict = flatten(conf["0.0.0"])
            # print "Key {0}".format(new_dict.keys())
            return new_dict
        except yaml.YAMLError as exc:
            print(exc)

def diff(args,a,b):
    print(" {0} vs {1}".format(a,b))
    keys_a = get_keys_from_enviroment(args, a)
    keys_b = get_keys_from_enviroment(args, b)


    diff_a = list(set(keys_a.keys()) - set(keys_b.keys()))
    diff_b = list(set(keys_b.keys()) - set(keys_a.keys()))
    # diff_qa  = list(set(qa.keys()) - set(dev.keys())).sort()
    diff_a.sort()
    diff_b.sort()

    #print "{0} -> {1}".format(a,b)
    for key in diff_a:
        print "- " + key

    # print "{1} -> {0}".format(a,b)
    for key in diff_b:
        print "+ " + key