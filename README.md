# PortScanner

A lightweight threaded TCP port scanner written in Python.
The tool resolves a hostname to an IP address and attempts TCP connections across the port range to identify reachable services.

# Features

- Accepts domain names or raw IP addresses

- DNS resolution before scanning

- Parallel scanning using ThreadPoolExecutor (300 concurrent connections)

- Timeout-controlled connection attempts for faster scans

- Displays only open ports with a closed/filtered summary

- Clean CLI output using Rich tables

# Purpose

This project was built to better understand how network services expose themselves over TCP and how connectivity checks behave in real environments.
Instead of relying on existing scanners, the connection logic was implemented manually to observe timeouts, filtering, and performance tradeoffs when scanning large port ranges.

# How it works

The scanner performs a TCP connect attempt on each port (1–65535).
If the TCP handshake succeeds, the port is reported as open.
Failures and timeouts are grouped as closed/filtered.

Because many hosts rate-limit aggressive scans, results may vary depending on firewall behavior and network conditions.
