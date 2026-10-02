#!/bin/bash

echo "=== SERVER STATUS ==="
echo

#Hostname 
echo "Hostname: $(hostname)"
#Uptime
echo "Uptime: $(uptime -p)"
#Cpu usage
echo "CPU usage: $(top -bn1 | grep "Cpu(s)" | awk '{print 100 - $8}')%"
#Memory usage
echo "Memory usage: $(free | awk '/Mem:/ {printf  int($3/$2 * 100)}')%"
#Disk usage 
echo "Disk usage: $(df -h / | awk 'NR==2 {print $5}')"

#SSH status check
if systemctl is-active --quiet ssh; then
	echo "SSH service: OK"
else
	echo "SSH service: NOT RUNNING"
fi

#Netowrk state check
if ping -c 1 -W 2 8.8.8.8 > /dev/null 2>&1; then
	echo "Network connectivity : OK"
else
	echo "Network connectivity: FAILED"
fi
