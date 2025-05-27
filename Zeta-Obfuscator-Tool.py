import marshal
import random
import string
import sys
import os
import datetime
import colorama
import sys
import ctypes
import tkinter as tk
from tkinter import filedialog
import shutil
import time
import sys
from colorama import init

init(autoreset=True)

name = "".join(random.choices(string.ascii_letters, k=10))

color = colorama.Fore
red = color.RED
white = color.WHITE
green = color.GREEN
reset = color.RESET
BEFORE = f"{red}[{white}"
AFTER = f"{red}]"
INPUT = f"{BEFORE}>{AFTER} |"
INFO = f"{BEFORE}!{AFTER} |"
ERROR = f"{BEFORE}x{AFTER} |"
ADD = f"{BEFORE}+{AFTER} |"
WAIT = f"{BEFORE}~{AFTER} |"
discord_server = "discord.gg/Benzox"
github = "github.com/BenzoXdev"
telegram = "t.me/Benzox"
instagram = "instagram.com/just._.benzo"
by = "BenzoXdev"
modified_by = "Melphination"
folder = "Zeta-Obfuscator"
output_folder_1 = folder + "/Script-Obfuscate"
script_folder = folder + "/Script"
txt_file = folder + "/README.txt"


def current_time_hour():
    return datetime.datetime.now().strftime("%H:%M:%S")


def Title(title):
    if sys.platform.startswith("win"):
        ctypes.windll.kernel32.SetConsoleTitleW(
            f"Zeta-Obfuscator - Obfuscator Tool | {title}"
        )
    else:
        if sys.platform.startswith("linux"):
            sys.stdout.write(f"\033]2;Zeta-Obfuscator - Obfuscator Tool | {title}\a")


def ChoosePythonFile():
    try:
        print(
            f"{BEFORE + current_time_hour() + AFTER} {INPUT} Chose a python file -> {reset}"
        )
        root = tk.Tk()
        root.withdraw()
        root.attributes("-topmost", True)
        python_file = filedialog.askopenfilename(
            parent=root,
            title="Zeta-Obfuscator - Obfuscator Tool | Chose a python file (.py)",
            filetypes=[("PYTHON files", "*.py")],
        )
    except:
        python_file = input(
            f"{BEFORE + current_time_hour() + AFTER} {INPUT} Chose a python file -> {reset}"
        )
    else:
        return python_file


def random_var(used_vars, number=10):
    while True:
        rdm_var = "".join(random.choices(string.ascii_letters, k=number))
        if rdm_var not in used_vars:
            used_vars.add(rdm_var)
            return rdm_var


def layer_2(script, size_1, size_2):
    used_vars = set()
    for i in range(random.randint(size_1, size_2)):
        var_1 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_2 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_3 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_4 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_5 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_6 = random_var(used_vars, number=random.randint(size_1, size_2))
        script = (
            script
            + f"\nclass {var_1}:\n def {var_2}({var_3}):\n  {var_4} = {var_3}\n  {var_5} = {var_4}\n  return {var_5}\n {var_3} = '{var_6}'\n {var_5} = {var_2}({var_3})\n{var_1}()\n"
        )
    for i in range(random.randint(size_1, size_2)):
        var_1 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_2 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_3 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_4 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_5 = random_var(used_vars, number=random.randint(size_1, size_2))
        var_6 = random_var(used_vars, number=random.randint(size_1, size_2))
        script = (
            f"\nclass {var_1}:\n def {var_2}({var_3}):\n  {var_4} = {var_3}\n  {var_5} = {var_4}\n  return {var_5}\n {var_3} = '{var_6}'\n {var_5} = {var_2}({var_3})\n{var_1}()\n"
            + script
        )
    return script


def layer_3(script):
    used_vars = set()
    key = random.randint(1, 10)
    var_1 = random_var(used_vars)
    var_2 = random_var(used_vars)
    var_3 = random_var(used_vars)
    obfuscated_script = "".join((chr(ord(c) + key) for c in script))
    script = f"{var_1} = {repr(obfuscated_script)}\n{var_3} = {key}\n{var_2} = ''.join(chr(ord(c) - {var_3}) for c in {var_1})\nexec({var_2})"
    return script


def layer_4(script):
    compiled_code = marshal.dumps(compile(script, "<string>", "exec"))
    script = f"_{name}_ = {repr(compiled_code)}\nexec(_{name}.loads(_{name}_))"
    return script


