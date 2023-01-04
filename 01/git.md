DATA 515: Git

We've been talking about tools that you can use in the terminal and for programming, and we'll continue with version control.

## Version Control

Programmers use a group of technologies called "version control" to make them more productive and effective. Version control was developed to address three problems:

1. Backups. In order to prevent loss of data when your computer crashes or dies, you should back up your work somewhere else.
1. Collaboration. If you're working on a large project with someone else, how do you collaborate? Do you email files back and forth? Do you save things in a common Google Drive folder? Neither of these are very scalable solutions if you have a large project with many files and many collaborators. How do you deal with conflicting changes from differing people? How do you keep track of which version is the "final" version?
1. Version log. Have you ever made a mistake and tried to undo it with CTRL-Z, but been unable to do so because Word or whatever program you were working with wouldn't go back far enough? Version control helps with this problem by keeping a log of all previous changes and allowing you to retrieve those versions whenever you like. 

Version control solves these three problems by managing files and coordinating how they are shared across computers. We'll discuss the theory behind it and then how to use it.

There are many different actual programs that do version control: git, subversion, mercurial, perforce, and others. Each of these works in a slightly different way, but the concepts are similar and can be extended from one to the other. We'll use git in this class.

None of these version control systems is language-specific or file-type-specific. Commonly people store source code in a version control system, but you can store whatever type of files you like! We use a git repository for storing course administrative files related to DATA 515, for example, which consists of source code, class website, PowerPoint presentations, pdfs, Word documents, and text files. Some people use source control for everything they do. (Note however that version control systems were originally built and optimized for text files - while you can store photos and videos in them, this may be less efficient due to how version control stores changes).

Finally, it's totally ok not to memorize all of the commands that we'll talk about! Know the concepts and the basics, and look up the rest as you need it.

## Theory

The most traditional type of version control system is called a "distributed version control system."

* A project lives in a collection called a "repository" (essentially a folder).
* Each user has their own copy of the repository (in the following diagram notated with "R").
* A user "commits" changes to their copy of the repository to save them.
* Other users can "pull" changes from that repository into their own local repository.
* The repository's history of commits ends up getting represented as a directed acyclic graph - a "DAG" or tree - because different people's versions of the repository can fork from each other.

```
  Distributed version control

     -------       -------
    | Alice |     |  Bob  |
     -------       -------
      | R | <-----> | R |
       ---           ---
        ^             ^
        |             |
        |     ---     |
         --> | R | <--
            -------
           | Carol |
            -------

```


The distributed version control system is powerful, but in large projects with a lot of collaborators, it can be infeasible for every person to pull changes from every other person. As an alternative to distributed version control, many projects use a "centralized version control" system:

* Users have a shared repository (called "origin" in git) which lives on some central server.
* Each users "clones" the repository to create a "local" copy.
* A user "commits" changes to their copy of the repository to save them.
* To share changes, a user "pushes" their local changes to the origin.
* All users "pull" from the central server periodically to get changes (instead of from each other).
* We call the central repository the "remote" repository - to access the remote repository, you'll need authentication to validate your permission to access the shared repository.
* Once code is pushed to the central server, the history of commits is linear, not a DAG.

We'll use a central repository model for DATA 515 (like most companies that use git), using a service called "GitHub" to maintain the central shared repository.

```
       Centralized version control

           --------------------
          | Central repository |
          |      (GitHub)      |
           --------------------
         -------> | R | <-------
        |          ---          |
        |           ^           |
        |           |           |
        |           |           |
        v           v           v
       ---         ---         ---
      | R |       | R |       | R |
     -------     -------     -------
    | Alice |   |  Bob  |   | Carol |
     -------     -------     -------
```

Typical terminology for tasks that you'll accomplish with version control:

* Create a ...
    * new repository/project - this is fairly rare and only occurs when you're starting a new collaboration.
    * new branch - they are used for independent development on subprojects while still allowing for collaboration.
    * new commit - a single change, which should be significant but not too large. This will happen daily or more.
* Push - regularly, whenever you have made commits.
* Pull - also regularly, so that you can make the best choices given the work that other people have been doing.

## git

In DATA 515, we will be using git as our version control system, with GitHub as our central repository.

There are three main steps to getting a repository set up in git:

* Create a repository. In GitHub this can be accomplished by selecting the "+ New Repository" button in the GitHub UI.
* Set up your credentials and configuration. You can check out [GitHub's instructions](https://docs.github.com/en/get-started/getting-started-with-git) on how to do this using `git config`.
* Clone the repository onto your local computer using the "git clone" command.

```sh
$ cd where-you-want-to-put-it
$ git clone https://github.com/UWDATA515/lecture-materials.git
```

A typical workflow for working on code in a git repository is as follows:

```sh
# Get the latest version of the code from the central repository.
# Pull often to prevent merge conflicts (see below).
$ git pull

# Edit the files
$ nano foo.py

# Check the status - what files have changed?
$ git status

# Mark the file "foo.py" as ready for the next commit.
$ git add foo.py

# View the line-by-line differences between the last commit and
# any uncommitted local changes.
$ git diff

# Actually commit the change to git - "save" it. Commit messages
# should be descriptive of what you changed to help others understand
# what changed.
$ git commit -m "added new function do_foo to the foo module"

# View the history of all commits in the repository
$ git log

# Push the new commit to the central repository.
$ git push
```

Gotchas and more advanced things (use "man git" to learn more):

* git has special rules around moving and removing files: you can't just run a normal "rm" or "mv" command and expect git to understand (lots of error messages!). Instead, you'll need to use the git-specific "git mv" and "git rm" to move and remove, respectively.
* Sometimes you've been making a bunch of changes, but you decide that you don't like them and want to undo them (you haven't made any commits yet). To reset your local repository to the last commit (forget all changes that you've made), you can run "git reset --hard HEAD". Here "HEAD" refers to the most recent commit.
* If one of your past commits was BAD, you can undo it using "git revert"! If the second-to-last commit was bad, you can undo it by saying "git revert HEAD~1", where HEAD is the most recent commit and "1" signifies the one before it. This will create a NEW commit that is the opposite of the original commit.
* Commits aren't completely static and permanent. If you make a commit but then realize you forgot one little thing, you can "amend"/modify your previous commit rather than creating a brand new commit using "git commit --amend".

## Summary

* Git is another tool for letting the computer do what it's good at.
    * MUCH better than manually emailing files, adding dates to filenames, etc.
    * Managing versions, storing the differences between versions.
    * Keeping source-code safe (so local crashes won't lose data).
    * Preventing concurrent access, detecting conflicts with collaborators.
* Full git docs and a book are online, free and downloadable, but beware of complexity - much of what they describe is beyond the scope of DATA 515. Keep it simple!
* Ask for help when you need it - git has a steep learning curve.
