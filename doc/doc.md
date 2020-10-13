# Preparation
1. Open browser to https://code.visualstudio.com/
1. Open VSCode new window
1. Have demo repo on PC
1. Have this file open somewhere for notes
1. Be ready to connect to Cheaha via Remote Dev
1. Have repo url ready to copy onto Cheaha

# VS Code

## Introduction

- General-purpose text editor with a strong focus on facilitating programming tasks, especially JavaScript and Python.
- Built on top of Electron and written in JavaScript, so it is portable, OS agnostic, and can be displayed directly in a browser (we will use this later).
- Highly extensible with a large and diverse collection of extensions available through the Visual Studio Marketplace, many of which are open-source on GitHub.
- May be obtained from https://code.visualstudio.com/

### Quick high-level overview of features

- Opening a folder
- Command palette
- Cloning a repo
- Navigating the filesystem
- Opening files
- Editor windows
- Intellisense, autocomplete and linting
- Comment highlighting extension
- Split view
- Debugging/running files
- Opening the terminal, output windows
- Git operations and git graph extension

## Cheaha-specific Tasks

- Conda environments can be shared using YAML files, so we make sure to obtain the YAML language extension. We can use it to inspect or maintain the YAML file by modifying a version number for a package, etc.
- We can conda create the environment and reload the window to refresh.
  - `conda env create --name <name> --file <env.yml>`
  - `ctrl+p` -> `Developer: Reload Window`
- Once the extension is loaded, we should be able to look through our list of environments and pick the one we just created.
  - `bottom-left of status bar`
- If we open a new terminal window, it should conda activate that environment in that terminal window. We can type python to, say, test out an assumption about some builtin function.
- When we modify our code, intellisense knows about what is available in the environment, and gives us autocomplete choices that make sense. It also lints the file based on the environment.
- If we switch to a different environment, then the linter will say some imports aren’t valid.
- We can even load Jupyter notebooks, though the current UX is not up to par with Jupyter server itself. Many features are missing including find/replace, and certain cell operations.

## Remote Dev

- Now say we really want to do our development on Cheaha so we don’t have to keep switching between a local context and a remote context due to small bugs, differences in environment, etc. BUT! We don’t want to lose out on the VSCode experience.
- There are a couple of options, one of which is to use the Remote Development extension.
- Once it is installed, we can click on the left-right caret symbol here at the bottom left and select “Remote SSH”
- I already have SSH info prepared for Cheaha, and the info for setting it up is available online `https://code.visualstudio.com/docs/remote/ssh`
- Put in our info to get on Cheaha
- Pick a folder we wish to open
- And now we’re doing development on Cheaha like it was our local environment.
- We can even install extensions on Cheaha using ctrl+x
- We can clone the repo we've been working on.

### Limitations

- We’ve all been taught not to perform heavy tasks on the login node, because that reduces everyone’s ability to access Cheaha.
- Well...VSCode remote dev runs its server on the login node. All its subprocesses and GUI-based tasks also run on the login node. That means Jupyter notebook server, git operations, file management operations (mv, cp, rm), debuggers, linters, everything.
- Furthermore, VSCode doesn’t source bashrc, so no modules are loaded. That means we’re using stock git and no other special software.
- We can open a terminal window and create a job context there, but ONLY that terminal window will be in the job context. From here we can load modules and perform tasks like starting jobs, running git operations using a more recent version of git, etc. But that job context doesn't translate back to tasks performed by the GUI.
- There is an alternative way of using VSCode on Cheaha which gets around some of these limitations using the app sandbox.
