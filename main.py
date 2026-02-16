from rich.table import Table
from rich.console import Console
import socket
import concurrent.futures

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            if s.connect_ex((host, port)) == 0:
                return port
    except:
        pass
    return None

console = Console(force_terminal=True, color_system="truecolor")

target = input("Enter your domain")

target = target.replace("https://", "").replace("http://", "").split("/")[0].strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror as e:
    console.print(f"[red] FAILED TARGET IP:[/red] {e}")
    exit()
common_ports = range(1,65536)
closed_ports = 0
failed_ports = []

table = Table(title="Port Scan", style = "bold green")
table.add_column("IP", style="red")
table.add_column("Status", style="blue")

console.print(f"[bold]Scanning {target} ({target_ip})...[/bold]\n")

open_ports = []
total_ports = len(common_ports)

with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
    futures = {executor.submit(scan_port, target_ip, port): port for port in common_ports}
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        if result:
            open_ports.append(result)

                    
for port in open_ports:
    table.add_row(str(port), "Open")

console.print(table)

closed_ports = total_ports - len(open_ports)

console.print(f"\nScanned: {total_ports}")
console.print(f"[green]Open:[/green] {len(open_ports)}")
console.print(f"[red]Closed/Filtered:[/red] {closed_ports}")
console.print("[green]Scan complete[/green]")
