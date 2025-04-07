from traditional_recon import run_nmap, run_whois
from ai_recon_parser import parse_with_ai
from comparator import compare_outputs
from report_generator import generate_report

target = "facebook.com"

# Step 1: Run Traditional Recon
run_nmap(target)
whois_data = run_whois(target)

# Combine raw output
with open('data/nmap.xml', 'r') as f:
    nmap_data = f.read()

raw_traditional = nmap_data + "\n\n" + str(whois_data)

# Step 2: Run AI Parser
ai_output = parse_with_ai(raw_traditional)

# Step 3: Compare
comparison = compare_outputs(raw_traditional, ai_output)

# Step 4: Generate Report
generate_report(raw_traditional, ai_output, comparison)
print("✅ Report generated at: output/report.md")
