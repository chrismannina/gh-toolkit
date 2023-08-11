import json
import os
import requests
from dotenv import load_dotenv
import sys


def create_github_issue(token, repo_owner, repo_name, title, body="", labels=[]):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"title": title, "body": body, "labels": labels}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Issue '{title}' created successfully!")
    else:
        print(
            f"Failed to create issue '{title}'. Status code: {response.status_code}. Response: {response.content.decode('utf-8')}"
        )


def create_github_label(token, repo_owner, repo_name, name, color):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/labels"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {"name": name, "color": color}

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f"Label '{name}' created successfully!")
    else:
        print(
            f"Failed to create label '{name}'. Status code: {response.status_code}. Response: {response.content.decode('utf-8')}"
        )


def ensure_labels_exist(token, repo_owner, repo_name, labels):
    for label in labels:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/labels/{label['name']}"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
        }
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            # Label does not exist, create it
            create_github_label(token, repo_owner, repo_name, label['name'], label['color'])


def load_labels_from_files(filepaths):
    """Load labels from multiple JSON files."""
    labels = []
    for filepath in filepaths:
        with open(filepath, "r") as file:
            labels.extend(json.load(file))
    return labels

def load_configuration(filename="data.json"):
    """Load configuration from a JSON file and environment variables."""
    with open(filename, "r") as file:
        data = json.load(file)

    # Extract configurations
    token = data["config"].get("token", os.getenv("GITHUB_PAT"))
    repo_owner = data["config"]["repo_owner"]
    repo_name = data["config"]["repo_name"]
    issues_to_upload = data["issues"]

    return token, repo_owner, repo_name, issues_to_upload

def main():
    load_dotenv()
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "data.json"  
    TOKEN, REPO_OWNER, REPO_NAME, issues_to_upload = load_configuration(filename)
    labels_to_add = load_labels_from_files([r"C:\Users\machris\projects\chris_dev\github_tools\labels\category.json", r"C:\Users\machris\projects\chris_dev\github_tools\labels\priority.json"])
    ensure_labels_exist(TOKEN, REPO_OWNER, REPO_NAME, labels_to_add)

    
    
    for issue in issues_to_upload:
        create_github_issue(
            TOKEN, REPO_OWNER, REPO_NAME, issue["title"], issue.get("body", ""), issue.get("labels", [])
        )


if __name__ == "__main__":
    main()