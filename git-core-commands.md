# Git Core Commands

The commands you will use every day, with plain-English explanations and earth observation examples.

**Companion files:**
- `git-setup-and-troubleshooting.md`: configuration, vim escape, error decoder
- `git-shell-basics.md`: the non-git terminal commands that travel with git
- `git-sharing-and-collaboration.md`: new repos, forks, pull requests, public repo hygiene

**The one rule:** the Terminal prompt ends in `$` or `%` and takes git and shell commands. The R Console prompt is `>` and takes R code. Git never goes in the Console.

**The one habit:** most beginner mistakes come from not checking state. Run `git branch` and `git status` before anything that changes something.

**The one sentence:** branch, status, add, commit, push.

---

## 1. Look before you act (safe, run constantly)

| Command | What it does | Example use |
|-|-|-|
| `git status` | Shows your branch, staged, unstaged and untracked files | Before every commit, merge and push |
| `git branch` | Lists branches. `*` marks where you are | Before every merge. Prevents "Already up to date" |
| `git log --oneline -5` | Last 5 commits, one line each | Check your last commit message says what you think it does |
| `git diff` | Shows unstaged line changes | See exactly which lines of `ndvi.R` you changed |
| `git diff --staged` | Shows what is staged | Last look before committing |
| `git remote -v` | Shows where `origin` points | `https://` means a credential helper matters, `git@` means SSH |

**Fun fact:** Linus Torvalds wrote the first version of git in about 10 days in 2005, after the Linux kernel lost free access to its old version control tool. He named it after British slang for an unpleasant person.

---

## 2. The save loop: add, commit, push

| Command | What it does | Plain English |
|-|-|-|
| `git add <file>` | Stages a file | "Put this in the box" |
| `git add <folder>/` | Stages a folder | Stage by name. Avoid `git add -A` |
| `git commit -m "message"` | Saves a snapshot on your computer | "Seal the box and label it" |
| `git push` | Sends commits to GitHub | "Ship the box" |
| `git push -u origin <branch>` | First push of a new branch, sets tracking | Once per branch. After that, plain `git push` works |

**Use case:** `git add` followed straight by `git push` does nothing useful. Staging is not saving. Nothing was committed, so nothing was in the box to ship.

**Fun fact:** every commit gets a 40-character ID (a SHA-1 hash) computed from its contents. `a1b2c3d` is enough to name one, because the first 7 or so characters are usually unique.

---

## 3. Branches

| Command | What it does | Example use |
|-|-|-|
| `git checkout -b name` | Creates a branch and switches to it | `git checkout -b feature-ndvi` |
| `git switch -c name` | Newer form of the same | Same |
| `git checkout main` | Switches to an existing branch | Parking work, then returning |
| `git switch main` | Newer form | Same |
| `git branch -d name` | Deletes a merged branch, refuses if unmerged | Cleanup. Safer than `-D` |
| `git branch -D name` | Force-deletes, even unmerged | Only when the work is expendable |

**Fun fact:** a branch is a tiny text file holding one commit ID. Creating one costs almost nothing, so make them freely. A branch label only moves when you commit on it, which is why `main` stays put while you work on `feature-ndvi`.

**Trap:** uncommitted edits follow you to the new branch. Commit first, then switch.

---

## 4. Merging

| Command | What it does | Example use |
|-|-|-|
| `git checkout main` then `git merge feature-ndvi` | Brings `feature-ndvi` into `main` | Always switch to the receiving branch first |
| `git merge --abort` | Cancels a merge in progress | When a conflict scares you |
| `git add <file>` then `git commit` | Finishes a conflict resolution | After deleting the `<<<<<<<` markers |

**Three outcomes:**
- **Fast-forward:** the label just moves. Silent.
- **Merge commit:** vim opens for a message. Press `Esc`, then type `:wq`.
- **Conflict:** markers appear in the file. Edit, delete the markers, add, commit.

**Trap:** running `git merge feature-ndvi` while you are on `feature-ndvi` says "Already up to date", because you merged a branch into itself. Run `git branch` first.

---

## 5. Syncing with GitHub

| Command | What it does | Example use |
|-|-|-|
| `git clone <url>` | Downloads a repo | Once per repo |
| `git clone -b <branch> <url> <folder>` | Clones one branch | Testing a branch on a clean copy |
| `git fetch origin` | Downloads GitHub's state, changes no files | Safe peek before merging |
| `git pull` | Fetch plus merge | When GitHub is ahead of you |
| `git pull --no-rebase origin main` | Pull and merge, no rebasing | Safe default when you and GitHub both have new commits |
| `git pull origin main --allow-unrelated-histories` | Merges two repos that started separately | Two repos that each began with their own README |
| `git remote set-url origin <url>` | Changes where `origin` points | Switching to a new repo |
| `git remote add origin <url>` | Adds a remote, errors if `origin` exists | First-time setup only |

**Fun fact:** `origin` is not special. It is the default nickname for the remote you cloned from. You could call it `banana`.

**Memory trick:** a push rejected with "fetch first" means GitHub has something you lack. Fetch or pull, then push.

---

## 6. Undo and rescue

| Command | What it does | Danger |
|-|-|-|
| `git restore <file>` | Discards unstaged edits to a file | **Permanent.** Cannot be recovered |
| `git restore --staged <file>` | Unstages, keeps your edits | Safe |
| `git reset` | Unstages everything, files untouched | Safe. Clears a confusing staged list, for example after clicking around RStudio's Git pane |
| `git checkout -f <branch>` | Switches and discards local changes | **Destructive.** Back up first |
| `git stash` | Shelves uncommitted edits | Safe. "Put it in my pocket" |
| `git stash pop` | Takes them back out | Safe |
| `git reflog` | History of everywhere HEAD has been | Safe. The rescue tool |
| `git rm <file>` | Deletes a file and stages the deletion | Removing a scratch script such as `old_test.R` |

**Fun fact:** `git reflog` keeps recent moves for about 90 days by default, so a "lost" commit is usually recoverable. Committed work is very hard to destroy. Uncommitted work is not.

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
2. Why does an uncommitted edit follow you to another branch?
3. Why must you switch to `main` before merging a feature branch into it?
4. What does "fetch first" mean, and what fixes it?
5. Which undo commands are permanent?
