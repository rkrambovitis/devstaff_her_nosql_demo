#!/bin/sh
cd /demo

case $1 in
	put)
		./dsp.py $2 $3
		;;
	get)
		./dsg.py $2
		;;
	sh|bash|shell)
		/bin/sh
		;;
	*)
		echo "Usage: $0 <put|get>"
		;;
esac
