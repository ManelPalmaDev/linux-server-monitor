#!/usr/bin/env python3

import os
import shutil
import socket
import subprocess
import time

#Get Hostname Funciton
def get_hostname():
    return socket.gethostname()

#Get uptime function
def get_uptime():
    with open("/proc/uptime", "r") as file:
        uptime_seconds = float(file.readline().split()[0])

    days = int(uptime_seconds // 86400)
    hours = int((uptime_seconds % 86400) // 3600)
    minutes = int((uptime_seconds % 3600) // 60)

    return f"{days}d {hours}h {minutes}m"

#Get cpu usage function
def get_cpu_usage():
    with open("/proc/stat", "r") as file:
        cpu = file.readline().split()

    idle = int(cpu[4])
    total = sum(map(int, cpu[1:]))

    time.sleep(0.5)

    with open("/proc/stat", "r") as file:
        cpu = file.readline().split()

    idle_new = int(cpu[4])
    total_new = sum(map(int, cpu[1:]))

    idle_diff = idle_new - idle
    total_diff = total_new - total

    return (1 - idle_diff / total_diff) * 100

#Get memory usage function
def get_memory_usage():
    with open("/proc/meminfo", "r") as file:
        memory = file.readlines()

    total = int(next(line for line in memory if line.startswith("MemTotal")).split()[1])
    available = int(next(line for line in memory if line.startswith("MemAvailable")).split()[1])

    used = total - available

    return (used / total) * 100

#Get disk usage function
def get_disk_usage():
    usage = shutil.disk_usage("/")
    return (usage.used / usage.total) * 100

#Get SSH status function
def get_ssh_status():
    result = subprocess.run(
        ["systemctl", "is-active", "--quiet", "ssh"]
    )

    return result.returncode == 0

#Check network is UP/DOWN function
def check_network():
    result = subprocess.run(
        ["ping", "-c", "1", "-W", "2", "8.8.8.8"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0

#Screen output block
print("=== SERVER STATUS ===")
print()

print(f"Hostname: {get_hostname()}")
print(f"Uptime: {get_uptime()}")
print(f"CPU usage: {get_cpu_usage():.1f}%")
print(f"Memory usage: {get_memory_usage():.1f}%")
print(f"Disk usage: {get_disk_usage():.1f}%")

if get_ssh_status():
    print("SSH service: OK")
else:
    print("SSH service: NOT RUNNING")

if check_network():
    print("Network connectivity: OK")
else:
    print("Network connectivity: FAILED")
