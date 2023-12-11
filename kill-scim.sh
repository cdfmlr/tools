#!/bin/sh

usage() {
    echo "Usage: $0 [-q|--quiet] [-y|--yes] [-h|--help] [max_threads]"
	echo ""
    echo "Check the number of threads used by the SCIM input method and kill it if it exceeds the specified maximum number of threads."
	echo ""
	echo "目测 macOS 13.0.1 (22A400) 输入法线程数超过一定数量（感觉是 64 个）就会卡住整个系统（跨应用的彩虹圈）。"
	echo "这个程序检查输入法线程数，大于 max_threads 时可以一键杀死输入法，避免卡顿问题。"
	echo ""
	echo "Update: 目测 Sonoma (截止 14.1.2 23B92) 仍然存在这个问题。"
	echo ""
	echo "实际上用一行命令就可以完成这个："
	echo '  scim_pid=$(ps aux | grep "SCIM.app" | grep "zh-Hans-CN" | cut -f 2 -w) && ps -M $scim_pid | wc -l |xargs test 64 -lt && kill -9 $scim_pid'
	echo "但这个脚本可读性和鲁班性更好一点。"
    echo ""
    echo "  -q, --quiet   suppress output"
    echo "  -y, --yes     automatically confirm to kill SCIM without prompting"
	echo "  -h, --help    show this help message and exit"
    echo "  max_threads   the maximum number of threads allowed for SCIM (default: 64)"
}

max_threads=64

# Check for options & arguments
while [[ $# -gt 0 ]]
do
    case "$1" in
        -q|--quiet)
            quiet=true
            ;;
        -y|--yes)
            yes=true
            ;;
		-yq|-qy)
			yes=true
			quiet=true
			;;
		-h|--help)
			usage
			exit 0
			;;
		*)
			max_threads=$1
    esac
	shift
done

# --quiet 则不要哔哔赖赖，干就完了
quiet_echo() {
	test -z "$quiet" && echo "$1" >&2
}

# test -z "$quiet" && usage

pid=$(ps aux | grep "SCIM.app" | grep "zh-Hans-CN" | cut -f 2 -w)
quiet_echo "输入法（SCIM）进程: pid=$pid"

if [ -z "$pid" ]; then
	quiet_echo "输入法没有在运行。"
	exit 1
fi

threads=$(ps -M $pid | wc -l)  # 虚大了 1: ps 的 header，再套一个 tail 可以解决但没必要
quiet_echo "输入法进程数: threads=$threads, expected max=$max_threads"

if [ $threads -lt $max_threads ]; then
	quiet_echo "Normal. Do nothing."
	exit 1
fi

# 可以 sh kill-scim.sh -y 来跳过确认
if [ ! -z "$yes" ]; then
	response="y"
else
	read -r -p "Too many SCIM! kill -9 $pid? [y/N] " response
fi
case "$response" in
	[yY][eE][sS]|[yY]) 
		kill -9 $pid		
		quiet_echo "Killed SCIM ($pid)."
		exit 0
		;;
	*)
		quiet_echo "Abort."
		exit 2
		;;
esac

