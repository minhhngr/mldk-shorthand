# Linux Control

## SSH Confiuaration
(Only WSL)
- mkdir -p ~/.ssh
- cp /mnt/c/Users/<YourUsername>/.ssh/id_rsa ~/.ssh/
- cp /mnt/c/Users/<YourUsername>/.ssh/id_rsa.pub ~/.ssh/
- chmod 700 ~/.ssh/
- chmod 600 ~/.ssh/id_rsa
- chmod 644 ~/.ssh/id_rsa.pub

## Oh my ZSH

- sudo apt install zsh (sudo apt-get install zsh)
- sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

Optional

ZSH Autosuggestions
(https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md)
- Clone repository: git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
- Open your ssh: nano ~/.zshrc
- Add the plugins: plugins=(git zsh-autosuggestions)
- (Optional) Change style color:
  - Below the "Set personal aliases ...., run 'alias'" added: ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=white,bold,bg=#ff00ff,bold"
- Apply changes: source ~/.zshrc

## Brew install

Added `brew` to `Bash`
- Step 1: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- Step 2: Follow 'next steps' in shell

  Example

    Run these two commands in your terminal to add Homebrew to your PATH:
    - (echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/minhhuynh-ubuntu/.bashrc
    - eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
    
    Install Homebrew's dependencies if you have sudo access:
    - sudo apt-get install build-essential

    We recommend that you install GCC
    - brew install gcc

Added `brew` to `zsh`

- Step 1: nano ~/.zshrc
- Step 2: Below the "Set personal aliases ......., run 'alias'"
- Step 3: Added path to the line (like example above install)
  - (echo; echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"') >> /home/minhhuynh-ubuntu/.zshrc
  - eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

### Brew Software

#### Python3
 - brew install python3
 - brew install python3@3.10 # specific version

#### NodeJS
 - brew install node

#### Java 
 - brew install openjdk
 - brew install openjdk@8

# Network Analysis Tools Setup Guide

Follow these installation instructions to set up the tools on your system.

### Ubuntu/Debian

To install the tools on Ubuntu or Debian systems, open your terminal and execute:

```bash
sudo apt-get update
sudo apt-get install net-tools iproute2 nmap traceroute
```

### CentOS/Red Hat

```bash
sudo yum update
sudo yum install net-tools iproute nmap traceroute
```

