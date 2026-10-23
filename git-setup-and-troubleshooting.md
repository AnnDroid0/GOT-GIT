# Git Setup and Troubleshooting

One-time configuration, the vim screen that traps everyone, and a decoder for the errors beginners hit most.

**Companion files:** `git-core-commands.md`, `git-shell-basics.md`, `git-sharing-and-collaboration.md`

---

## 1. Setup and config (mostly one-time)

| Command | What it does |
|-|-|
| `git --version` | Shows the installed git version |
| `git config --global user.name "Your Name"` | Sets the name on your commits |
| `git config --global user.email "you@example.com"` | Sets the email on your commits |
| `git config --global core.editor nano` | Replaces vim for commit messages |
| `git credential-manager --version` | Confirms Git Credential Manager (GCM) is installed |
| `git credential-manager configure` | Registers GCM as your credential helper |
| `git config --global --get-all credential.helper` | Shows active credential helpers. You want only the GCM path |
| `git config --show-origin --get-all credential.helper` | Shows which config file adds each helper |
| `git config --global --unset-all credential.helper` | Removes all helpers. Rerun `configure` afterward |
| `git config --global credential.useHttpPath true` | Keeps credentials separate per repo |
| `git config --global credential.gitHubAuthModes pat` | Makes GCM ask for a personal access token instead of browser sign-in |

**Credential helpers in one paragraph:** over HTTPS, git needs to prove who you are. A credential helper stores that proof so you are not asked every time. Having two helpers chained (for example `osxkeychain` and GCM) can cause confusing double prompts or stale credentials answering first. Check with `--get-all`, and keep only one.

**Scope matters:** browser sign-in through GCM usually gives a token covering your whole account. A fine-grained personal access token can be limited to a single repo. If you want the narrower one, use the `pat` setting above.

**SSH or HTTPS?** Run `git remote -v`. URLs starting `git@` use SSH keys, and credential helpers do nothing for them. URLs starting `https://` use helpers.

---

## 2. Vim escape (the git screen you will hit most)

Git opens vim when it needs a message and you did not give one, for example on `git commit` without `-m`, or on a merge.

| Goal | Keys |
|-|-|
| Save and finish | `Esc`, then `:wq`, Return |
| Quit without saving | `Esc`, then `:q!`, Return |

If letters appear in the file as you type, you are in insert mode. Press `Esc` and retry.

On a commit message screen, `:wq` finishes the commit and `:q!` aborts it.

To avoid vim entirely, run `git config --global core.editor nano`. In nano, Ctrl+X exits and it asks whether to save.

**Fun fact:** "how do I exit vim" is one of the most viewed questions on Stack Overflow, with millions of views. You are in very large company.

---

## 3. Error decoder

| What you see | What it means | Fix |
|-|-|-|
| `Nothing specified, nothing added` | `git add` with no file name | Name the file |
| `rejected ... (fetch first)` | GitHub has commits you lack | `git pull`, then `git push` |
| `rejected ... (non-fast-forward)` | Your branch is behind or diverged | `git pull --no-rebase origin main`, then push |
| `rejected (fetch first)` on the very first push | The GitHub repo was created with a README or license, so it already has a commit | `git clone` instead of `git init` (see `git-sharing-and-collaboration.md`) |
| `remote origin already exists` | Used `remote add` on an existing remote | Use `git remote set-url origin <url>` |
| `Already up to date` on a merge | You merged a branch into itself | `git checkout main` first |
| `fatal: not a git repository` | You are not inside a repo folder | `pwd`, then `cd` into the repo |
| `Your branch is behind 'origin/main'` | GitHub has commits you lack | `git pull` |
| `Your local changes would be overwritten` | Uncommitted edits clash with a merge or switch | Commit them, `git stash`, or `git restore` them |
| `CONFLICT (content): Merge conflict in <file>` | Both sides changed the same lines | Edit out the markers, `git add`, `git commit`. Or `git merge --abort` |
| `Authentication failed` or `Repository not found` | Wrong or missing credentials, or no access to a private repo | Check the helper (section 1) and token scope |
| `File ... exceeds GitHub's file size limit of 100 MB` | A large raster or dataset was committed | Add it to `.gitignore`, run `git rm --cached <file>`, then `git commit --amend` if it was the last commit. Older commits need history rewriting, so ask for help before forcing anything |
| Stuck on `:` or `(END)` after `git diff` or `git log` | Output opened in a pager | Press `q` |
| A file shows as modified and you did not mean to touch it | A command or editor rewrote it | `git diff <file>` to look, `git restore <file>` to undo |
| `unexpected symbol` or a stuck `>` prompt | Git typed into the R Console | Use the Terminal tab |
| `function>` prompt in the Terminal | R code typed into the Terminal | Ctrl+C |
| HTTP 404 on `install_github()` | Private repo and no token available to R | `gitcreds::gitcreds_set()` in the R Console |

**Reading any git error:** read the last few lines first. Git usually ends with a `hint:` that names the fix.

**Before reaching for `--force`:** do not. `git push --force` overwrites what is on GitHub, and it is almost never the right answer for a beginner. Run `git fetch` and `git log --oneline origin/main` to see what you would erase first.
