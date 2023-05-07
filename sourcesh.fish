function sourcesh --description 'evaluate contents of file in (z)sh'
  exec zsh -c "source $argv; exec fish"
end

