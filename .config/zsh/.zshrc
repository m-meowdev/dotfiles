# environment variables
export TERM="alacritty"
export HISTORY_IGNORE="(ls|cd|pwd|exit|sudo reboot|history|cd -|cd ..)"
export EDITOR="nvim"
export HISTFILE=~/.local/state/zsh/history
export STARSHIP_CONFIG=~/.config/starship/starship.toml
export XINITRC=~/.config/X11/xinitrc
export XAUTHORITY="$XDG_RUNTIME_DIR"/Xauthority

# plugins
plugdir=~/.config/zsh/plugins
source $plugdir/zsh-autocomplete/zsh-autocomplete.plugin.zsh

# vim-like keybindings
bindkey -v

# options
setopt hist_ignore_all_dups
setopt hist_ignore_space
setopt inc_append_history
setopt auto_cd

# pacman aliases
alias pacupg="sudo pacman -Syu"
alias pacupd="sudo pacman -Sy"
alias pacin="sudo pacman -S"
alias pacre="sudo pacman -R"
alias pacrem="sudo pacman -Rns"
alias paclean="sudo pacman -Sc"

# yay aliases
alias yaupg="yay -Syu"
alias yaupd="yay -Sy"
alias yain="yay -S"
alias yare="yay -R"
alias yarem="yay -Rns"
alias yaclean="yay -Sc"

# misc aliases
alias l="exa --long --all --group-directories-first" # file listing
alias md="mkdir -p" # making directories
alias vim="nvim" # replace vim with nvim
alias dots="/usr/bin/git --git-dir=$HOME/dotfiles --work-tree=$HOME" # dotfile management

# starship prompt
eval "$(starship init zsh)"

# random pokemon on terminal open
krabby random -i
