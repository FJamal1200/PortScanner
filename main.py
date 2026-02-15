from rich.table import Table
from rich.console import Console
from rich.live import Live
import socket

console = Console()

target = input("Enter your domain")

target = target.replace("https://", "").replace("http://", "").split("/")[0].strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror as e:
    console.print(f"[red] FAILED TARGET IP:[/red] {e}")
    exit()
common_ports = [21,22,23,25,53,80,110,143,443,445,3389]
closed_ports = 0
failed_ports = []

table = Table(title="Port Scan", style = "bold green")
table.add_column("IP", style="red")
table.add_column("Status", style="blue")

with Live(table, console=console, refresh_per_second=4):
    for port in common_ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    table.add_row(str(port), "Open")

                else:
                    table.add_row(str(port), "[yellow]CLosed/Filtered[/yellow]")
                    closed_ports += 1

        except Exception as e:
            failed_ports.append(port)
            console.print(f"[red] FAILED PORT(S): {port}{type(e).__name__}[/red] ")

if failed_ports !=[]:
    console.print(f"[red] FAILED PORT(S): {failed_ports} ")

console.print(f"[red] Closed/Filtered PORT(S): {closed_ports} ")
console.print("[green] SCAN NOW COMPLETE [/green]")
