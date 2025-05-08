import os
import subprocess
from datetime import datetime, timedelta

# === YOUR INFO ===
REPO_NAME = "hack"  # Repository name (can be any name you like)
USERNAME = "AUTOBOT"  # Author name changed to AUTOBOT
EMAIL = "adibxr@yahoo.com"
DAYS_BACK = 90  # How many days to go back
COMMITS_PER_DAY = 3  # Number of commits per day

# === SETUP FOLDER & GIT ===
os.makedirs(REPO_NAME, exist_ok=True)
os.chdir(REPO_NAME)
subprocess.run(["git", "init"])  # Initialize the Git repository
subprocess.run(["git", "config", "user.name", USERNAME])  # Set the username
subprocess.run(["git", "config", "user.email", EMAIL])  # Set the email

# Create a file to commit
with open("activity.txt", "w") as f:
    f.write("Fake contribution history by AUTOBOT\n")

# === CREATE BACKDATED COMMITS ===
print("🔧 Creating fake commits for past", DAYS_BACK, "days...")
for day in range(DAYS_BACK):
    commit_date = datetime.now() - timedelta(days=day)
    for c in range(COMMITS_PER_DAY):
        with open("activity.txt", "a") as f:
            f.write(f"{commit_date.date()} - commit {c}\n")

        subprocess.run(["git", "add", "activity.txt"])

        # Set fake author and commit dates to current date and time
        env = os.environ.copy()
        current_time_str = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")  # Current time format
        env["GIT_AUTHOR_NAME"] = "AUTOBOT"  # Set author name to AUTOBOT
        env["GIT_AUTHOR_DATE"] = current_time_str  # Set author date
        env["GIT_COMMITTER_DATE"] = current_time_str  # Set committer date

        subprocess.run(["git", "commit", "-m", f"Commit {c} on {commit_date.date()}"], env=env)

print("\n✅ DONE: All commits created with past dates!")

# Print next steps
print("\n🔜 NEXT STEPS:")
print("1. Go to https://github.com/new and create an empty repo named: hack")
print("2. Then run these commands in terminal:")
print("   cd hack")
print("   git remote add origin https://github.com/rawenergon/hack.git")
print("   git branch -M main")
print("   git push -u origin main")
print("\n🎉 After pushing, check your green squares at: https://github.com/rawenergon")
