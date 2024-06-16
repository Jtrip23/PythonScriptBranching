from github import Github

# Replace with your GitHub username and access token
USERNAME = "Jtrip23"
TOKEN = "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"

# List of repositories where branches will be created
repositories = [
    {"name": "SampleRepo1", "base_branch": "main", "new_branch": "feature-branch4"},
    {"name": "SampleRepo2", "base_branch": "main", "new_branch": "feature-branch4"},
    {"name": "HelloWorld", "base_branch": "main", "new_branch": "feature-branch4"},
    {"name": "Branching", "base_branch": "main", "new_branch": "feature-branch4"}
]

def create_branch(username, token, repo_name, base_branch, new_branch_name):
    try:
        # Authenticate using username and access token
        g = Github(username, token)
        
        # Access repository
        repo = g.get_repo(f"{username}/{repo_name}")
        
        # Get the base branch reference
        base_ref = repo.get_branch(base_branch)
        
        # Create a new reference for the new branch based on the base branch
        new_ref = repo.create_git_ref(
            ref=f"refs/heads/{new_branch_name}",
            sha=base_ref.commit.sha
        )
        
        print(f"Branch '{new_branch_name}' created successfully in '{repo_name}'.")
        
    except Exception as e:
        print(f"Error creating branch in '{repo_name}': {e}")

# Create branches in all repositories
def create_branches_in_repositories(username, token, repositories):
    for repo_info in repositories:
        repo_name = repo_info["name"]
        base_branch = repo_info["base_branch"]
        new_branch_name = repo_info["new_branch"]
        create_branch(username, token, repo_name, base_branch, new_branch_name)

# Example usage
if __name__ == "__main__":
    create_branches_in_repositories(USERNAME, TOKEN, repositories)
