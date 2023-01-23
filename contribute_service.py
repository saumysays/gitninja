from github import Github
import random
import datetime
import os
from dotenv import load_dotenv
 
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

# Define a function to create a new commit with a random message
def create_commit():
    message = f"Commit message {random.randint(1, 100)}"
    content = f"Content {random.randint(1, 100)}"
    path = f"file-{random.randint(1, 100)}.txt"
    try:
        # Get the file object if it exists
        file = repo.get_contents(path)
        # Update the file with new content
        repo.update_file(file.path, message, content, file.sha)
    except:
        # Create a new file if it doesn't exist
        repo.create_file(path, message, content)
    print(f"Commit created: {message}")

# Call the create_commit function 10 times to create 
# 10 random commits
for i in range(5):
    create_commit()

# Print a message indicating the script has finished
print(f"Script finished running at {datetime.datetime.now()}")