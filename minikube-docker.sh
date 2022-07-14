# 开关没有 k8s 的 minikube 环境，并自动配置好 docker-env
#
# 这个脚本必须用 source 运行！
# 推荐在 ~/.zshrc 中配置: 
#     alias minidocker="source ~/minikube-docker.sh"

MPNAME="no-k8s-docker"

usage() {
	echo "My minikube-docker start/stop helper (PERSONAL USE ONLY)

Usage: 

	source minikube-docker.sh <start|stop|shell>

This script helps to start/stop a docker demon by running:
    minikube start|stop -p ${MPNAME}
And set the docker-env:
    eval \$(minikube -p ${MPNAME} docker-env)

MAKE SURE TO run this script with a . (source)

CDFMLR                  Jan 25, 2022                  CDFMLR
"
}

start() {
	minikube start -p ${MPNAME} --image-mirror-country='cn' --no-kubernetes
	eval $(minikube -p ${MPNAME} docker-env)
}

stop() {
	minikube stop -p ${MPNAME}
}

shell() {
	eval $(minikube -p ${MPNAME} docker-env)
}

# if [ $# -le 0 ]; then
#     usage
# fi

case $1 in
	"start")
		start
		;;
	"stop")
		stop
		;;
	"shell")
		shell
		;;
	*)
		usage
		;;
esac

