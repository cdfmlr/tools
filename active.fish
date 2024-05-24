# source {this_file} in ~/.config/fish/config.fish

set TOOLSDIR "$HOME/tools"
set PYTHON "/usr/bin/python3"

source $TOOLSDIR/sourcesh.fish

source $TOOLSDIR/private/active.fish

fish_add_path $TOOLSDIR/bin

# deprecated
# minikube docker
#alias minidocker="source $TOOLSDIR/minikube-docker.sh"

# make-gitignore
alias makegitignore="$PYTHON $TOOLSDIR/make-gitignore.py"

# f2utf8
alias f2utf8="$PYTHON $TOOLSDIR/f2utf8.py"

# km2t
alias km2t="$PYTHON $TOOLSDIR/others/km2t.py"

# ignore_folders_in_spotlight
alias ignore_folders_in_spotlight="sudo $TOOLSDIR/ignore_folders_in_spotlight.py"

# httpserve (python)
alias httpserve="$PYTHON $TOOLSDIR/simple-cors-http-server.py"

# httpstatic (go)
alias httpstatic="$TOOLSDIR/httpstatic/bin/httpstatic"

# emsend
alias emsend="$PYTHON $TOOLSDIR/myemail_sender.py"

# kill 输入法
alias killscim="sh $TOOLSDIR/kill-scim.sh"

# portnum 每日端口号
alias portnum="$PYTHON $TOOLSDIR/portnum.py"
 
