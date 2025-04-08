import subprocess
import nmap
import os


def run_nmap(target):
    print(f"📡 Running Nmap scan on {target}...")
    os.makedirs("data", exist_ok=True)

    output_path = "data/nmap.xml"
    command = f"nmap -T4 -p 1-1000 -sV -oX {output_path} {target}"

    try:
        subprocess.run(command.split(), check=True)
        print(f"✅ Nmap scan complete. Output saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Nmap scan failed: {e}")
