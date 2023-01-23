from github import Github
import random
import datetime
import os
from dotenv import load_dotenv
from datetime import datetime, timezone ,timedelta
 
 # Load the .env file
load_dotenv()


# Replace the placeholders with your own values
owner = os.environ.get("OWNER")
repo_name = os.environ.get("REPO")
access_token = os.environ.get("ACCESS_TOKEN")

# Create a Github instance using your access token
g = Github(access_token)

# Get the repository object
repo = g.get_user(owner).get_repo(repo_name)

# Get the main branch of the repository
main_branch = repo.get_branch('main')

# Set the commit date to a specific date and time
commit_date = datetime(2022, 3, 19, 23, 59, 59)

# Set the timezone to UTC
tz = timezone(timedelta(0))

# Add the timezone information to the commit date
commit_date = commit_date.replace(tzinfo=tz)

# Create a commit object with the specified date
commit = repo.get_git_ref(f"heads/{main_branch.name}").create_git_commit(
    message='Commit message',
    author={
        'name': 'Your Name',
        'email': 'your-email@example.com',
        'date': commit_date
    },
    committer={
        'name': 'Your Name',
        'email': 'your-email@example.com',
        'date': commit_date
    },
    tree=main_branch.commit.commit.tree
)

# Update the main branch reference to point to the new commit
main_branch.edit(commit.sha)

print('Commit created with date:', commit_date)