# Git Commands: Beginner Reference (built from my own project)

_Added 2026-10-23. Companion to `terminal-and-console-commands.md` (R and package commands) and `class4_notes.md` (branching walkthrough). This file is git only._

**The one rule:** Terminal prompt ends in `$` or `%` and takes git and shell commands. R Console prompt is `>` and takes R code. Git never goes in the Console.

**The one habit:** Run `git branch` and `git status` before anything that changes something.

**The one sentence:** branch, status, add, commit, push.

---

## 1. Look before you act (safe, run constantly)

| Command | What it does | Use case |
|-|-|-|
| `git status` | Shows branch, staged, unstaged and untracked files | Before every commit, merge and push |
| `git branch` | Lists branches, `*` marks where I am | Before every merge. Prevents "Already up to date" |
| `git log --oneline -5` | Last 5 commits, one line each | Confirm `124f05e` is on top of `a3` |
| `git diff` | Shows unstaged line changes | The `readme.md` check that showed one line replaced |
| `git diff --staged` | Shows what is staged | Last look before committing |
| `git remote -v` | Shows where `origin` points | `https://` means GCM matters, `git@` means SSH |

**Fun fact:** Linus Torvalds wrote the first version of git in about 10 days in 2005, after the Linux kernel lost free access to its old version control tool. He named it after British slang for an unpleasant person.

---

## 2. The save loop: add, commit, push

| Command | What it does | Plain English |
|-|-|-|
| `git add <file>` | Stages a file | "Put this in the box" |
| `git add <folder>/` | Stages a folder | Stage by name, never `git add -A` |
| `git commit -m "message"` | Saves a snapshot on my computer | "Seal the box and label it" |
| `git push` | Sends commits to GitHub | "Ship the box" |
| `git push -u origin <branch>` | First push of a new branch, sets tracking | Once per branch. After that plain `git push` works |

**Fun fact:** every commit gets a 40 character ID (a SHA-1 hash) computed from its contents. `4ee02ef` is enough because the first 7 or so characters are usually unique.

---

## 3. Branches

| Command | What it does | Use case |
|-|-|-|
| `git checkout -b name` | Creates and switches | Starting new work |
| `git switch -c name` | Newer form of the same | Same |
| `git checkout main` | Switches to an existing branch | Parking work, then returning |
| `git switch main` | Newer form | Same |
| `git branch -d name` | Deletes a merged branch, refuses if unmerged | Cleanup. Safer than `-D` |
| `git branch -D name` | Force-deletes, even unmerged | Only when the work is expendable |

**Fun fact:** a branch is a tiny text file holding one commit ID. Creating one costs almost nothing, so make them freely. `a2` stayed fixed while `main` moved because a branch label only moves when I commit on it.

**Trap:** uncommitted edits follow me to the new branch. Commit first, then switch.

---

## 4. Merging

| Command | What it does | Use case |
|-|-|-|
| `git checkout main` then `git merge a3` | Brings `a3` into `main` | Always switch to the receiving branch first |
| `git merge --abort` | Cancels a merge in progress | When a conflict scares me |
| `git add <file>` then `git commit` | Finishes a conflict resolution | After deleting the `<<<<<<<` markers |

**Three outcomes:**
- **Fast-forward:** the label just moves. Silent.
- **Merge commit:** vim opens for a message. `Esc`, then `:wq`.
- **Conflict:** markers appear in the file. Edit, delete the markers, add, commit.

---

## 5. Syncing with GitHub

| Command | What it does | Use case |
|-|-|-|
| `git clone <url>` | Downloads a repo | Once per repo |
| `git clone -b a1 <url> <folder>` | Clones one branch | Fresh-clone install test |
| `git fetch origin` | Downloads GitHub's state, changes no files | Safe peek before merging |
| `git pull` | Fetch plus merge | When GitHub is ahead |
| `git pull origin main --allow-unrelated-histories` | Merges repos with separate origins | 
| `git remote set-url origin <url>` | Changes where `origin` points |
| `git remote add origin <url>` | Adds a remote, errors if `origin` exists | First-time setup only |

**Fun fact:** `origin` is not special. It is the default nickname for the remote I cloned from. I could call it `banana`.

**Memory trick:** push rejected with "fetch first" means GitHub has something I lack. Fetch or pull, then push.

---

## 6. Undo and rescue

| Command | What it does | Danger |
|-|-|-|
| `git restore <file>` | Discards unstaged edits to a file | **Permanent.** Cannot be recovered |
| `git restore --staged <file>` | Unstages, keeps my edits | Safe |
| `git reset` | Unstages everything, files untouched | Safe. Fixed the RStudio Git pane mess |
| `git checkout -f <branch>` | Switches and discards local changes | **Destructive.** Back up first |
| `git stash` | Shelves uncommitted edits | Safe. "Put it in my pocket" |
| `git stash pop` | Takes them back out | Safe |
| `git reflog` | History of everywhere HEAD has been | Safe. The rescue tool |
| `git rm <file>` | Deletes a file and stages the deletion | How I removed `test_function` |

**Fun fact:** `git reflog` keeps recent moves for about 90 days by default, so a "lost" commit is usually recoverable. Committed work is very hard to destroy. Uncommitted work is not.

---

## 7. Setup and config (mostly one-time)

| Command | What it does |
|-|-|
| `git config --global --get-all credential.helper` | Shows active credential helpers. Want only the GCM path |
| `git credential-manager configure` | Registers Git Credential Manager |
| `git config --global credential.useHttpPath true` | Keeps credentials separate per repo |
| `git config --global core.editor nano` | Replaces vim for commit messages |

---

## 8. Vim escape (the git screen I hit most)

| Goal | Keys |
|-|-|
| Save and finish | `Esc`, then `:wq`, Return |
| Quit without saving | `Esc`, then `:q!`, Return |

**Fun fact:** "how do I exit vim" is one of the most viewed questions on Stack Overflow, with millions of views.

---

## 9. Error decoder (from my own logs)

| What I saw | Meaning | Fix |
|-|-|-|
| `Nothing specified, nothing added` | `git add` with no file name | Name the file |
| `rejected ... (fetch first)` | GitHub has commits I lack | `git pull`, then `git push` |
| `rejected ... (non-fast-forward)` | My branch is behind or diverged | `git pull --no-rebase origin main`, then push |
| `remote origin already exists` | Used `add` on an existing remote | Use `set-url` |
| `Already up to date` on a merge | Merged a branch into itself | `git checkout main` first |
| `unexpected symbol` or stuck `>` | Git typed in the R Console | Use the Terminal tab |
| `function>` prompt in Terminal | R code typed in the Terminal | Ctrl+C or Cmd+C|
| HTTP 404 on `install_github()` | Private repo, no token | `gitcreds::gitcreds_set()` in the Console |

---

## Standard workflow

1. `git branch` and `git status`: where am I, is it clean?
2. Make edits.
3. `git diff`: what did I change?
4. `git add <file>`, then `git status`: only the right files staged?
5. `git commit -m "..."`
6. `git push`

## Questions to answer without notes

1. What is the difference between `add`, `commit` and `push`?
2. Why does an uncommitted edit follow me to another branch?
3. Why must I switch to `main` before `git merge a3`?
4. What does "fetch first" mean, and what fixes it?
5. Which undo commands are permanent?
