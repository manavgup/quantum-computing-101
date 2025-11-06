# How to Upload Files to Your GitHub Repository

## Method 1: Using GitHub Web Interface (Easiest)

### For Individual Files

1. **Go to your repository**: https://github.com/manavgup/quantum-computing-101

2. **Navigate to the location** where you want to add a file
   - Click on folders to navigate into them
   - Or stay in the root for top-level files

3. **Click "Add file" → "Create new file"** or **"Upload files"**

4. **For Create new file:**
   - Type the filename (including path like `01-foundations/README.md`)
   - Paste the content
   - Scroll down, add commit message
   - Click "Commit new file"

5. **For Upload files:**
   - Drag and drop files
   - Or click "choose your files"
   - Add commit message
   - Click "Commit changes"

### Creating Directory Structure

To create folders on GitHub web:
1. Click "Add file" → "Create new file"
2. Type: `folder-name/filename.md`
3. GitHub will automatically create the folder!

Example: Type `01-foundations/README.md` and it creates the folder `01-foundations` with `README.md` inside.

---

## Method 2: Using Git Command Line (Recommended for Multiple Files)

### Initial Setup

```bash
# 1. Clone your repository
git clone https://github.com/manavgup/quantum-computing-101.git
cd quantum-computing-101

# 2. Verify you're in the right place
pwd  # Should show .../quantum-computing-101
ls   # Should show LICENSE and README.md
```

### Copy Files from Our Created Structure

```bash
# Option A: Copy everything at once
cp -r /tmp/quantum-repo/* .

# Option B: Copy selectively
cp /tmp/quantum-repo/README.md .
cp /tmp/quantum-repo/CONTRIBUTING.md .
cp /tmp/quantum-repo/CODE_OF_CONDUCT.md .
cp /tmp/quantum-repo/LEARNING_PATHS.md .
cp /tmp/quantum-repo/PROJECT_STATUS.md .
cp /tmp/quantum-repo/requirements.txt .
cp /tmp/quantum-repo/.gitignore .

# Copy directories
cp -r /tmp/quantum-repo/01-foundations .
cp -r /tmp/quantum-repo/06-hands-on .
cp -r /tmp/quantum-repo/07-resources .
```

### Create Remaining Directory Structure

```bash
# Create all needed directories
mkdir -p 01-foundations/{illustrations,exercises}
mkdir -p 02-gates-and-circuits/{illustrations,notebooks}
mkdir -p 03-quantum-stack/{illustrations,code-examples}
mkdir -p 04-algorithms/{illustrations,implementations/{grovers,vqe,qaoa}}
mkdir -p 05-use-cases/illustrations
mkdir -p 06-hands-on/{notebooks,exercises/{beginner,intermediate,advanced},solutions}
mkdir -p 07-resources
mkdir -p assets/{css,js,images/logos}
mkdir -p .github/{ISSUE_TEMPLATE,workflows}
mkdir -p scripts
```

### Commit and Push

```bash
# 1. Check what's changed
git status

# 2. Add all files
git add .

# 3. Commit with a message
git commit -m "feat: Add initial quantum computing content structure

- Added comprehensive README and documentation
- Created Part 1: Foundations with 'Why Quantum' content
- Added setup guide, glossary, and learning paths
- Established complete directory structure"

# 4. Push to GitHub
git push origin main
```

If you get an error about `main` vs `master`:
```bash
git push origin master
```

---

## Method 3: Using GitHub Desktop (Visual Interface)

### Setup

1. **Download GitHub Desktop**: https://desktop.github.com/
2. **Install and sign in** with your GitHub account
3. **Clone your repository**:
   - File → Clone Repository
   - Select `manavgup/quantum-computing-101`
   - Choose local path
   - Click "Clone"

### Add Files

1. **Copy files** to the cloned folder using your file explorer
2. **GitHub Desktop** will automatically detect changes
3. **Review changes** in the left panel
4. **Write commit message** in bottom left
5. **Click "Commit to main"**
6. **Click "Push origin"** to upload to GitHub

---

## Quick Start Commands

### If You Just Want to Get Everything Up Quickly

```bash
# Navigate to a working directory
cd ~

# Clone the repo
git clone https://github.com/manavgup/quantum-computing-101.git
cd quantum-computing-101

# Copy all our created files
cp -r /tmp/quantum-repo/* .

# Add everything
git add .

# Commit
git commit -m "feat: Initial content and structure"

# Push
git push origin main
```

Done! 🎉

---

## Verification

After pushing, verify everything worked:

1. Go to https://github.com/manavgup/quantum-computing-101
2. Refresh the page
3. You should see:
   - Updated README.md with the full content
   - All new files and folders
   - Green "committed" timestamp

---

## Troubleshooting

### "Permission denied"
```bash
# Make sure you're authenticated
gh auth login
# Or use SSH keys
```

### "Your branch is behind"
```bash
# Pull first, then push
git pull origin main
git push origin main
```

### "Merge conflict"
```bash
# If you have conflicts
git status  # See conflicted files
# Edit files to resolve conflicts
git add .
git commit -m "Resolved conflicts"
git push origin main
```

### "Failed to push"
```bash
# Force push (⚠️ use carefully!)
git push -f origin main
```

---

## Need Help?

- **Git basics**: https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control
- **GitHub Desktop**: https://docs.github.com/en/desktop
- **GitHub CLI**: https://cli.github.com/manual/

---

## What to Upload First

### Priority 1 (Do Now):
- [x] README.md
- [x] CONTRIBUTING.md
- [x] CODE_OF_CONDUCT.md
- [x] LEARNING_PATHS.md
- [x] requirements.txt
- [x] .gitignore
- [x] 01-foundations/README.md
- [x] 01-foundations/01-why-quantum.md
- [x] 06-hands-on/setup-guide.md
- [x] 07-resources/glossary.md
- [x] PROJECT_STATUS.md

### Priority 2 (Next Session):
- [ ] Complete remaining Part 1 content
- [ ] Create first illustrations
- [ ] Add README files for other sections

---

**Choose the method that works best for you and let's get your content online!** 🚀
