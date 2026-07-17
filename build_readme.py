import os
import json
from pathlib import Path

def build_readme():
    """Generate README dashboard from LeetCode submissions."""
    
    # Find all submission files
    submissions = []
    submissions_dir = Path("submissions")
    
    if submissions_dir.exists():
        for file in submissions_dir.glob("**/*.py"):
            submissions.append(file)
    
    # Generate README content
    readme_content = f"""# LeetCode Solutions Dashboard

## Statistics
- **Total Submissions:** {len(submissions)}

## Solutions

"""
    
    # Add your custom logic here to format submissions
    for submission in sorted(submissions):
        readme_content += f"- {submission.name}\n"
    
    # Write README
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print(f"README updated with {len(submissions)} submissions")

if __name__ == "__main__":
    build_readme()
