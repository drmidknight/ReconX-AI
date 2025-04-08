def generate_report(traditional, ai, comparison):
    with open('output/report.md', 'w') as f:
        f.write("# 🕵️ Reconnaissance Comparison Report\n\n")
        f.write("## 🔧 Traditional Recon Output\n")
        f.write(f"```\n{traditional}\n```\n\n")
        f.write("## 🤖 AI Parser Output\n")
        f.write(f"```\n{ai}\n```\n\n")
        f.write("## 🔍 Comparison Result\n")
        f.write(f"```\n{comparison}\n```\n")
