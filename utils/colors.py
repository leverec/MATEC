__ver__ = "0.3.0"

def colors():
    return {
        "TEXT_GREEN" : "\033[92m",
        "TEXT_YELLOW" : "\033[93m",
        "TEXT_RED" : "\033[31m",
        "TEXT_CYAN" : "\033[36m",
        "TEXT_PURPLE" : "\033[35m",
        "BG_YELLOW" : "\033[103;30m",
        "BG_RED" : "\033[41m",
        "RESET" : "\033[0m"
    }
color = colors()

def colorize(colors: str, text: str):
    return color[colors] + text + color["RESET"]

def colorize_feedback_type1(status, text):
    if status == "D1":
        return f"[{color['TEXT_GREEN']}{status}{color['RESET']}]{text}"
    elif status == "WX":
        return f"{color['BG_YELLOW']}[{status}]{text}{color['RESET']}"
    elif status == "X0":
        return f"{color['BG_RED']}[{status}]{text}{color['RESET']}"
    return text

def colorize_feedback_type2(status, text):
    if status == "D1":
        return f"[{color['TEXT_GREEN']}{status}{color['RESET']}] {text}"
    elif status == "WX":
        return f"[{color['TEXT_YELLOW']}{status}{color['RESET']}] {text}"
    elif status == "NF":
        return f"[{color['TEXT_CYAN']}{status}{color['RESET']}] {text}"
    elif status == "X0":
        return f"[{color['TEXT_RED']}{status}{color['RESET']}] {text}"
    return text