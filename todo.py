import todoist
api = todoist.TodoistAPI('0123456789abcdef0123456789abcdef01234567')
api.sync()
full_name = api.state['user']['full_name']
print(full_name)
# John Doe
# for project in api.state['projects']:
# ...     print(project['hello'])
...
# Personal
# Shopping
# Work
# Errands
# Movies to watch