def layer_5(script):
    chunks = [script[i : i + 1000] for i in range(0, len(script), 1000)]
    used_vars = set()
    vars = {random_var(used_vars): repr(chunk) for chunk in chunks}
    code_vars = "\n    ".join((f"{k} = {v}" for k, v in vars.items()))
    script = f"\nclass {name}:\n    {code_vars}\n\nimport marshal as _{name}\nexec(''.join([{name}.{f', {name}.'.join(vars.keys())}]))"
    return script


def obfuscate(script, size_1, size_2):
    script = layer_2(script, size_1, size_2)
    script = layer_3(script)
    script = layer_4(script)
    script = layer_5(script)
    return script


def Zeta_Obfuscator():
    Title(f"By: {by}, Modified by: {modified_by}")
    print(f"""{red}                                                                                                  

                                            ▒███████▒▓█████▄▄▄█████▓ ▄▄▄      
                                            ▒ ▒ ▒ ▄▀░▓█   ▀▓  ██▒ ▓▒▒████▄    
                                            ░ ▒ ▄▀▒░ ▒███  ▒ ▓██░ ▒░▒██  ▀█▄  
                                              ▄▀▒   ░▒▓█  ▄░ ▓██▓ ░ ░██▄▄▄▄██ 
                                            ▒███████▒░▒████▒ ▒██▒ ░  ▓█   ▓██▒
                                            ░▒▒ ▓░▒░▒░░ ▒░ ░ ▒ ░░    ▒▒   ▓▒█░
                                            ░░▒ ▒ ░ ▒ ░ ░  ░   ░      ▒   ▒▒ ░
                                            ░ ░ ░ ░ ░   ░    ░        ░   ▒   
                                              ░ ░       ░  ░              ░  ░
                                            ░                                 
                                 
{white}                                              GitHub : {github}

                                                  ╔═════════════════╗
                                                  ║ {red}Obfuscator Tool{white} ║
                                                  ╚═════════════════╝

{red}[{white}>{red}]{red} Discord  : {white}{discord_server}
{red}[{white}>{red}]{red} Telegram : {white}{telegram}
{red}[{white}>{red}]{red} Instagram : {white}{instagram}
""")

    file_python = ChoosePythonFile()
    print(f"""
    {red}[{white}1{red}] {white}Weak
    {red}[{white}2{red}] {white}Medium
    {red}[{white}3{red}] {white}Strong
    {red}[{white}4{red}] {white}Very Strong
    """)
    obfuscation_force = int(
        input(
            f"{BEFORE + current_time_hour() + AFTER} {INPUT} Obfuscation Force -> {reset}"
        )
    )
    if obfuscation_force == 1:
        size_1 = 8
        size_2 = 15
    else:
        if obfuscation_force == 2:
            size_1 = 10
            size_2 = 25
        else:  # inserted
            if obfuscation_force == 3:
                size_1 = 30
                size_2 = 50
            else:  # inserted
                if obfuscation_force == 4:
                    size_1 = 50
                    size_2 = 100
                else:  # inserted
                    print(
                        f"{BEFORE + current_time_hour() + AFTER} {ERROR} Invalid Number."
                    )
                    return
    if "\\" in file_python:
        file_name = file_python.split("\\")[(-1)]
    else:  # inserted
        if "/" in file_python:
            file_name = file_python.split("/")[(-1)]
        else:  # inserted
            file_name = file_python
    with open(file_python, "r", encoding="utf-8") as file:
        script = file.read()
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Deleting previous folders..")
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    time.sleep(1)
    print(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} The previous folders was deleted."
    )
    print(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} Creation of the folder: {white + folder}"
    )
    os.mkdir(folder)
    time.sleep(1)
    print(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} Creation of the folder: {white + output_folder_1}"
    )
    os.mkdir(output_folder_1)
    print(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} Creation of the folder: {white + script_folder}"
    )
    os.mkdir(script_folder)
    time.sleep(1)
    print(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} Copy python script to: {white + script_folder}/{file_name}"
    )
    with open(f"{script_folder}/{file_name}", "w", encoding="utf-8") as file:
        file.write(script)
    print(f"{BEFORE + current_time_hour() + AFTER} {WAIT} Obfuscation in progress..")
    obfuscated_script = obfuscate(script, size_1, size_2)
    with open(f"{output_folder_1}/{file_name}", "w", encoding="utf-8") as file:
        file.write(obfuscated_script)
    print(
        f"{BEFORE + current_time_hour() + AFTER} {INFO} Obfuscation finish: {white + output_folder_1}/{file_name}"
    )


while True:
    Zeta_Obfuscator()
    input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Press to continue.. ")
