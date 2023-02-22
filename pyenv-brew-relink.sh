#!/bin/bash

show_usage() {
    echo "Usage: $0 [OPTION]"
    echo "Relink Python versions installed via Homebrew to Pyenv."
    echo ""
    echo "Options:"
    echo "  -h, --help       Display this help and exit."
}

pyenv_brew_relink() {
    rm -f "$HOME/.pyenv/versions/*-brew"
    for i in $(brew --cellar)/python* ; do
      for p in $i/*; do
        echo $p
        ln -s -f $p $HOME/.pyenv/versions/${p##/*/}-brew
      done  
    done
    pyenv rehash
}

case "$1" in
    -h|--help)
        show_usage
        ;;
    *)
        pyenv_brew_relink
        ;;
esac

