import difflib


def compare_outputs(traditional_data, ai_data):
    diff = difflib.unified_diff(
        traditional_data.splitlines(),
        ai_data.splitlines(),
        fromfile='Traditional Recon',
        tofile='AI Recon'
    )
    return '\n'.join(diff)
