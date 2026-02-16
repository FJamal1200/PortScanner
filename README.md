# PortScanner

A lightweight threaded TCP port scanner written in Python.
The tool resolves a hostname to an IP address and attempts TCP connections across the port range to identify reachable services.

Features

Accepts domain names or raw IP addresses

DNS resolution before scanning

Parallel scanning using ThreadPoolExecutor

Adjustable timeout for faster scans

Displays only open ports with a closed/filtered summary

Clean CLI output using Rich tables

Purpose

This project was built to understand how network services expose themselves over TCP and how connection attempts behave under different conditions such as timeouts, filtering, and rate limiting.
Rather than relying on existing scanners, the goal was to implement the connection logic manually to observe real network behavior and performance tradeoffs.

How it works

The scanner performs a TCP connect attempt on each port.
If the handshake succeeds, the port is reported as open.
Failures or timeouts are grouped as closed/filtered.
