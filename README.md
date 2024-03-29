# Starmart

## Installing

The following command will, not only install the starmart CLI tool, but also the helper classes for returning the correct output.

```bash
pip install starmart
```

## CLI Usage

**NOTE**: On Windows, all commands must be prepended with a `python -m ...`. Example: `python -m starmart init`.

Once you've installed the CLI tool (see **Installing** section), go to an empty directory and run:

```bash
# sudo privileges are needed for adding gitlab ssh key in case there's none. 
# If you already have one, you can run it without sudo. 
sudo starmart init
```

This command will create a starter project to which you would need to add all your code. It'll prompt you to sign in to your account. After that, a git repository will be configured with an alternative remote called **starmart**.

In order to deploy the code, you must first add and commit all the files you would like to be pushed to the remote repository. This is the way starmart knows which files to push. So, in order to deploy you should run the following commands: 

```bash
# Adding all files to git. Feel free to select specific files if you need to
git add .

# Adding a commit message.
git commit -m "Descriptive commit message"

# Deploying the code. This will push all the files to the remote repository, 
# build a model runtime environment and make it available for the public. 
# Running starmart deploy is equivalent to running git push starmart main. 
starmart deploy
```