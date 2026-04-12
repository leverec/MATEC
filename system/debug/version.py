__ver__ = "0.3.0"
from utils.colors import colorize_feedback_type1, colors
from system.loader import Load
from pathlib import Path
import os
import re

color = colors()
EXCLUDE_DIRS = {".git", "__pycache__", ".ignore", ".upcoming"}

def match_version(first_line):
    match = re.match(r'^__ver__\s*=\s*"(\d+\.\d+\.\d+)"', first_line.strip())
    return match.group(1) if match else None

def atomic_write(path, lines):
    temp_path = f"{path}.tmp"
    try:
        with open(temp_path, "w", encoding="utf-8") as f:
            f.writelines(lines)
        os.replace(temp_path, path)
    except Exception as e:
        if os.path.exists(temp_path):
            os.remove(temp_path)
        raise e

def version_debug(path_filter=None, version_filter=None, mode="scan"):
    ROOT = Path(__file__).resolve().parents[2]
    target = ROOT if path_filter is None else ROOT / path_filter
    
    config = Load()
    project_version = config.get("meta", "version")
    major, minor = project_version.split(".")[:2]
    
    if mode == "scan":
        print(f"— [{config.get('meta', 'name')}] : {project_version} > {path_filter} > {version_filter}")
        print(f"scanner.version = {__ver__}\n")
    else:
        print(f"--sync VERSION commands : {project_version} — {config.get('meta', 'name')}--")
        print(f"update.version.file from {__ver__[0]}.{__ver__[2]}.x to {major}.{minor}.x\n")
        
    stats = {"D1": 0, "WX": 0, "X0": 0}
    results = []
    max_len = 0
    
    for root_dir, dirs, files in os.walk(target):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if not file.endswith(".py"):
                continue
                
            full_path = Path(root_dir) / file
            try:
                rel_path = f"./{full_path.relative_to(ROOT)}"
            except:
                rel_path = str(full_path)
                
            status, info = "X0", "ERROR"
            
            try:
                if mode == "scan":
                    with open(full_path, "r", encoding="utf-8") as f:
                        first_line = f.readline()
                    
                    version_in_file = match_version(first_line)
                    
                    if version_in_file:
                        f_parts = version_in_file.split(".")
                        target_version = f"{major}.{minor}.{f_parts[2]}" 
                        
                        if version_in_file == target_version:
                            status, info = "D1", version_in_file
                        else:
                            status, info = "WX", version_in_file 
                    else:
                        status, info = "WX", "INVVS"
                        
                    if version_filter and version_in_file != version_filter:
                        continue
                        
                else:
                    with open(full_path, "r", encoding="utf-8") as f:
                        lines = f.readlines()
                        
                    if not lines:
                        status, info = "X0", "NOTFL" # File is empty or doesnt exist
                    else:
                        target_version_str = match_version(lines[0])
                        
                        if target_version_str:
                            f_patch = target_version_str.split(".")[2]
                            final_sync_version = f"{major}.{minor}.{f_patch}"
                            
                            if target_version_str == final_sync_version:
                                status, info = "D1", target_version_str
                            else:
                                lines[0] = f'__ver__ = "{final_sync_version}"\n'
                                atomic_write(str(full_path), lines)
                                status, info = "D1", f"{final_sync_version} (UPDATED)"
                        else:
                            status, info = "WX", "INVVS"
                            
            except Exception as e:
                status, info = "X0", str(e)
                
            results.append((status, rel_path, info))
            stats[status] += 1
            max_len = max(max_len, len(rel_path))
            
    output_buffer = []
    for status, display, info in results:
        padded = display.ljust(max_len)
        line = f" {padded} : {info}"
        output_buffer.append(colorize_feedback_type1(status, line))
        
    print("\n".join(output_buffer))
    print(f"\n[ {color['TEXT_GREEN']}{stats['D1']}{color['RESET']} | {color['TEXT_YELLOW']}{stats['WX']}{color['RESET']} | {color['TEXT_RED']}{stats['X0']}{color['RESET']} ]")
