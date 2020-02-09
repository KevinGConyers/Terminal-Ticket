
# from .classmodule import MyClass
# from .funcmodule import my_function


#!/bin/python

import argparse
import sys
import os
import os.path
import ticket_service.webservices as tc
import ticket_service.ticketinterface as ti
import json
from collections import Counter
from jira import JIRA


def handleArgs():
    parser = argparse.ArgumentParser(description='Command line Jira frontend')
    #parser.add_argument('-f', '--filename',  dest='filename', action='store', default='default.shock', help='provide a filename, if not provided, a default is used, located in ~/.ShockStohr/default.shock')
    parser.add_argument('mode', nargs=1, action='store', help='Supply an action mode')
    parser.add_argument('search_string', nargs='*', action='store')
    parser.add_argument('-m', '--message', nargs="*", action='store')
    args = parser.parse_args(sys.argv[1:])
    return args
def loadConfiguration():
    configuration_dict_list = []
    home = os.path.expanduser("~")
    config_path = "{}/.ttktconfig.json".format(home)
    if os.path.isfile(config_path):
        config_file = open(config_path)
        configuration_dict_list = json.load(config_file)
    else:
        print("User configuration file not set, contact sysadmin")
        exit()
    return configuration_dict_list



def main():
    args = handleArgs()
    configuration = loadConfiguration()
    project_name =configuration["project-key"]
    user_name = ''
    if configuration["auth-type"] == "http":
        user_name = configuration["http-user"]["name"]
        jira = JIRA(configuration["options"], auth=(configuration["http-user"]["name"], configuration["http-user"]["password"]))  # a username/password tuple
    else :
        print("Authentication appears to be configured incorrectly")
        exit()
    project = jira.project(project_name)
    if len(args.mode) < 1:
        print("Please supply a mode!")
        exit()
    if args.mode[0] == 'list':
        tc.listIssues(jira, project_name)
    if args.mode[0] == 'create':
        issue = ti.createIssue(user_name)
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


    args = sys.argv[1:]

if __name__ == '__main__':
    main()

