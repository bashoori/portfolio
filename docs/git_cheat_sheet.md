# 📚 Git Cheat Sheet (Day-to-Day Developer Use)

Essential Git commands for professional developer daily workflows.

---

## 🔹 Initialize & Setup

| Action | Command |
|:------|:--------|
| Initialize a new Git repository | `git init` |
| Set your name for commits | `git config --global user.name "Your Name"` |
| Set your email for commits | `git config --global user.email "your-email@example.com"` |
| Check Git configuration | `git config --list` |

---

## 🔹 Working with Files

| Action | Command |
|:------|:--------|
| Check status of working directory | `git status` |
| Stage all changes | `git add .` |
| Stage a specific file | `git add filename.ext` |
| Unstage a file | `git reset HEAD filename.ext` |
| Commit changes with a message | `git commit -m "your commit message"` |
| See commit history | `git log` |

---

## 🔹 Working with Remote Repositories

| Action | Command |
|:------|:--------|
| Add a remote repository | `git remote add origin https://github.com/username/repository.git` |
| View current remotes | `git remote -v` |
| Remove a wrong remote | `git remote remove origin` |
| Push changes to remote repository | `git push -u origin main` |
| Pull latest changes from remote | `git pull origin main` |
| Force merging different histories | `git pull origin main --allow-unrelated-histories` |

---

## 🔹 Merge Conflicts

| Action | Command |
|:------|:--------|
| Open conflicted files (GUI editor or terminal) |
| Fix conflict manually: choose parts you want to keep |
| After fixing, mark file as resolved | `git add conflicted_file.ext` |
| Commit the resolution | `git commit -m "Resolve merge conflict"` |

---

## 🔹 Other Useful Commands

| Action | Command |
|:------|:--------|
| Clone a repository | `git clone https://github.com/username/repository.git` |
| Rename local branch | `git branch -M main` |
| View local branches | `git branch` |
| Delete a local branch | `git branch -d branch_name` |

---

# 🛠 Pro Best Practices

- Always run `git status` before committing.
- Write clear, meaningful commit messages.
- Pull the latest changes from remote before pushing new work.
- Resolve merge conflicts carefully, and test code after merging.
- Commit early and often to create clean history.

---

# 🚀 Common Daily Flow Example

```bash
git pull origin main
git add .
git commit -m "Short and meaningful commit message"
git push -u origin main




📢 Important Reminders

✅ Unrelated Histories Error?
Use the allow-unrelated-histories flag to pull:
git pull origin main --allow-unrelated-histories

✅ Git Lock Errors?
Clean lock files if Git refuses commands:
rm -f .git/index.lock
rm -f .git/config.lock

✅ Merge Conflicts?
Steps to resolve:
  1.	Open conflicted files
  2.	Keep or combine content you want
  3.	Remove conflict markers (<<<<<<<, =======, >>>>>>>)
  4.	Save and run:
   git add conflicted_file.ext
   git commit -m "Resolve conflict"
  

✅ Good Habit:
•	Always git pull first before starting new work.
•	Always git status before adding files.

---

# ✅ How to use:

1. **Create a file** named `GIT_CHEAT_SHEET.md` in your project.
2. **Copy-paste** the above content into it.
3. **Push** it to GitHub:

```bash
git add GIT_CHEAT_SHEET.md
git commit -m "Add professional Git Cheat Sheet for developers"
git push