#!/bin/zsh

if [ "$#" -lt 1 ]; then
    echo "z2fish: zsh -> fish with no args."
    zsh -lic "exec fish"
else
    echo "z2fish: zsh -> fish with $# args:" "$@"

    zsh -lic zsh -t << EOF
fish "$@"
EOF

fi

