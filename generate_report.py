import os
from datetime import datetime

# Function to get README content
def get_readme_content(repo_dir):
    readme_path = os.path.join(repo_dir, 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r') as file:
            return file.read()
    return "README.md not found."

# Function to get commit history
def get_commit_history(repo_dir):
    os.chdir(repo_dir)
    commits = os.popen('git log --pretty=format:"%h - %an, %ar : %s"').read()
    return commits

# Function to generate report
def generate_report(repo_dir, output_file):
    readme_content = get_readme_content(repo_dir)
    commit_history = get_commit_history(repo_dir)

    with open(output_file, 'w') as report:
        report.write("# Project Report\n")
        report.write(f"Generated on: {datetime.now()}\n\n")

        report.write("## README Contents:\n")
        report.write(f"{readme_content}\n\n")

        report.write("## Commit History:\n")
        report.write(f"{commit_history}\n\n")

# Set repository directory and output file
repo_dir = os.getcwd()  # Uses the current directory where Git Bash is opened
output_file = 'report.txt'

# Generate the report
generate_report(repo_dir, output_file)
print(f"Report generated at {output_file}")
