# source {this_file} in ~/.config/fish/config.fish

set TOOLSDIR "$HOME/tools"

source $TOOLSDIR/sourcesh.fish

# proxy
alias proxy="sourcesh $TOOLSDIR/proxy.sh"

# deprecated
# minikube docker
#alias minidocker="source $TOOLSDIR/minikube-docker.sh"

# make-gitignore
alias makegitignore="python3 $TOOLSDIR/make-gitignore.py"

# f2utf8
alias f2utf8="python3 $TOOLSDIR/f2utf8.py"

# km2t
alias km2t="python3 $TOOLSDIR/others/km2t.py"

# ignore_folders_in_spotlight
alias ignore_folders_in_spotlight="sudo $TOOLSDIR/ignore_folders_in_spotlight.py"

# httpserve (python)
alias httpserve="python3 $TOOLSDIR/simple-cors-http-server.py"

# httpstatic (go)
alias httpstatic="$TOOLSDIR/httpstatic/bin/httpstatic"

# emsend
alias emsend="python3 $TOOLSDIR/myemail_sender.py"

# kill 输入法
alias killscim="sh $TOOLSDIR/kill-scim.sh"

