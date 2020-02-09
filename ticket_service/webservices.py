#!/home/kevin/projects/

# This script shows how to connect to a JIRA instance with a
# username and password over HTTP BASIC authentication.

from collections import Counter
from jira import JIRA

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK.
# See
# https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK
# for details.
options = {"server": "http://45.32.220.47:8080"}
jira = JIRA(options, auth=("kevin", "v3ryC0mpl3x!"))  # a username/password tuple

# Get the mutable application properties for this server (requires
# jira-system-administrators permission)

#props = jira.application_properties()

# Find all issues reported by the admin


# Find the top three projects containing issues reported by admin

#top_three = Counter([issue.fields.project.key for issue in issues]).most_common(3)


def listIssues(jira):
    issues = jira.search_issues('project=10000')
    for issue in issues:
        print("Issue Key: {0:<10}\n\t{1:<10}".format(issue.key, issue.fields.summary))

def openIssue(jira, issue_key):
    issue=jira.issue(issue_key)
    return issue

