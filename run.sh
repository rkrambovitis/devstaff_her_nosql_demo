#!/bin/sh
cd /demo

case $1 in
	put)
		./dsp.py
		;;
	get)
		./dsg.py
		;;
	*)
		echo "Usage: $0 <put|get>"
		;;
esac
