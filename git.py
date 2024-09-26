import os
import random
import datetime

# Number of commits to create
num_commits = 200

for i in range(num_commits):
    # Calculate a random date in the past
    days_ago = i  # or use: random.randint(1, 365)
    commit_date = (datetime.datetime.now() - datetime.timedelta(days=days_ago)).strftime('%Y-%m-%d %H:%M:%S')

    # Create or append to the file
    with open('test.txt', 'a') as file:
        file.write(f'Commit made {days_ago} days ago\n')

    # Stage and commit with the specified date
    os.system('git add test.txt')
    os.system(f'git commit --date="{commit_date}" -m "Automated commit {i+1}"')

# Push all the commits to the main branch
os.system('git push -u origin main')
