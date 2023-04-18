# EE 437 Final Project

### Alex, Eugene, Tyler, Micheal, Diego, Matthew

## GitHub Download Instructions
1. Make sure you're added as a collaborator on the GitHub repository (talk to Alex).
1. Set up your git username and email, like so:
```
$ git config --global user.name "John Doe" 
$ git config --global user.email "your.email@uw.edu"
```
1. Set up an SSH key on GitHub in the linux lab, from your home directory. 
    1. type `cd ~` to get to your home directory.
    1. The [UW CSE 154](https://courses.cs.washington.edu/courses/cse154/23sp/resources/assets/vscode-git-tutorial/windows/index.html#settingupgitlabkey) page has a great tutorial for setting up your key.
1. `cd` to the folder where you would like to store your EE437 folder and enter `git clone git@github.com:Codax2000/ee437-wireline-transceiver.git YOUR_FOLDER_NAME_HERE`

## Cadence Virtuoso Instructions
1. To set up virtuoso, `cd` into the folder you just created and type `ls -al`. There will be a lot there, but don't panic.
1. Type `vi ~/.cshrc` to open your personal `cshrc` file and add the following line to it. This will add FreePDK to your environment.
```bash
source /home/lab.apps/vlsiapps/kits/FreePDK45/ncsu_basekit/cdssetup/setup.csh
```
1. Time to start virtuoso. `cd` into the `cadence` directory and type `virtuoso &`. You should be able to see two NCSU libraries (both ending with `FreePDK` and the `NangateOpenCellLibrary`)
1. There should also be a `channel_response_test` library. If you open it, you should be able to open up the spectre state for the `test_nmos` cell.
1. Before simulating, make sure to add the `freepdk45.l` to the model library. Otherwise, ADE will throw an error saying that `MO` is referencing and undefined model.


## Using Git and Version Control
