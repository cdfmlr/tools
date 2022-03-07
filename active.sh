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
