# DATA 515: The shell

## File systems

Let's start at the beginning. The data on your computer is stored in what we call a "file system". A file system is composed of "directories" or "folders", each of which contain other directories or individual "files", which contain data. This file system is actually a tree.

                          / (root)
                             |
               -----------------------------
              |              |              |
         Applications      System         Users
              |              |              |
             ...            ...     ---------------
                                   |               |
                           melissawinstanley     alice
                                   |               |
                             ------------         ...
                            |            |
                        Documents    Downloads
                            |            |
                        ---------       ...
                       |         |
                      foo       bar.txt

A "path" is a route from the root to a file or directory.

We can refer to things in the file system either by their "absolute path" or their "relative path".

* The "absolute path" lists every directory that exists between a file and the root. For instance, in the prior example, the absolute path of bar.txt would be
    ```
    /Users/melissawinstanley/Documents/bar.txt
    ```
* The "relative path" says that, relative to the current directory that we're looking at, what is the path the the file? For instance, if we are currently in the "melissawinstanley" folder, then the path to bar.txt is only the part that occurs after melissawinstanley in the file tree.
    ```
    Documents/bar.txt
    ```

## What you're used to

Typically, when we're using a computer, we use a graphical user interface or "GUI" to accomplish tasks. For instance, when I start up my computer, I see a text box that I click on and enter my password, then see a "desktop" that displays many buttons for different applications. If I want to view a text file on my Mac, I click on a button that launches an application called Finder. Finder displays a list of all the folders and files on my computer, and I can click through to change folders and double click to open a file in another application called TextEdit. I can then modify the file and save it by clicking on the menu bar and then on the "Save" option. I can copy a file by right clicking on its name and selecting the "copy" option, or I can click, hold, and drag the file to move it someplace else. I can delete the file by right clicking on it, or by clicking and dragging it to the "trash can".

## A textual alternative

In this class, we're going to translate these operations from a graphical user interface to a textual user interface. Instead of clicking on things, we'll use the keyboard to get around.

Let's try it. In order to do this, we use an application called a "terminal". To get to text-world, we open up the Terminal (in Windows, make sure you're using WSL).

Now where are we? What do we see? We are running a program called a "shell" on your computer. The "shell" takes text that you type ("commands") and executes the programs that correspond with those commands. All of the "commands" that we are about to talk about are actually little programs that do things.

"Click on Finder button to display files" becomes

```sh
$ pwd
/Users/melissawinstanley
$ ls
foo bar.txt
```

