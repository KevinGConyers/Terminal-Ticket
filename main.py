#!/bin/python

import argparse
import sys
import os
import ticket_service.webservices as tc
#import ticket_service.tickerinterface as ti
from collections import Counter
from jira import JIRA


def handleArgs():
    parser = argparse.ArgumentParser(description='Command line Jira frontend')
    #parser.add_argument('-f', '--filename',  dest='filename', action='store', default='default.shock', help='provide a filename, if not provided, a default is used, located in ~/.ShockStohr/default.shock')
    parser.add_argument('mode', nargs=1, action='store', help='list all issues in project')
    parser.add_argument('search_string', nargs='*', action='store')
    args = parser.parse_args(sys.argv[1:])
    return args

def main():
    args = handleArgs()
    options = {"server": "http://45.32.220.47:8080"}
    jira = JIRA(options, auth=("kevin", "v3ryC0mpl3x!"))  # a username/password tuple
    print("Mode: {}".format(args.mode))
    if args.mode[0] == 'list-issues':
        tc.listIssues(jira)
    if args.mode[0] == 'create-issue':
        print(args.search_string)
        issue = tc.openIssue(jira, args.search_string[0])
        ti.editTicket(issue)
        print("{}".format(issue.fields.summary))


main()
