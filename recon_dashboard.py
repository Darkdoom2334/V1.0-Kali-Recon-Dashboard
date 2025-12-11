#!/usr/bin/env python3
import nmap
from rich.console import Console
from rich.table import Table

scanner = nmap.PortScanner()
console = Console()

target_subnet = "123.123.123.123" # <---- Replace with your Subnet

console.print(f"[bold cyan]Scanning {target_subnet}...[/bold cyan]")
scanner.scan(hosts=target_subnet, arguments='-n -T4 -F')

table = Table(title="Darkdoom2334 Recon Dashboard")

table.add_column("IP", style="cyan", no_wrap=True)
table.add_column("Hostname", style="magenta")
table.add_column("Open Ports", style="green")
table.add_column("Risk Level", style="bold")
table.add_column("OS Guess", style="yellow")

def assess_risk(ports):
    high_risk = {'21', '23', '445', '139', '3389'}
    medium_risk = {'80', '443', '22'}
    score = 0
    for port in ports:
        if port in high_risk:
            score += 3
        elif port in medium_risk:
            score += 1
    if score >= 5:
        return "High", "bold red"
    elif score >= 2:
        return "Medium","bold yellow"
    else:
        return "Low", "bold green"

for host in scanner.all_hosts():
    ip = host
    hostname = scanner[host].hostname()
    ports = []
    for proto in scanner[host].all_protocols():
        lport = scanner[host][proto].keys()
        for port in sorted(lport):
            ports.append(str(port))
    risk_level, style = assess_risk(ports)
    os_guess = "Unknown"
    if 'osmatch' in scanner[host] and scanner[host]['osmatch']:
        os_guess = scanner[host]['osmatch'][0]['name']
    table.add_row(ip, hostname or "-", ", ".join(ports), f"[{style}]{risk_level}[/{style}]", os_guess)

console.print(table)

#Made by Darkdoom2334
