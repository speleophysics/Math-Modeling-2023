# Math-Modeling-2023
Main class repository for Math modeling class in 2023.

# Setting up your computer for Math modeling class

Below you will find summaries for setup of software and **Github** repositories for *Mathematical Modeling of Geological Processes.* 

Code in the class will be written in the [Python](http://www.python.org) programming language. **Python** is a general purpose programming language that can be used to do all kinds of things (write computer games, generate websites, data analysis and visualization, and even for *mathematical modeling!*). There are many packages available for Python that extend its basic functionality. We will need many of these packages for the exercises in this course. To make our lives easier, we will install a specific *distribution* of Python called **Anaconda**, which includes most of the packages that we will need for scientific programming in Python and also includes a variety of other useful software, such as a package management software called **conda**, which we can use to install any other packages we might need.

## Anaconda python distribution

The individual version of **Anaconda**  is free, meaning that you can easily transfer the tools that you learn in this course to wherever you find yourself working in the future (*no need for expensive licenses, e.g. as with Matlab or other similar programming languages*). 

To download and install Anaconda using this [link](https://www.anaconda.com/products/individual). Chose the installer for your OS, and make sure you *install Python 3 as opposed to Python 2*, that is, the installer should be Python 3.x of some variety. It gives a choice for 32-bit vs 64-bit. Most of you probably have 64-bit machines, so chose this option unless you know that you have a 32-bit machine. 

You can find some general information about using Anaconda [here](https://docs.anaconda.com/anaconda/user-guide/getting-started/).

## Git and Github

**Git** is a [distributed version control system](https://git-scm.com/video/what-is-version-control). It allows us to keep track of changes within our code by creating shapshots of that code (called **commits**) at different points in time. This can be incredibly useful if you mess something up in your code and want to revert to an older version. However, it also helps you to keep track of progress or go back and see the history of your changes. To install **Git**, go to https://git-scm.com/downloads.

**Github** is an online server where you can publish your git repositories. This is important because it creates an online backup of your work. It also makes it easier to share your code with others. In fact, Git and Github really shine when you have a team of programmers working on the same code. It provides a very useful workflow for collaborative programming.

## Using a terminal

#### **Windows**

To open a terminal in Windows (after installing Git) go to the search menu and start typing Git. Look for the executable called **Git Bash**. This will provide a bash shell that would be same as what you would get in Linux or MacOS. Using this version of the shell will assure that we all can use the same commands.

#### **MacOS**

To open a terminal on a Mac, see [these instructions](https://support.apple.com/guide/terminal/open-or-quit-terminal-apd5265185d-f365-44cb-8b09-71a064a42125/mac).

#### Paths

Many of the most common problems you will run into with getting set up to work with git relate to **paths**. Paths are locations within the file structure of your computer. If you have a terminal open, then it will always have a current working directory that corresponds to a particular directory (or folder) on your machine. You can change this working directory using the command `cd`. For example:

`$ cd Documents/Math-modeling`

would change the working directory to a directory called `Math-modeling` that is inside of another directory called `Documents`. This will only work if the current working directory has a subdirectory called `Documents`. Note that `/` separates directory names in the path. If you are working in Git Bash, or MacOS, then this is the character that separates directories in a path. In a plain Windows terminal, this would be a `\` instead.

*You do not type in the `$` symbol, this just indicates that you are typing the command into a terminal.*

If you want to see what your working directory is, then you can use the command:

`$ pwd`

which stands for "print working directory." This will print out the full path to the current working directory of the terminal.

There are also some characters that have special meaning in paths:

- `.` means current working directory
- `..` means one directory up in the file structure from the working directory
- `~` means the home directory for your user.
- `*` is a wildcard that means any set of characters.


If you start a path with a directory name, then the path will be a **relative path**, which is relative to the working directory, e.g.:

`$ cd Documents`

That is why this will only work if the working directory contains a Documents directory. You can provide **absolute paths** if you start with a `/`. For example:

`$ cd /Users/username/Documents`

If you just type `cd` with no path specified, then it will take you to the home directory for your user.
#### Common commands

**`ls`**

List the contents of the working directory. You can also specify a path to some other directory or file:

`$ ls Documents/Math-modeling` 

would list the contents of a `Math-modeling` directory that was contained inside a `Documents` directory that was in the working directory.

You can also use wildcards. 

`$ ls Documents/Math-modeling/*.ipynb` 

would list all of the ipython notebook files in that directory.

**`cp`**

Copy files from one path to another. To use this command you have to provide two paths. The first one is the file to copy and the second one is the place to copy it to. If you do not provide a filename at the end of the path, then it will use the same file name. For example:

`$ cp Documents\Math-modeling\asdf.ipynb Documents\My-Math-modeling\`

Would copy the asdf notebook into a directory called My-Math-modeling. This only works if the directory already exists. You can also specify a new name by ending the path with the filename you want, like this:

`$ cp Documents\Math-modeling\asdf.ipynb Documents\My-Math-modeling\my-asdf.ipynb`

**`mkdir`**

Makes a new directory at the specified path. 

`$ mkdir Documents\Modeling-project`

would create a `Modeling-project` directory in the `Documents` directory, assuming that your current working directory contained a `Documents` directory.

## Setting up git repositories for class

In class, we will use two different git repositories. One is a **main class repository** that contains code that I provide and/or create during lectures. This *is* that main repository (Math-Modeling-2023).  

The second repository will be your **own repository** where you store and track your own code. I also recommend that you create a separate repository specifically for your project, as this would help to separate out your project code from your in-class and homework code.

### Organizing your repos

You will want to decide where to put your class git repos. My suggestion is that you create a directory (i.e. folder) within your `Documents` directory called `Math-Modeling` (or within your home directory) and then put the repos within this directory.  Each repo will be in its own directory that has the same name as the repo. The name of the main course repo is `Math-Modeling-2023`. You will want to chose a different name for your own repository so that the directory names don't conflict (e.g. `Math-Modeling-Lastname` would be one option). Repo names can't have spaces.

To navigate among these directories from the terminal, you will need to use the `cd` command (change directory). This is the terminal-based equivalent of navigating around through your folders with a file browser. When you open a terminal it should start in your main user directory. Your `Documents` folder will be a subdirectory of this user directory. The commands below would get you from the main user directory down into the directory containing the main course repo, and then pull the latest copy of the repo from Github, assuming you use the same directory names suggested above,

```
$ cd Documents
$ cd Math-modeling-2020
$ git pull 
```
*Note, this will only work after you have created a local copy of the repo (see next section).*

If you then wanted to change into your own code repo directory (from the main course one), you could use the commands:

```
$ cd ..
$ cd Math-Modeling-Lastname
```

Then you could enter git commands for your repo. Note `..` means next directory up in the structure. So, when you are in one of the repo directories, `..` refers to the `Math-modeling` directory. If you were in the `Math-modeling` directory, it would refer to the `Documents` directory. 

You can also string together directory names with a `/`, so that, for example the first commands shown above could be shorted into:

```
$ cd Documents/Math-modeling-2023
$ git pull 
```
In most terminals, you can also use `Tab` to auto-complete folder and file names. Try partially typing in a folder name and then hitting `Tab`. 

### Cloning the main course repo

To clone the main course repo, you would first use `cd` to get to the directory that you want to hold the repo directory. Then you use `git clone` and the url to the Github repo you want to clone. Following the example paths from above, this would be:

```
$ cd Documents/Math-modeling
$ git clone https://github.com/speleophysics/Math-Modeling-2023.git
```

*That's it! Now you should be able to use `git pull` from the Math-modeling-2023 directory in order to update to the lastest version. Note, if you ever accidentally edit code in the main course repo and have trouble with pulling the latest version, you can run:*

```
$ cd Documents/Math-modeling/Math-modeling-2020/
$ git stash
$ git pull
```

*Alternatively, worst case, just delete the whole folder that contains the main course repo and clone it afresh.*

It will be easiest to deal with this repo if you don't actually edit the code within in. If you want to mess around with code from the main course repo, I suggest you copy the specific files over into your own repo before editing. You can use `$ git pull` from a terminal in the directory containing the repo in order to download the most recent updates to the main course repo. Alternatively, you can also use the Git GUI or the Git interface found in VS Code, which we will use frequently in class.

### Creating your own course repo

You can create your own course repo using the Github website. Navigate to your repositories (first click on your user icon in the upper right). Then click on the green `New` button. Enter the name you want to use for the repo. I suggest that you make it private and also chose a default Python template for `.gitignore`.

### Moving files into your repo

If you want to move files into your repo, for example the notebooks you have already created for the course, then you can copy them over using the terminal, or you can also copy them into the repo folder using your file browser. Once they are copied into the directory containing the folder, you will have to stage, commit, and push the new commit(s) to Github.

## Basic Git Workflow

### Pull - get new changes from Github

When you start working on the code in a repo, often the first task is to pull any new updates from Github, particularly if you previously worked on the code using a different computer. To do this, the working directory of your terminal has to be the repo directory (or some sub-directory of it). Then you run:

```
$ git pull
```

### Stage - add files into the list for the next commit

After you do some work and edit files and save them, you will want to stage those changes for a commit. Typically, you want to stage a coherent set of changes that can easily be described with a short commit message. To stage files, you use:

```
$ git add filename
```
To stage everything in the current directory, you can run:
```
$ git add .
```

### Commit - save a snapshot of the current state

Once you have a set of files with changes that are staged for commit, you can create a commit that makes a snapshot of the current state of the repo. This will only make changes to files that are staged. If you have edited but not stages (added) a file, then it won't be included. With each commit, you provide a message. This message is limited to 72 characters. It should succinctly describe the changes that were made. This will help you (or others) to understand why you made specific changes. To commit use:
```
$ git commit -m "Your short, descriptive message"
```

### Push - send the latest commits from your computer to Github

Once you have one or more commits made, you can "push" these commits to Github. Then you will be able to see them in the web interface and pull them to other computers.
```
$ git push
```
You will likely have to authenticate when you do this, at least the first time in a given session.

### Status

If you want to see the current state of your repo (are there changed files, are their staged files, are there commits that haven't been pushed) then you can get the status with:
```
$ git status
```