Here, "pwd" stands for "present working directory", and it launches a computer program that displays the path to the current directory, where you are. We are in a folder called "Users" and a subfolder called "melissawinstanley" (which is what we call my "home directory", just like your user's directory in Mac or Windows). "ls" stands for "list segments", and it lists all the files and folders within the present working directory. In this case, there is a folder called "foo" and a file called "bar.txt" in the current directory.

You can also provide arguments to a shell commend. You can add a folder after "ls" if you want to see the files inside a sub-folder. If there is a folder named "foo" in the present working directory, you can do

```sh
$ ls foo
bar baz
```

"Double clicking on a folder to view the files in that folder" becomes

```sh
$ cd foo
$ pwd
/Users/melissawinstanley/foo
```

Here, "cd" stands for "change directory", and we move from the current directory to a child directory called "foo". Note that here we've used the "relative path" for the child directory foo - since we are currently in the directory /Users/melissawinstanley, we can provide the name of "foo" relative to that directory, which is just "foo". We could also have done this same thing with the "absolute path" of foo.

```sh
$ cd /Users/melissawinstanley/foo
```

How could I get back to the original directory? By providing the name of that directory.

```sh
$ cd /Users/melissawinstanley
```

"View the contents of a file" becomes

```sh
$ cat test.txt
This is an example text file.
```

"cat" is a command that displays the stuff that is stored in a file.

"Copy a file" becomes

```sh
$ cp test.txt test2.txt
$ cat test2.txt
This is an example text file.
```

"cp" stands for "copy" and it copies the first file (test.txt) and names the copy the second file name provided (test2.txt). Now if we "cat" the new file, we see that it contains exactly the same text as the original file.

"Drag and drop a file to move it" becomes

```sh
$ mv test2.txt test3.txt
$ cat test2.txt
cat: test2.txt: No such file or directory
$ cat test3.txt
This is an example text file.
```

"mv" stands for "move", and it moves the file to the new name and location. It removes the old file, as we can see when we try to "cat" it (it no longer exists).

"Remove a file by right-clicking and selecting delete" becomes

```sh
$ rm test3.txt
$ cat test3.txt
cat: test3.txt: No such file or directory
```

"rm" stands for "remove", and it deletes the file. It's important to note that for both mv and rm, there is NO undo. You can't undo this by dragging a file from the Trash back to the desktop - so be careful what you're doing.

## Why text?

OK, so why would we actually want this? Isn't a GUI a much better option?

* Power users can go faster in a text-based world
    * Using a mouse is actually slower for many things than just typing
* Low bandwidth (good for remote operation)
    * We're using a "remote machine" - for example, a Google engineer has a dedicated computer in a data center
    * All interactions with that machine must go over WiFi
    * A GUI is complicated - if we send all information about the GUI over WiFi, things can be really slow
    * Text is cheap to send back and forth over the network - so it's faster
* Users who want easy logging
    * We can easily see what went wrong (for example, "no such file or directory")
* Users who want programmability (scripting!)
    * This will be the core of the first assignments

Most computer scientists use a combination of GUIs and shells, depending what they’re doing.

## Getting help

So far we've seen a bunch of simple commands that help us navigate and examine the file system (ls, cd, cat, cp, mv, rm). But now I want to do something more complicated: I want to list not just the contents of the current directory (which I could do with "ls") but also the time at which each file was last modified. This was something easy to see in the GUI world: the Finder showed times next to the name of each file. How will we figure out how to do this?

Linux has a built-in manuals (files containing documentation) that describe the commands and programs that we've been running. We call these "man pages", and we can access them by using the "man" command.

```sh
$ man ls
```

That command gives us a large amount of information about how the "ls" command works. We can use the up and down keys to view the whole page (or, as the man page directs at the bottom of the screen, press "h" to learn more about how to navigate a man page). The man page lists how to use the ls command: provide the ls command followed by one or more "options" and then the name of a file.

```sh
ls [OPTION]... [FILE]...
```

What is an option? The man page lists those too. Options are usually represented as one or two dashes followed by one or more characters, and they customize the behavior of the command. For example, in the ls man page we can see that the "-c" command, when used with the "-lt" command, will "sort by, and show, ctime (time of last modification of file status information)". So to achieve our goal of displaying files with modification time, we can run the following command:

```sh
$ ls -c -lt
```

Options can be combined behind a single dash. The previous command is identical to this one:

```sh
$ ls -ltc
```

You can use the "man" command to find out information about other commands, too:

```sh
$ man mv
$ man rm
$ man pwd
```

Man pages are viewable online. Check out the Links section of the course webpage to find a link to the online Linux man pages reference. You can explore the documentation to learn about other commands (check out the intro link). You can also use the Linux pocket guide, if you've bought it, to learn about different commands and tools.

Another way to get help and understand how a command works is to use the --help option:

```sh
$ ls --help
```

Most built-in commands and also most more complicated programs that you run from the command line support the --help option. The output from --help is printed to the terminal, not displayed in the nice format of the man page, but it is another option for you.

What if you forget all the things that we've discussed today? Well the shell will help you out if you just type "help".

```sh
$ help
```

## Special characters

In the ls man page, you may have noticed a couple options that refer to . (one dot) and .. (two dots). What do those mean?

There are some "special characters" that you can use in the shell.

    .   # current directory
    ..  # parent directory
    ~   # home directory for your user

We can use these commands to simplify navigating the file system. To navigate up one level, before we had to give the full path of the parent directory:

```sh
# if we are in /Users/melissawinstanley/foo/baz
$ cd /Users/melissawinstanley/foo
```

But now, we can use the .. shortcut to do the same thing:

```sh
$ cd ..  # moves one directory up in the file system
```

Similarly for the home directory:

```sh
$ cd /Users/melissawinstanley # old version
$ cd ~                        # using the special tilde character
```

## Shell history, autocomplete

Typing all these commands is a lot of typing! I thought I said that the shell can be a lot faster than a GUI? There are a few ways to make things faster.

If you start typing a file name, you can use the tab key to autocomplete the file name. For example if I start typing this:

```sh
$ less An
```

and then I hit tab, if there is a file that starts with An in the current directory, it will auto-complete for you.

```sh
$ less AnnaKarenina.txt
```

You can also use the up arrow to get to previous commands (and the down arrow to get back again).

Similarly, the "history" command will list out all the commands that you've used in the past.

```sh
$ history
    1  cd books
    2  ls AnnaKarenina.txt
    3  history
```

(what's that "less" command that I just used? use "man" to find out what it does! there's also a "head" and a "tail" command that might help you out!)

## Filename metacharacters

How else can we do things faster in the shell? The shell is actually not just a simple program that takes a command and executes it. It can also take that command and perform SUBSTITUTIONS in order to avoid having to type file names directly.

For example, the "*" character is a special character. It means "all files in the current directory". So if I am in a directory that contains two sub-folders bar, and baz, then "ls *" will essentially perform "ls bar baz". It will substitute all files into the command.

```sh
$ ls *
bar:
a.txt  b.txt  test2.txt  test.txt

baz:
pun.txt
```

So I lied a bit. "*" actually stands for "zero or more characters". So if you add additionally characters around the star, you can get different results.

```sh
$ ls bar/*
bar/a.txt bar/b.txt bar/test2.txt bar/test.txt
$ ls bar/test*
bar/test2.txt  bar/test.txt
```

The ? character is also special - see if you can figure out what it means using man pages or the internet!

OK, but what if I ACTUALLY want to use the asterisk character, and I don't want to use it in this "zero or more characters" sense? If you actually want am asterisk, you can surround it with quotes ("", or '*'). This is easy to see with the "echo" command, which echos what you give it as input.

```sh
$ echo *
bar baz
$ echo "*"
*
```

## Text editor

Now we're at a point where we really need a text editor so we can modify files. There's a lot of different command line text editors and a lot of passionate people who prefer one in particular. I *do not care* which text editor you use. My preferred text editor is emacs, but that's often more complicated than beginners need. I recommend nano for you all. You can read how to install it in the Software section of the course website.

## Customizing your experience

In your home directory, you can have two special files called ".bashrc" and ".bash_profile". These are files to customize your bash shell. I showed my .bash_profile file.

```bash
# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/Users/melissawinstanley/opt/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/Users/melissawinstanley/opt/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/Users/melissawinstanley/opt/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/Users/melissawinstanley/opt/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

eval "$(/opt/homebrew/bin/brew shellenv)"

export NVM_DIR="$HOME/.nvm"
  [ -s "/opt/homebrew/opt/nvm/nvm.sh" ] && \. "/opt/homebrew/opt/nvm/nvm.sh"  # This loads nvm
  [ -s "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm" ] && \. "/opt/homebrew/opt/nvm/etc/bash_completion.d/nvm"  # This loads nvm bash_completion

export EDITOR="/usr/bin/pico"
export PS1='\h:\w$ '
```

We talked about the different elements of the file. There is the stuff that miniconda set up for me. There's some stuff that helps me use "homebrew", a management program that helps me install other programs. There's some stuff related to "NVM" which is for my personal projects that use Node.js. And finally, there's a setting for the default text editor to use and setting my prompt (the stuff that you see before each command) - you can actually set the PS1 to whatever you want!

Your .bashrc and .bash_profile file is loaded on startup (when you login via ssh), or whenever the "source" command is run. "source" is a builtin command in bash that says "execute every line as if the user had typed it in directly in the shell". So if you modify your .bashrc or .bash_profile files, you will need to run "source" in order for it to actually use your changes:

```sh
$ source .bash_profile
```

As for the differences between .bashrc and .bash_profile - research it if you're interested, but it's not important for this class!

## Scripting

We can actually write shell "programs" - we'll call them scripts. In fact, we've already seen one! The .bash_profile file is a type of script - a series of commands like what you'd see in the regular Terminal. When we ran it with `source`, it executed the commands in the order we saw them. But we'll dive in more deeply and understand how to write these programs ourselves.

Let's start with something simple - something that you might want to do as a data scientist. Let's write a program that downloads a data file and prints out the first few lines.

The data file I want to look at here, as a demonstration, is the data from the Pronto bike share - do you remember that being in Seattle, a while back? This is a fun data set that shows all of the trips that members took.

When I'm writing a shell script, I always try to do the things that I want to do in the regular terminal first. In this case, let's make a new directory called `pronto_data`. How do we make a new directory? Let's google for it!

It turns out there's a command `mkdir` to make a directory:

```sh
$ mkdir pronto_data
```

Let's move into the directory so we can work within it:

```sh
$ cd pronto_data
```

Now I want to download the bike share data. I found it online, but how do I download a file using the terminal. Google can help with that too - it shows that there are two options: wget and curl. I don't have wget on my computer, but I can read about curl using:

```sh
$ man curl
```

If I just curl, it's going to output everything to the terminal:

```sh
$ curl https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
```

But I want to save it in a file! Looking at the man page, we can see that there is a `-o` option that we can use to tell curl to put the data in a file:

```sh
$ curl https://s3.amazonaws.com/pronto-data/open_data_year_one.zip -o pronto.zip
```

That file is an archive. We want to unzip the zip file. How do you think we do that? `unzip`!

```sh
$ unzip pronto.zip
```

Now I want to examine some of that data. If I `cat` an entire file, it's huge! Too big. I just want to see some of it. Google tells us we can use `head`.

```sh
$ head 2015_trip_data.csv
```

Tada! We've done it. Now we can put all of those commands together into a file - a script. Just create a new file (download_pronto.sh) and put all those commands in one line after another. You'll need to put the following line at the very top of the file:

```sh
#!/bin/bash
```

This indicates that this program is a shell program - the shell should use /bin/bash (which is the shell itself) to execute the commands. Note that the program here could really refer to any program - like python, for example. The shell will find the program you specified and run it with the contents that follow the first line. (fun fact: the extension at the end of file, `.sh`, doesn't matter!)

To run a script that you've made, you can issue a command with the name of the script preceeded by `./`:

```sh
$ ./download_pronto.sh
```

But what's this? It doesn't work.

```sh
bash: ./download_pronto.sh: Permission denied
```

It turns out that each file in the file system also has the concept of "permissions". Who owns the file? Who is permitted to view it? Who is permitted to edit it? For example, if there are multiple users on a computer and I try to see the files in someone else's personal directory, I'm going to get an error, because your user owns it and not me:

```sh
$ cd /Users/someoneelse
-bash: cd: /Users/someoneelse/: Permission denied
```

We can see who owns each file and what they're allowed to do by running the ls command with an extra "-l" option.

```sh
$ ls -l download_pronto.sh
-rw-r--r--  1 melissawinstanley  staff   327B Jan  3 16:07 download_pronto.sh
```

When we do this, we can see that each of I "own" the file (that's what the "melissawinstanley" means). We can also see a set of permissions that look like a combination of "drwx" and dashes. What does this mean? Well, the r means "read", w means "write", and x means "execute" (coming soon). And there are permissions for three different categories of people: the owner, the "group" (won't discuss this right now), and everyone. So in the above example, the owner can read, write or execute the file; anyone in the group can read or write the file; and the general population can read the file.

You can change the permissions on a file by using the command "chmod" (which stands for "change mode"). Look at the man page for chmod to learn more. If I want to enable anyone to execute the script, I can say:

```sh
$ chmod a+x download_pronto.sh
```

Now we can run the file as expected!

```sh
$ ./download_pronto.sh
```

Why can't I do `download_pronto.sh` directly, without the `./` at the front? Hint: it has to do with what's called the "PATH" environment variable.

## I/O Streams

Each program needs a way to interact with the outside world - a program that is running on the computer but doesn't have a way to get input from you or to show you the result of its computation is not very useful!

We classify the modes of interaction into three categories:

* Input. How does the process get data?
* Output. How does the process show the results of its computation?
* Error. How does the process communicate diagnostic information or things that went wrong?

We call these "I/O streams" for "input" and "output".

Each I/O stream has a default implementation.

* Input: "stdin" - the keyboard
* Output: "stdout" - the screen
* Error: "stderr" - also the screen

## Redirection

What if we don't want to use the default input and output streams? Sometimes we might not want to take input manually from the keyboard, or we might want to save output in a file instead of just printing it to the screen. We call the process of changing the input and output streams of a program "redirection".

You specify redirection of input and output with another set of special characters.

    >     # Output stream to a file   ex. ls foo/ > foo_ls.txt
    2>    # Error stream to a file    ex. ls doesnotexist 2> error.txt
    >>    # Output stream to a file, but append to the file, don't overwrite
    &>    # Output and error streams to the same file
    <     # Input stream from a file  ex. cat < test.txt
    |     # Output stream of the first command equals the input stream of the second command (ie "piping")
          #     ex. cat AnnaKarenina.txt | less
    (and more: 2>>, &>>, <<, <<<, 2>&1)

Redirection is done entirely in the shell - the programs that you are running know nothing about it. All they have is a way to get input and a place to write output.

How could we use redirection instead of the `-o` option for the curl command, to redirect curl's output to a file? We could also do:

```sh
curl https://s3.amazonaws.com/pronto-data/open_data_year_one.zip > pronto.zip
```

Piping is a vary powerful idea. It means we don't have to execute commands in isolation - now we can string them together! This takes small, simple commands and creates a more useful output. For instance, curling the bike data produces a lot of output. We can navigate that output better by doing:

```sh
$ curl https://s3.amazonaws.com/pronto-data/open_data_year_one.zip | unzip
```

This takes the output of curl - which is a lot - and unzips it - all in one line!

One particular file on every Linux system that is useful when doing redirection is the file /dev/null. What is this file? Read up on it on your own and figure it out.
