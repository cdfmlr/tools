# source {this_file} in ~/.zshrc

THIS_DIR="~/tools"

# proxy
# SH 小知识: source 就不 fork 执行，
#            否则脚本是 fork 执行的，在新 proc 里 export 白费了
alias proxy="source ${THIS_DIR}/proxy.sh"

# minikube docker
alias minidocker="source ${THIS_DIR}/minikube-docker.sh"

# make-gitignore
alias makegitignore="python3 ${THIS_DIR}/make-gitignore.py"

# f2utf8
alias f2utf8="python3 ${THIS_DIR}/f2utf8.py"

# km2t
alias km2t="python3 ${THIS_DIR}/others/km2t.py"

# ignore_folders_in_spotlight
alias ignore_folders_in_spotlight="sudo ${THIS_DIR}/ignore_folders_in_spotlight.py"

# httpserve (python)
alias httpserve="python3 ${THIS_DIR}/simple-cors-http-server.py"

# httpstatic (go)
alias httpstatic="${THIS_DIR}/httpstatic/bin/httpstatic"

# emsend
alias emsend="python3 ${THIS_DIR}/myemail_sender.py"

# kill 输入法
alias killscim="sh ${THIS_DIR}/kill-scim.sh"

# pyenv-brew-relink
alias pyenv-brew-relink="sh ${THIS_DIR}/pyenv-brew-relink.sh"

# portnum 每日端口号
alias portnum="python3 ${THIS_DIR}/portnum.py"
