# 在终端设置网络代理。
# 
# 这个必须 source 执行！
# 
# fix(2022-01-25): 以 source 运行，修复了 on/off 无效的问题

HTTPPROXY="http://127.0.0.1:1087"
SOCKPROXY="socks5://127.0.0.1:1080"

echo_help() {
	echo "Proxy takes the http proxy on/off in current env.

THIS SOFTWARE IS FOR CDFMLR's PERSONAL USE ONLY.

Usage:

	source proxy.sh <command> 

The commands are:

    on      takes proxy on
    off     takes proxy off
    do <c>  run a command <c> with proxy on, then take proxy off 

CDFMLR      May 8, 2020       CDFMLR
    "
}

proxy_on() {
	export http_proxy=${HTTPPROXY}
    export https_proxy=$http_proxy
    git config --global http.proxy ${HTTPPROXY} 
	git config --global https.proxy ${HTTPPROXY}
    echo "Proxy On: ${SOCKPROXY}"
}

proxy_off() {
    unset http_proxy
    unset https_proxy
    git config --global --unset http.proxy
	git config --global --unset https.proxy
    echo "Proxy off."
}


# 没参数会执行到下面的 case *)
#if [ $# -le 0 ]; then
#    echo_help
#	# exit 1
#fi

case $1 in 
    "on")
        proxy_on
        # exit 1
        ;;    # ;; 就是 break
    "off")
        proxy_off
        # exit 1
        ;;
    "do")
        shift
        proxy_on

        trap 'onInterrupt' INT
        function onInterrupt () {
            echo ' Interrupt'
        }

        echo "> $*"
        $*
        proxy_off
        # exit 1
        ;;
    *)
        echo_help
        # exit 1
        ;;
esac
