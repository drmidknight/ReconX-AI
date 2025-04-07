import subprocess
import json


def run_nmap(target):
    result = subprocess.run(
        ['nmap', '-sV', '-oX', 'data/nmap.xml', target], capture_output=True)
    return result.returncode == 0


def run_whois(target):
    import whois
    return whois.whois(target)


def run_theHarvester(target):
    result = subprocess.run(
        ['theHarvester', '-d', target, '-b', 'all', '-f', 'data/harvested.html'])
    return result.returncode == 0
