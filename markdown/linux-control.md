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

- sudo apt install zsh
- sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

Optional
- https://github.com/zsh-users/zsh-autosuggestions/blob/master/INSTALL.md

## Brew install

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

### Brew Software

#### Python3
 - brew install python3
 - brew install python3@3.10 # specific version

#### NodeJS
 - brew install node

#### Java 
 - brew install openjdk
 - brew install openjdk@8
