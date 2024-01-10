users = {'Hans': 'active', 'Éléonore': 'inactive', 'deem': 'active'}
"""for status in users:
    if status == 'inactive':
        del users[status]
"""
for user, status in users.copy().items():
        if status == 'inactive':
                    del users[user]
        print(users)


active_users = {}
for user, status in users.items():
        if status == 'active':
                    active_users[user] = status
