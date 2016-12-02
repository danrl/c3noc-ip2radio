#!/bin/sh

trap exit SIGHUP SIGINT SIGTERM

while true
do
  python ip2radio.py
  sleep 5
done
