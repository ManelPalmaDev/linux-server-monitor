# Linux Server Monitor

A small Bash script for checking basic Linux server status and system resources.

## Objective

The objective of this lab is to create simple monitoring scripts capable of displaying basic information about the current Linux system.

The same monitoring functionality was implemented using both Bash and Python.

## Environment

- OS: Ubuntu Server 26.04

- Shell: Bash 5.3.9

- Python: 3.14.4

- Hostname: UbuntuServerMP

## Features

The script checks:

- Hostname

- System uptime

- CPU usage

- Memory usage

- Disk usage

- [SERVICE STATUS]

- Network connectivity

## Implementations

- monitor.sh — Bash implementation using Linux command-line utilities.
- monitor.py — Python implementation providing the same monitoring functionality.

## Usage

### Bash

- chmod +x monitor.sh
- ./monitor.sh

### Python
- chmod +x monitor.py
- ./monitor.py

Alternatively:

- python3 monitor.py

## Example output

=== SERVER STATUS ===

- Hostname: [HOSTNAME]
- Uptime: [UPTIME]

- CPU usage: [XX]%
- Memory usage: [XX]%
- Disk usage: [XX]%

- [SERVICE]: OK
- Network connectivity: OK

## Files

- monitor.sh — Bash monitoring script.
- monitor.py - Python implementation of the monitoring script.

## Results

The script successfully retrieves and displays basic system information and provides a quick overview of the server status.

## Screenshots

- Bash script execution and output

- Pyhton script exectuion and output

## What I learned

- Bash scripting fundamentals

- Python scripting for system administration

- Retrieving system information from Linux

- Using Linux command-line utilities

- Working with system services and network connectivity

- Combining commands into a simple administration script


