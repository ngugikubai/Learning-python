current_users = ['william','gerald','rabin','gichane','kester','mosobo']

new_users = ['william','hawanga','isaaka','kester','muchai']

for new_user in new_users:
    if new_user in current_users:
        print(" You will need to enter a new username ")
    else:
        print(" The username is available ")