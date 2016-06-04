#!/bin/sh
cd /demo

case $1 in
	put)
		./dsp.py
		;;
	get)
		./dsg.py
		;;
	sh|bash|shell)
		/bin/sh
		;;
	*)
		echo "Usage: $0 <put|get>"
		;;
esac
