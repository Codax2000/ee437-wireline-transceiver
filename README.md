# EE 437 Final Project

### Alex, Eugene, Tyler, Micheal, Diego, Matthew

## Setup
### Creating a New SSH Key
1. SSH into the Linux server in the client of your choice, like PuTTY, MobaXTerm, or VSCode
1. Enter the following command to generate a new ssh key:
**Leave the file and passphrase blank**. If it prompts you to overwrite the file, enter `y`.
```bash
ssh-keygen -o -t rsa -b 4096 -C "YOUR_EMAIL_ADDRESS@EXAMPLE.COM"
```
1. Enter `cat ~/.ssh/id_rsa.pub` to output the new ssh key to the terminal.
1. Copy the text (`ctrl+C` works on your own computer, this is why using an SSH is easier than doing it on the Linux Servers).
1. Go to your personal settings on GitHub, under "SSH and GPG Keys" and click "New SSH Key".
1. Enter a descriptive name (like "Linux Lab Key") and paste the key into the GitHub box, and click "Add SSH Key".

### Cloning the GitHub Repository
1. In a Linux terminal, `cd` into the directory where you would like to have your `EE437` folder.
1. Enter `git clone git@github.com:Codax2000/ee437-wireline-transceiver.git EE437` into the command line. It should create a new directory
and populate it with the contents of the repository.
1. `cd` into the new folder and type `ls -al` to ensure that the contents roughly match the GitHub repository. 

### Testing Virtuoso
1. Enter `cd cadence` to enter the Cadence directory.
1. Enter `tcsh` to make sure you are using the c-shell, or this won't work.
1. Start Virtuoso by entering `virtuoso &`. The first time will take a few minutes, be patient.
1. In the library manager, you should see libraries for testing `GPDK` and `FreePDK`.

#### Testing `GPDK`
1. In the library manager, select `gpdk_test` and open the `nmos_test` schematic.
1. Launch ADE and load the `spectre_state1` simulation in ADE, under "Session > Load State", and select the `spectre_state1` _cellview_.
1. Run the simulation. It should show a VGS sweep, with high-vt, low-vt, and standard-vt devices.

#### Testing `FreePDK`
1. 

## Version Control
### Creating a New Branch
1. Go to the GitHub Issues Page and create a new issue. Describe what you will be doing.
1. On the right side, assign yourself under "Assignees".
1. Under "Development", create a new branch. The default name is fine, shorten if you like.

### Using `git` Locally