__ver__ = "0.2.0"
import os
import re
from pathlib import Path
from system.loader import Load

# btw i use AI, obviously

# ↓ color ↓
TEXT_GREEN = "\033[92m"
TEXT_YELLOW = "\033[93m"
TEXT_RED = "\033[31m"
BG_YELLOW = "\033[103;30m"
BG_RED = "\033[41m"
RESET = "\033[0m"

def colorize(status, text):
    if status == "D1": # only D1 get colored
        return f"[{TEXT_GREEN}{status}{RESET}]{text}"
    elif status == "WX": # all text background get colored
        return f"{BG_YELLOW}{text}{RESET}"
    elif status == "X0": # same as above
        return f"{BG_RED}{text}{RESET}"
    return text

def sync():
    # .parent.parent.parent ahh 🥀
    root_dir = Path(__file__).resolve().parents[2]
    
    config = Load()
    project_version = config.get("meta", "version")  # version -> ex: 1.2.3
    
    # split it so only the first 2 that actually count
    parts = project_version.split(".")
    major, minor = parts[0], parts[1]
    
    # ↓ header displayed output ↓
    print(f"--sync commands : {project_version} — {config.get('meta', 'name')}--")
    print(f"update.version into {major}.{minor}.x\n")
    
    results = []
    stats = {"D1": 0, "WX": 0, "X0": 0}
    max_len = 0
    
    # results = [(status, display, info)]
    for root, _, files in os.walk(root_dir):
        # searching for a file that doesn't exi- oh i mean...
        # ends with .py
        for file in files:
            if not file.endswith(".py"):
                continue # skip
            
            full_path = Path(root) / file
            status = "X0"
            info = ""
            
            try:
                # idk, im just copying from AI (kinda)
                rel_path = f"./{full_path.relative_to(root_dir)}"
                
                with open(full_path, "r", encoding="utf-8") as f:
                    lines = f.readlines() # and it's trying to read the files
                
                if not lines:
                    status = "X0"  # and if the files empty
                    info = "NOTFL"
                else:
                    # the first line yk
                    first_line = lines[0].strip()
                    match = re.match(r'__ver__\s*=\s*"(\d+)\.(\d+)\.(\d+)"', first_line)
                    # regex that search a specific characters yk
                    # match __ver__ = "x.y.z"
                    
                    if match:
                        # and yk, only kept the last one, which is the internal version update
                        _, _, patch = match.groups()
                        target_ver = f"{major}.{minor}.{patch}"
                        new_line = f'__ver__ = "{target_ver}"\n' # new
                        
                        lines[0] = new_line # overwrite the first line
                        with open(full_path, "w", encoding="utf-8") as f:
                            f.writelines(lines) # spam W chat
                        
                        status = "D1"
                        info = target_ver
                    else:
                        status = "WX"
                        info = "NOTVS"
            except Exception as e:
                status = "X0"
                info = str(e)
                rel_path = str(full_path)
                
            results.append((status, rel_path, info))
            stats[status] += 1
            if len(rel_path) > max_len:
                max_len = len(rel_path)
    
    # ↓ Displayed Output ↓
    for status, display, info in results:
        padded = display.ljust(max_len)
        
        if status == "D1":
            output = f" {padded} : {info}"
        else:
            output = f"[{status}] {padded} : {info}"
        
        print(colorize(status, output))
    
    # ↑ stats ↑
    print(f"[ {TEXT_GREEN}{stats['D1']}{RESET} | {TEXT_YELLOW}{stats['WX']}{RESET} | {TEXT_RED}{stats['X0']}{RESET} ]")