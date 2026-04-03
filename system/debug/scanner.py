__ver__ = "0.1.0"
import os
import re
from pathlib import Path
from system.loader import Load

# ===== COLOR =====
TEXT_GREEN = "\033[92m"
TEXT_YELLOW = "\033[93m"
TEXT_RED = "\033[31m"
BG_YELLOW = "\033[103;30m"
BG_RED = "\033[41m"
RESET = "\033[0m"

# ===== PARSE VERSION =====
def parse_version(line):
    match = re.match(r'__ver__\s*=\s*["\'](.+?)["\']', line)
    return match.group(1) if match else None

# ===== ANALYZE FILE =====
def analyze_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            line = f.readline().strip()

            if line.startswith("__ver__"):
                version = parse_version(line)
                if version:
                    return "D1", line, version
                else:
                    return "WX", "INVVS", None
            else:
                return "WX", "NOTVS", None

    except Exception as e:
        return "X0", str(e), None

# ===== COLORIZE OUTPUT =====
def colorize(status, text):
    if status == "D1":
        return f"[{TEXT_GREEN}{status}{RESET}]{text}"
    elif status == "WX":
        return f"{BG_YELLOW}{text}{RESET}"
    elif status == "X0":
        return f"{BG_RED}{text}{RESET}"
    return text

# ===== MAIN SCAN FUNCTION =====
def scan(path=None, recursive=True, version_filter=None):
    # ROOT project (MATEC)
    ROOT = Path(__file__).resolve().parent.parent.parent

    if path is None:
        target = ROOT
    else:
        target = ROOT / path[0]  # target relative ke MATEC
    
    config = Load()
    print(f"— [{config.get("meta", "name")}] : {config.get("meta", "version")} $ {path}")
    print(f"scanner.version = {__ver__}")
    print()

    stats = {"D1": 0, "WX": 0, "X0": 0}
    results = []
    max_len = 0

    # ===== WALK FILES =====
    for root_dir, _, files in os.walk(target):
        for file in files:
            if file.endswith(".py"):
                full = Path(root_dir) / file
                status, info, version = analyze_file(full)

                if version_filter and version != version_filter:
                    continue
                
                stats[status] += 1

                try:
                    rel = full.resolve().relative_to(ROOT)
                    display = f"./{rel}"
                except Exception:
                    display = str(full)

                results.append((status, display, info, version))
                if len(display) > max_len:
                    max_len = len(display)

    # ===== PRINT ALIGNED OUTPUT =====
    for status, display, info, version in results:
        padded = display.ljust(max_len)
        if status == "D1":
            output = f" {padded} : {version}"
        else:
            output = f"[{status}] {padded} : {info}"
        print(colorize(status, output))

    # ===== SUMMARY =====
    print(f"[ {TEXT_GREEN}{stats['D1']}{RESET} | {TEXT_YELLOW}{stats['WX']}{RESET} | {TEXT_RED}{stats['X0']}{RESET} ]")

# ===== FOR DIRECT RUN =====
if __name__ == "__main__":
    scan()  # default scan ./ dari MATEC