# Shell Basics for Git

These are not git commands, but every git session uses them. Run them in the Terminal, never the R Console.

**Companion files:** `git-core-commands.md`, `git-setup-and-troubleshooting.md`, `git-sharing-and-collaboration.md`

---

## 1. Which window am I in?

| Prompt | Window | Takes |
|-|-|-|
| Ends in `$` or `%` | Terminal | git and shell commands |
| `>` | R Console | R code only |
| `function>` or a stuck `>` in the Terminal | Terminal waiting for more input | Press Ctrl+C |

---

## 2. Moving around and looking

| Command | What it does | Example use |
|-|-|-|
| `pwd` | Prints the folder you are in | Check you are in the repo you think you are, so you never create a repo inside a repo |
| `ls` | Lists files in this folder | Confirm the files you copied are really there |
| `ls -la` | Lists everything, including hidden files | Seeing the hidden `.git` folder and `.gitignore` |
| `cd <folder>` | Moves into a folder | `cd ~/Projects/ndvi-study`. Capitals must match the folder name |
| `cd ..` | Moves up one folder | Leaving a subfolder |

**Path shortcuts:** `~` means your home folder, `.` means the current folder, `..` means the parent folder.

**Tip:** press Tab to autocomplete file and folder names, and the up arrow to bring back earlier commands.

---

## 3. Making, copying and moving files

| Command | What it does | Example use |
|-|-|-|
| `mkdir <folder>` | Makes a folder | `mkdir notes` |
| `cp <file> <destination>` | Copies a file. `.` means "into this folder" | `cp ~/Downloads/scene-list.csv .` |
| `mv <old> <new>` | Renames or moves a file | `mv draft.md ndvi-notes.md` |
| `rm <file>` | Deletes a file. **No trash, no undo** | Prefer `git rm <file>` for tracked files |

---

## 4. Writing and reading file contents

| Command | What it does | Example use |
|-|-|-|
| `echo "text" > file` | Writes text into a file, **replacing** what was there | A one-line starter `README.md` |
| `printf "a\nb\n" > file` | Same, but `\n` makes new lines | Building a `.gitignore` in one command |
| `echo "text" >> file` | **Appends** to the end instead of replacing | Adding one more line to `.gitignore` |
| `cat <file>` | Prints a whole file | Reading a short note |
| `head -3 <file>` / `tail -2 <file>` | Shows the first or last lines | `head -3 LICENSE` to see which license is inside |
| `grep -n "word" <file>` | Finds lines containing a word, with line numbers | `grep -n "Fork" README.md` to check a fix landed |

**Danger:** `>` replaces a file with no warning. Run `ls` first if the name might already exist. If the file was tracked by git, `git restore <file>` brings the committed version back.

---

## 5. Pipes, downloads and leaving things

| Command | What it does | Example use |
|-|-|-|
| `command \| head -20` | The pipe `\|` sends one command's output into the next | `git diff LICENSE \| head -20` shows only the top of a long diff |
| `curl -o <file> <url>` | Downloads a URL into a file | Fetching a license text. **Overwrites** an existing file with that name |
| `q` | Leaves a pager (`less`) | Gets you out of `git diff` and `git log` output |
| `Ctrl+C` | Cancels the running command | Escapes a stuck prompt |

**Fun fact:** the pipe `|` came to Unix in 1973. The idea behind it, small tools chained together, is why git commands are so small and specific.
