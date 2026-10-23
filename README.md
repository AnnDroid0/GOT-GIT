# GOT-GIT

Plain-language git notes for geography and earth observation work. Written by a student, for students, so the answers to common git problems live in one place.

> **Heads up:** the starter notes were written with help from an AI assistant and checked against a real project. Test a command on a throwaway repo before you trust it with work you care about.

## What is here

| File | What it is |
|-|-|
| `git-core-commands.md` | Daily commands: look, save, branch, merge, sync, undo |
| `git-setup-and-troubleshooting.md` | Config, vim escape, error decoder |
| `git-shell-basics.md` | Terminal commands that travel with git |
| `git-sharing-and-collaboration.md` | New repos, forks, pull requests, public repo hygiene |
| `cheatsheet/` | One-page PDF, plus the markdown source and script to rebuild it |
| `notes/` | Classmate contributions (see below) |
| `notes/TEMPLATE.md` | Copy this to start a new note |

## If you only remember one thing

**branch, status, add, commit, push.** Check where you are (`git branch`), check what changed (`git status`), then stage, save and send. Most beginner mistakes come from skipping the check.

## Why git matters for earth observation

Satellite and geospatial work breaks git in ways generic tutorials skip:

- **Rasters are huge.** GitHub rejects files over 100MB. A single GeoTIFF or NetCDF can exceed that.
- **Data is not code.** Commit scripts and a recipe for downloading the data, not the data itself.
- **Secrets are everywhere.** NASA Earthdata logins, Google Earth Engine credentials, API keys and GitHub tokens must never be committed.
- **Reproducibility.** Someone should be able to clone your repo, run your script and get your result.

## Add your own notes

Anyone can contribute, and doing it is a real git exercise. You cannot push straight to this repo, so you use the standard **fork and pull request** route:

1. Click **Fork** (top right of this repo's page). You get your own copy.
2. Clone your copy, not mine:
   ```
   git clone https://github.com/<your-username>/GOT-GIT.git
   cd GOT-GIT
   ```
3. Create a branch for your note:
   ```
   git checkout -b add-<your-topic>
   ```
4. Copy the template and write your note:
   ```
   cp notes/TEMPLATE.md notes/<your-name>-<topic>.md
   ```
5. Stage, commit and push:
   ```
   git status
   git add notes/<your-name>-<topic>.md
   git commit -m "Add note on <topic>"
   git push -u origin add-<your-topic>
   ```
6. On GitHub, click **Compare & pull request**, describe your note in a sentence, and submit.

Good topics: your own error and how you fixed it, a `.gitignore` for a specific data type, Git LFS, handling large rasters, git with R or Python workflows, working with a lab partner, anything that cost you an hour.

## Dos

- **Do** run `git status` and `git branch` before anything that changes something.
- **Do** stage files by name (`git add file.md`).
- **Do** write commit messages that say what changed ("Add LFS note"), not "stuff" or "update".
- **Do** make small commits, one idea each.
- **Do** write a `.gitignore` before your first commit in a data project.
- **Do** say what you tested and on what system (macOS, Windows, Linux).
- **Do** pull before you push when working with others.
- **Do** credit sources you used, including AI.

## Don'ts

- **Don't** commit data files (`.tif`, `.nc`, `.shp` folders, large CSVs). Link to where the data comes from instead.
- **Don't** commit tokens, passwords or API keys. If you do, revoke the token immediately. Deleting the file is not enough, because it stays in git history.
- **Don't** post graded assignment solutions or instructor materials.
- **Don't** include personal information such as emails, home paths or student IDs.
- **Don't** use `git add -A` or `git add .` without reading `git status` first.
- **Don't** use `git push --force` on a shared branch. It can erase other people's work.
- **Don't** run `git restore` or `git checkout -f` on work you haven't saved elsewhere. They are permanent.
- **Don't** paste commands you don't understand. Look them up first.

## Note style

- Keep it short. One problem, one fix.
- Start with the symptom (the error text) so people can find it by searching.
- Show the exact command and what you should see.
- Say what could go wrong.

## License

[CC0 1.0](LICENSE). Use, copy and adapt freely, no credit required.
