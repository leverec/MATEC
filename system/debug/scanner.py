__ver__ = "0.2.2"
import os
import re
from pathlib import Path
from system.loader import Load

# ↓ color ↓
TEXT_GREEN = "\033[92m"
TEXT_YELLOW = "\033[93m"
TEXT_RED = "\033[31m"
BG_YELLOW = "\033[103;30m"
BG_RED = "\033[41m"
RESET = "\033[0m"

# finding the __ver__ on the very first line and on every python files
def parse_version(line):
    match = re.match(r'__ver__\s*=\s*["\'](.+?)["\']', line)
    # ex :__ver__ = "1.0.0" , output = 1.0.0
    return match.group(1) if match else None 

def is_valid_version(ver):
    return bool(re.match(r'^\d+\.\d+\.\d+$', ver))

def analyze_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            line = f.readline().strip()
            if line.startswith("__ver__"):
                version = parse_version(line)
                if version is None:
                    return "WX", "INVVS", None
                elif is_valid_version(version):
                    return "D1", line, version  # line = __ver__ = "[ver]", version = [ver]
                else:
                    return "WX", "INVVS", version # INVVS -> Invalid Version Format
            else:
                return "WX", "NOTVS", None # NOTVS -> Version Not Found
    except Exception as e:
        return "X0", str(e), None

def colorize(status, text):
    if status == "D1": # only D1 get colored
        return f"[{TEXT_GREEN}{status}{RESET}]{text}"
    elif status == "WX": # all text background get colored
        return f"{BG_YELLOW}{text}{RESET}"
    elif status == "X0": # same as above
        return f"{BG_RED}{text}{RESET}"
    return text

# scan: path = None (default): input = path/ or path
def scan(path=None, version_filter=None):
    # input["debug", "version", path, version_filter]
    ROOT = Path(__file__).resolve().parents[2]
    # ROOT = MATEC(in this case)
    if path is None:
        target = ROOT
    else:
        target = ROOT / path  # target = MATEC(.)/path
    
    config = Load()
    # ↓ header displayed output ↓
    print(f"— [{config.get("meta", "name")}] : {config.get("meta", "version")} $ {path} $ {version_filter}")
    print(f"scanner.version = {__ver__}\n")
    # — [MATEC / meta : (name) in config] : (meta : (version) in config) $ ["{path}" | None]
    stats = {"D1": 0, "WX": 0, "X0": 0}
    results = []
    # results = status(D1,WX,X0), path, info: __ver__ = {version}, version: {version}
    max_len = 0
    for root_dir, _, files in os.walk(target):
        for file in files:
            if file.endswith(".py"): # detect only python files
                full = Path(root_dir) / file
                status, info, version = analyze_file(full)
                # case version got filtered
                if version_filter and version != version_filter:
                    continue
                # status = D1 | WX | X0
                stats[status] += 1
                try:
                    rel = full.resolve().relative_to(ROOT)
                    display = f"./{rel}"
                except Exception:
                    display = str(full)
                results.append((status, display, info, version))
                if len(display) > max_len:
                    max_len = len(display)
                    # max_len = display_text_len
    # ↓ displayed output ↓
    for status, display, info, version in results:
        padded = display.ljust(max_len)
        # example:
        # Display1        :
        # Displ2          :
        # Example_Display :
        if status == "D1":
            output = f" {padded} : {version}"
        else:
            output = f"[{status}] {padded} : {info}"
        print(colorize(status, output))
        # [status] [text] : [version]
    print(f"[ {TEXT_GREEN}{stats['D1']}{RESET} | {TEXT_YELLOW}{stats['WX']}{RESET} | {TEXT_RED}{stats['X0']}{RESET} ]")
    # ↑ stats ↑