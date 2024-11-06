import requests
import os
# GitHub token with access to your repo
GITHUB_TOKEN = os.getenv("access_token")
REPO_OWNER = os.getenv("REPO_OWNER")
REPO_NAME = os.getenv("REPO_NAME")
PR_NUMBER = 1  # The PR number you want to approve


# API URL for creating a review
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/pulls/{PR_NUMBER}/reviews"


# Headers for authentication and content type
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}


# Review data for approving the PR
data = {
    "event": "APPROVE",  # APPROVE to approve the PR
    "body": "PR Request Approved! Enjoy"  # Optional message
}

# Send a POST request to approve the PR
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(f"Pull request #{PR_NUMBER} approved successfully!")
else:
    print(f"Failed to approve PR: {response.status_code}")
    print(response.json())