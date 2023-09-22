# GIT SHORT HAND

## Common Flows

```sh
"""
Create branch from server branch
"""

 git fetch $REMOTE_NAME
 git checkout -b $LOCAL_BRANCH_NAME $REMOTE_NAME/$SERVER_BRANCH_NAME
```

```sh
"""
Merged code local into the server
"""

 git fetch $REMOTE_NAME               # - Get the latest changes from $BRANCH in repo
 git rebase $REMOTE_NAME/$BRANCH_NAME # - Update your local against that of the main repo
 git push $REMOTE_NAME $BRANCH_NAME   # - Push your local change to server
```

```sh
"""
Fork and remote to server
"""
 
 git clone $REMOTE_FORK_URL
 git remote -v
 git remote add upstream ${REMOTE_URL}
```

```sh
"""
If you’re following a forking model is like this (let’s say the main repo is remote “main”, and you are updating your master against main’s)
"""

 git fetch $REMOTE_NAME             # - Get the latest changes from $BRANCH in repo
 git stash                          # - Put away your local change
 git merge $REMOTES($MAIN/$MASTER)  # - Update your local against that of the main repo
 git stash apply                    # - Put your local changes on top of your uopdated
```

```sh
"""
(Becarefully) Delete all commit history
"""

git checkout --orphan latest_branch
git add .
git commit -m "commit message"
git branch -D main
git branch -m main
git push -f origin main
```

## Notice command

```sh
"""
git status

Git is constantly tracking what’s going on as you make changes locally 
Git status is going to return the files in your local repository in 2 categories, untracked and tracked.

This command is very important, because 
- What it says will affect what you do next commands (add & commit)
- This status represents the changed files Git detects across your project.
"""

 git status 
```

```sh
"""
git add

Notice
------
What git add . does is that it adds literally every file Git has detected a change with to be set up for a commit
. This is dangerous if a lot of the code you’ve created is actually generated, and your .gitignore doesn’t sufficiently cover them.
. This will lead to a lot of junk getting pushed to your remote, which will constantly generate noise on pull requests

=> Only run `git add .` if everything underneath the untracked files section is stuff that you want on remote.  
"""

 git add .          # <-- Try not to do this ! (Notice)
 git add $FILE_PATH
 git add -u         # Updated tracked files
```

```sh
"""
git commit

-a (add): What this does is that it grabs all of the changes you've made to existing files and packages them into your commit
-m (mesage): This allows you to attach the message associated with the commit from the command line
"""

 git commit -m $YOUR_COMMIT_MESSAGE
 git commit -am $YOUR_COMMIT_MESSAGE 
 git commit --author="John Doe <john@doe.org>" # Changing the Author Information Just for the Next Commit
```

```sh
"""
git push

By default, Git will push to whatever remote lies at origin
It will also push all local branches that don’t match their counterparts on the remote side, counterparts being determined by a simple name match.
Keep these notes in mind for when you’re pushing to non-origin remotes and the much rarer case of your local branch not having the same name as the remote one you’re updating.
"""

 git push $REMOTE_NAME $BRANCH_NAME

 # If you want to be specific and push a specific branch to a certain remote
 git push $REMOTE_NAME $MY_LOCAL_BRANCH_NAME:$REMOTE_BRANCH_NAME 
```

```sh
"""
git fetch

By default, a fetch will fetch from whatever the origin remote is in your git repository
What fetch does is it grabs all of the new code on remote so you can play around with it locally (rebase, cherry-pick, check out a new branch, etc)
Unlike git pull, it doesn’t do anything with your local code; you are fully in control.
 => This is why git pull is risky. In short, git pull does a fetch and then a merge, which gives you less control over how you want the new code to be integrated with yours.
"""

 git fetch origin
```

```sh
"""
git diff

This tells you exactly what code changes Git is currently aware of and what the commit will look like after you add/commit whatever
This will give you the lines added/deleted for that one file.
If the diff doesn’t match your expectations, you’re going to want to hit save in whatever IDE/text editor you’re using. You can also just do a git diff, but that gives you everything you have changed so far which is kind of a mess.
"""

 git diff $FILE_PATH
```

```sh
"""
git cherry-pick

Let’s say that there’s a single commit’s worth of code that you want to test/work with. 
However, there isn’t a branch you can merge/rebase against in order to only get that commit. This is when you do a cherry pick.
"""

 git cherry-pick $COMMIT_ID
```

```sh
"""
git stash

Stash is mainly relevant when you’re merging in code
Stash does is that it hides away your work in progress code in a safe place and you can bring it back whenever
"""

 git stash       # This “hides away” your code
 git stash apply # This brings back your most recently “hidden away” code
 git stash list  # Shows you the list of stashes you have locally (yup, you can have multiple stashes, Git is great)
```

```sh
"""
git branch

Figure out which branch you’re on along with all local branches
If you’re missing a branch, you either need to convert a remote branch into a local one and/or do a fetch.
"""

 git branch -av  # Figure out what branches exist (both local and remote)
 git branch -D   # Delete local branch
```

```sh
"""
git checkout
"""

 git checkout -- $FILE_PATH   # Remove File or Directory
 git checkout $BRANCH_NAME    # Start working on another branch
 git checkout -b $BRANCH_NAME # Create a new branch
```

```sh
"""
git remote
"""

 git remote -v  # Checking Your Current Remotes
 git remote add $NAME_REMOTE $REMOTE_URL
```

```sh
"""
git config
"""

 # Changing Your Committer Name & Email Globally
 git config --global user.name "John Doe"
 git config --global user.email "john@doe.org"

 # Changing Your Committer Name & Email per Repository
 git config user.name "John Doe"
 git config user.email "john@doe.org"
```

## Topics

### GIT (Rebase >< Merge) What's the difference?

### Reference by topics

-----

* [What's the Difference?](https://phoenixnap.com/kb/git-rebase-vs-merge#:~:text=The%20main%20difference%20between%20git,the%20changes%20from%20both%20branches.&text=Allows%20users%20to%20merge%20branches%20in%20Git)
* [Why you should avoid using Git merge to update your branches?](https://blog.piotrnalepa.pl/2022/09/19/git-merge-vs-git-rebase-why-you-should-avoid-using-git-merge-to-update-your-branches/)
* [Merging vs. Rebasing](https://viblo.asia/p/git-merging-vs-rebasing-3P0lPvoGKox)

## Visualize

![Cheat sheet](../resources/git/cheat-sheet.jpeg)

![Git Commands](../resources/git/commands.gif)

## Ref

* [Hướng dẫn về git cho người mới bắt đầu](https://backlog.com/git-tutorial/vn/)
* [Getting Started With Git and GitHub in Your Python Projects](https://blog.martinfitzpatrick.com/git-github-python/)
* [Git Commands Every Software Engineer Should Know](https://www.jointaro.com/blog/git-commands-every-engineer-should-know-stop-using-version-control-incorrectly/)
