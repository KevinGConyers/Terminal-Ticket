#!/bin/python

import argparse
import sys
import os
import ticket_service.webservices as tc
import ticket_service.ticketinterface as ti
from collections import Counter
from jira import JIRA


def handleArgs():
    parser = argparse.ArgumentParser(description='Command line Jira frontend')
    #parser.add_argument('-f', '--filename',  dest='filename', action='store', default='default.shock', help='provide a filename, if not provided, a default is used, located in ~/.ShockStohr/default.shock')
    parser.add_argument('mode', nargs=1, action='store', help='list all issues in project')
    parser.add_argument('search_string', nargs='*', action='store')
    parser.add_argument('-m', '--message', nargs="*", action='store')
    args = parser.parse_args(sys.argv[1:])
    return args

def main():
    args = handleArgs()
    options = {"server": "http://45.32.220.47:8080"}
    project_name = "TT"
    jira = JIRA(options, auth=("kevin", "v3ryC0mpl3x!"))  # a username/password tuple
    project = jira.project(project_name)
    print("Mode: {}".format(args.mode))
    if args.mode[0] == 'list':
        tc.listIssues(jira)
    if args.mode[0] == 'create':
        issue = ti.createIssue('kevin')
        issue['project']['id'] = project.id
        tc.createIssue(jira, issue)
    if args.mode[0] == 'edit':
        if len(args.search_string) < 1:
            print("Please provide an issue key")
            exit()
        issue = tc.openIssue(jira, args.search_string[0])
        ti.editIssue(issue)
    if args.mode[0] == 'resolve':
        if len(args.search_string) < 1:
            print("Please provide an issue key")
            exit()
        issue = tc.openIssue(jira, args.search_string[0])
        issue_transition_fields = ti.resolveIssue()
        issue_transition_fields['assignee']['name'] = 'kevin'
        tc.tranisitionIssue(jira, issue, issue_transition_fields, 'Resolve Issue')
    if args.mode[0] == "qresolve":
        if len(args.search_string) < 1:
            print("Please provide an issue key")
            exit()
        if len(args.message) < 1:
            print('Please provide a resolution message')
            exit()
        issue = tc.openIssue(jira, args.search_string[0])
        issue_transition_fields = ti.resolveIssue(args.message[0])
        issue_transition_fields['assignee']['name'] = 'kevin'
        tc.tranisitionIssue(jira, issue, issue_transition_fields, 'Resolve Issue')




main()
