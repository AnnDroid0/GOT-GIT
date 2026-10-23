# Git Sharing and Collaboration

Starting a new repo, contributing to someone else's, and keeping a public repo safe, with earth observation in mind.

**Companion files:** `git-core-commands.md`, `git-setup-and-troubleshooting.md`, `git-shell-basics.md`

---

## 1. Starting a new repo: clone or init?

The deciding question: **did you create the GitHub repo with a README, license or .gitignore ticked?**

| Situation | Use | Why |
|-|-|-|
| GitHub repo made **with** a README or license (the creation form shows README On by default) | `git clone <url>` | GitHub already has a first commit. `clone` downloads it and sets `origin` for you |
| GitHub repo made **empty**, all three unticked | `git init -b main`, then `git remote add origin <url>`, then `git push -u origin main` | No history on GitHub to collide with |
| Local folder already has commits, GitHub repo has a README | Avoid. Needs `--allow-unrelated-histories` | Two histories that never met |

**Recipe A: the repo has a README**

```
cd ~/Projects
git clone https://github.com/<user>/<repo>.git
cd <repo>
git branch
cp ~/Downloads/<file> .
git add <file>
git status
git commit -m "Add <file>"
git push
```

Plain `git push` works because `clone` already set up tracking.

**Recipe B: the repo is empty**

```
mkdir ~/Projects/<repo>
cd ~/Projects/<repo>
pwd
git init -b main
git add <files>
git commit -m "Initial commit"
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```

**Fun fact:** `git init` creates a hidden `.git` folder. That folder **is** the repository, and everything else is just files. Delete `.git` and the history is gone, while the files stay.

**Trap:** if a repo is already cloned in a folder, do not clone it again. `cd` into it and, if GitHub changed, run `git pull`.

---

## 2. Forks and pull requests (contributing to a repo you do not own)

On a public repo, strangers cannot push. They **fork**, change their own copy, and ask the owner to pull the change in.

| Step | Where | Command or click |
|-|-|-|
| 1. Fork | GitHub, the repo's page | **Fork** button, top right |
| 2. Clone your fork | Terminal | `git clone https://github.com/<you>/<repo>.git` |
| 3. Branch | Terminal | `git checkout -b add-<topic>` |
| 4. Work and save | Terminal | `git add <file>`, `git commit -m "..."` |
| 5. Push the branch | Terminal | `git push -u origin add-<topic>` |
| 6. Pull request | GitHub | **Compare & pull request**, one sentence, submit |

| Word | Plain English |
|-|-|
| Fork | Your own copy of someone else's repo, on GitHub |
| Pull request (PR) | "Please pull my branch into your repo" |
| Collaborator | Someone the owner lets push directly. Not needed for public repos |
| Merge | The owner clicking the green button once the PR looks safe |

**Owner's check before merging:** open the PR's **Files changed** tab and look for tokens, data files and personal information. On a public repo, whatever you merge is public.

**Fun fact:** a "pull request" is named from the owner's side. The contributor pushes to their own fork, and the owner **pulls** from it.

**Keeping your fork current:** if the original repo moves ahead, add it as a second remote (`git remote add upstream <original-url>`), then `git fetch upstream` and `git merge upstream/main`.

---

## 3. Public repo hygiene (earth observation edition)

| Do or don't | Why |
|-|-|
| Do write a `.gitignore` before the first commit | Rasters and R history files slip in otherwise |
| Don't commit `.tif`, `.nc`, large CSVs or shapefile folders | GitHub rejects files over 100MB. Link to the data source and commit the download script instead |
| Don't commit tokens or passwords (GitHub tokens, NASA Earthdata, Earth Engine credentials, API keys) | Scrapers find leaked tokens in minutes. Deleting the file leaves it in history, so **revoke the token** |
| Don't post graded solutions or instructor materials | Academic integrity |
| Do add a license | Without one, others cannot legally reuse your work |
| Do make the work reproducible | Someone should be able to clone, run your script and get your result |

Starter `.gitignore` for geospatial work:

```
*.tif
*.nc
data/
.Rhistory
.RData
.DS_Store
```

**Very large files:** Git LFS exists for them, but GitHub's free quota is small. Treat it as a last resort and prefer links to the data source.

**License notes:**
- **CC0 1.0** gives up all rights. Anyone can reuse the work with no credit. GitHub's new-repo form offers it.
- **CC BY 4.0** requires credit to the author. GitHub's new-repo form only lists CC0 from the Creative Commons family, so CC BY would have to be added by downloading its text into a file named `LICENSE`.
- If you swap the license file, change the README's license line too, or the two will contradict each other.

**Fun fact:** CC0 is called a "public domain dedication". It is the closest a person can get to waiving copyright on purpose.

**Before you flip a repo to public, check:**
1. `git log --oneline` shows nothing you would be embarrassed by.
2. `git status` and `ls` show no data files or credentials.
3. The README says what the repo is and how to use it.
4. A license file is present.
