#!/usr/bin/env python
# Add multigroups to users in IPA
# Author IPA2 verson: 1.0 by Magines <artur.mackowiak@allegro.pl>

import os
import sys
import subprocess
import argparse
import ipa2tools


logstr = string.join(sys.argv, ' ')
ipa2tools.log2syslog(logstr, os.environ['USER'])

parser = argparse.ArgumentParser()

parser.add_argument(
    "-g",
    "--groups",
    help="gets groups names, comma separated",
    required=True
)
parser.add_argument(
    "-u",
    "--users",
    help="gets users names, comma separated",
    required=True
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    help="verbose mode",
    default=False
)

args = parser.parse_args()


def add_users_into_groups(groups, users):
    values = groups.split(',')
    for i in values:
        subprocess.Popen(
            [
                "/user/bin/ipa",
                "group-add-member",
                i,
                '--users=%s' % (users)
            ]
        )
        ipa2tools.log2syslog(logstr)
    if args.verbose:
        print ("ipa group-add-member %s --users=%s" % (i, users))

#if args.groups and args.users:
print "Adding users in to groups...."
add_users_into_groups(args.groups, args.users)
print ("\n\n ... done\n---------------------------------------------\n")
