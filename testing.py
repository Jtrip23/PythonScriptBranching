from github import Github
import pandas as pd


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

# Create branches from data in an Excel file
def create_branches_from_excel(username, token, excel_file):
    try:
        # Read the Excel file
        df = pd.read_excel(excel_file, engine='openpyxl')
        
        # Iterate over rows in the DataFrame
        for index, row in df.iterrows():
            repo_name = row['name']
            base_branch = row['base_branch']
            new_branch_name = row['new_branch']
            create_branch(username, token, repo_name, base_branch, new_branch_name)
    
    except Exception as e:
        print(f"Error reading Excel file or creating branches: {e}")

# Example usage
if __name__ == "__main__":
    excel_file = 'repositories.xlsx'  # Path to your Excel file
    create_branches_from_excel(USERNAME, TOKEN, excel_file)
