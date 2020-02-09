#!/bin/python



def editIssue(issue):
    new_summary = input("Enter new issue summary, empty for no change: ")
    new_description = input("Enter new issue description, empty for no change: ")
    comment = input("Comment on the new change: ")
    if len(new_summary) > 0:
        issue.update(summary=new_summary)
    if len(new_description) > 0:
        issue.update(description=new_description)
    if len(comment) > 0:
        issue.update(comment= comment)
    return issue

def viewIssue(issue):
    print("Issue: {:<20}\tStatus: {}\nSummary: {:<20}\nDescrption: {:<20}".format(issue.key, issue.fields.status, issue.fields.summary, issue.fields.description))


def createIssue(current_user):
    issue_dict = {'project' : {'id': 123},
                  'assignee': {'name': ''},
                 'summary': '',
                 'description': '',
                 'issuetype': {'name': 'Bug'}}
    assigned_person = input("Assign somone to this issue (leave blank to auto-assign): ")
    if len(assigned_person) > 0:
        issue_dict['assignee']['name'] = assigned_person
    else:
       issue_dict['assignee']['name'] = current_user 
    issue_dict['summary'] = input("Enter issue summary: ")
    issue_dict['description'] = input("Enter description: ")
    return issue_dict

def resolveIssue(message=None):
    resolution_options = {'message': 'Please select a resolution type', 
                          'items': ['Fixed', 'Won\'t Fix', 'Duplicate', 
                                    'Incomplete', 'Cannot Reproduce']}
    transition_dict = {'assignee': {'name': ''}, 'resolution': {'name': '', 'comment': ''}}
    if message: #quick close condition
        transition_dict['resolution']['name'] = 'Fixed'
        transition_dict['resolution']['comment'] = message
    else:
        resolution = itemSelect(resolution_options)
        comment = input('Please describe the resolution:\n ')
        transition_dict['resolution']['name'] = resolution
        transition_dict['resolution']['comment'] = comment

    return transition_dict

def itemSelect(options_dict):
    print(options_dict['message'])
    for index, item in enumerate(options_dict['items']):
        print("{}: {:20}".format(index+1, item))
    item_selection = eval(input("Please select and option number: "))
    return options_dict['items'][item_selection-1]


