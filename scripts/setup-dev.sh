#!/bin/bash -e

echo ''
printf "    __  ____    ____          ___      __ \n\
   /  |/  / |  / / /___ _____/ (_)____/ /___ __   __ \n\
  / /|_/ /| | / / / __ \`/ __  / / ___/ / __ \`/ | / / \n\
 / /  / / | |/ / / /_/ / /_/ / (__  ) / /_/ /| |/ / \n\
/_/  /_/  |___/_/\__,_/\__,_/_/____/_/\__,_/ |___/\n"
echo '**************** 4D 56 6C 61 64 69 73 6C 61 76 *****************'
echo '****************************************************************'
echo '* Copyright of MVladislav, 2021                                *'
echo '* https://mvladislav.online                                    *'
echo '* https://github.com/MVladislav                                *'
echo '****************************************************************'
echo '* KONS                                                         *'
echo '****************************************************************'
echo ''

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ''
echo 'setup:: path:: to install without root'
echo '--> setup:: path:: go-bin'
# SETUP:: go-bin
# Install GO to /usr/local/go/bin
export PATH=$PATH:/usr/local/go/bin

echo '--> setup:: path:: go-path'
# SETUP:: go-path
# Install GO to ~/go
export GOPATH=$HOME/go
export PATH=$GOPATH/bin:$PATH

echo '--> setup:: path:: npm'
# SETUP:: npm
# Install NPM Gems to ~/.npm-packages
NPM_PACKAGES="${HOME}/.npm-packages"
export PATH="$PATH:$NPM_PACKAGES/bin"
# Preserve MANPATH if you already defined it somewhere in your config.
# Otherwise, fall back to `manpath` so we can inherit from `/etc/manpath`.
export MANPATH="${MANPATH-$(manpath)}:$NPM_PACKAGES/share/man"

echo '--> setup:: path:: ruby'
# SETUP:: ruby
# Install Ruby Gems to ~/gems
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"

echo '--> setup:: path:: make'
export PREFIX="$HOME/.local"

# read -p "Do you wish to install dependencies? [y/N] " yn
# case $yn in
# [Yy]*)
#   echo ""
#   break
#   ;;
# [Nn]*) exit ;;
# *) echo "Please answer yes or no." ;;
# esac

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
echo ''
echo 'init:: create base folder struct'

vm_project_name=vm_cli

vm_path="$HOME/.$vm_project_name"
vm_path_git="$vm_path/git"
vm_path_source="$vm_path/deb"
vm_prefix="$HOME/.local"
vm_run="$HOME/.local/bin"
mkdir -p "$vm_path"
mkdir -p "$vm_path_git"
mkdir -p "$vm_path_source"
mkdir -p "$vm_prefix"
mkdir -p "$vm_run"

echo ''
echo "init:: venv"
python3 -m venv "$vm_path/venv"
source "$vm_path/venv/bin/activate"

echo ''
echo 'inst:: dependencies...'
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# HELPER
clone_or_pull_and_cd() {
  git_link=$1
  repo_name=$(basename "$git_link" .git)
  echo ''
  echo "inst:: git:: $repo_name"
  cd "$vm_path_git"

  git clone "$git_link" 2>/dev/null || (
    cd "$repo_name"
    git pull
  )
  cd "$repo_name"
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

exit 0
