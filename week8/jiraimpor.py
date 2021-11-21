from jira import JIRA
from jira import JIRA
import re

# By default, the client will connect to a JIRA instance started from the Atlassian Plugin SDK
# (see https://developer.atlassian.com/display/DOCS/Installing+the+Atlassian+Plugin+SDK for details).
# Override this with the options parameter.
from jira import JIRA
jira = JIRA('https://jira.atlassian.com')
block_size = 1000
block_num = 0
allissues = []
while True:
 start_idx = block_num*block_size
 
 issue = jira.issue('JRASERVER-66576')

 worklogs = issue.fields.worklog.worklogs
 print(worklogs)
 print(issue.fields.worklog.worklogs[1].timeSpent)
 print(issue.fields.worklog.worklogs[0].author,issue.fields.worklog.worklogs[0].updated,issue.fields.timetracking.timeSpent)

 issues = jira.search_issues('created>=2022-01-01', start_idx, block_size)
 if len(issues) == 0:
 # Retrieve issues until there are no more to come
  break
 block_num += 1
 for issue in issues:
      allissues.append(issue)
 print(len(allissues))


 #log.info('%s: %s' % (issue.
"""options = {"server": "https://jira.atlassian.com"}
jira = JIRA(options)

# Get all projects viewable by anonymous users.
projects = jira.projects()

# Sort available project keys, then return the second, third, and fourth keys.
keys = sorted([project.key for project in projects])[2:5]

# Get an issue.
issue = jira.issue("JRASERVER-70503")
print(issue)

# Find all comments made by Atlassians on this issue.
atl_comments = [
    comment
    for comment in issue.fields.comment.comments
]
print(atl_comments)"""