#DON'T COPY IT WITHOUT CREDIT.
#OUR TELEGRAM CHANNEL: https://t.me/codepreceptor


import os
import time
from colorama import Fore
from lolpython import lol_py

update_message = Fore.GREEN + "Tool Update Successful. "

def execute_command(command, success_message):
    os.system(command)
    print(success_message)

def clear_screen():
    os.system("clear")

def display_header():
    print(Fore.RED + "======================================================")
    text = "echo {}| figlet HACKTOOLS | lolpython"
    os.system(text)
    print(Fore.RED + "===================== version 1.2 ====================\n")

def display_about_creator():
    creator = "Tool Creator: Code Preceptor"
    telegram = "Telegram Channel: https://t.me/codepreceptor"
    github = "GitHub Profile: https://github.com/codepreceptor"
    youtube = "Youtube Channel: https://youtube.com/@codepreceptor\n"

    lol_py(creator)
    lol_py(telegram)
    lol_py(github)
    lol_py(youtube)
    print(Fore.GREEN + "======================================================\n\n")

def install_tool(tool_name, install_command, success_message):
    user_input = input(Fore.YELLOW + f"Install {tool_name}? (y/n): ")
    if user_input.lower() == 'y':
        execute_command(install_command, success_message)

def option_vulnerability_scanners():
    options = '''    [1] Nmap
    [2] Sqlmap
    [3] TMScanner
    [4] Kali Linux 
    [5] BACK
    [6] EXIT'''
    lol_py(options)

    user_input = input(Fore.YELLOW + "Choose Option: ")

    try:
        user = int(user_input)

        if user == 1:
            install_tool("Nmap", "pkg install nmap", "Installation Successful. Type nmap --help for help.")
        elif user == 2:
            install_tool("Sqlmap", "cd $HOME && git clone --depth 1 https://github.com/sqlmapproject/sqlmap", "Installation Successful. Type cd sqlmap && python sqlmap.py -h to get Help.")
        elif user == 3:
            install_tool("TMScanner", "cd $HOME && apt update && apt upgrade && apt install git python2 && git clone https://github.com/TechnicalMujeeb/TM-scanner.git && cd TM-scanner && chmod +x * && sh install.sh", "Installation Successful. Type cd TM-scanner && python2 tmscanner.py to Start.")
        elif user == 4:
            install_tool("Kali Linux", "cd $HOME && apt update && apt upgrade && pkg install wget fish && wget https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-project/raw/master/nethunter-rootless/install-nethunter-termux && chmod +x install-nethunter-termux && ./install-nethunter-termux", '''Installation Successful. Type "nethunter" to start Kali Machine.''')
        elif user == 5:
            home()
        elif user == 6:
            option_exit()
        else:
            display_header()
            option_vulnerability_scanners()
    except ValueError:
        error()
        option_vulnerability_scanners()
        
def option_update_tool():
    run = '''apt update && apt upgrade
    wget -O $PREFIX/bin/hacktools https://raw.githubusercontent.com/codepreceptor/HackTools/main/hacktools
    chmod +x $PREFIX/bin/hacktools
    clear '''
    os.system(run)
    print("\n\n\t[✔️]", update_message, "[✔️]")
    time.sleep(3)
    os.system("python3 $PREFIX/opt/HackTools/hacktools.py")

def option_exit():
    clear_screen()
    display_header()
    wait()
    display_about_creator()
    wait()
    thanks = "           THANKS FOR USING MY TOOL.\n"
    please = "   PLEASE🙏 DON'T FORGET TO JOIN MY YOUTUBE AND TELEGRAM CHANNELS.\n"
    havean = "              HAVE A NICE DAY😊.\n\n"

    lol_py(thanks)
    wait()
    lol_py(please)
    wait()
    lol_py(havean)
    exit()

def wait():
    time.sleep(1.2)

def error():
    print(Fore.RED + '''Please Choose Correct Option
    Please Wait for 3 Seconds''')
    time.sleep(3)
    clear_screen()
    display_header()
    display_about_creator()

def home():
    clear_screen()
    display_header()
    display_about_creator()
    option()
    choose()

def option():
    options = '''    [1] VULNERABILITY SCANNERS (nmap, etc..) 
    [2] EXPLOITATION TOOLS (metasploit, etc..)
    [3] BOMBING TOOLS (xbomb, etc..)
    [4] PHISHING TOOLS (zphisher, etc..)
    [5] NETWORKING TOOLS (ip-tracer, etc..)
    [6] Instagram Brutal Force 
    [7] UPDATE TOOL
    [0] EXIT'''
    lol_py(options)

def choose():
    print("\n")
    user_input = input(Fore.YELLOW + "Choose Option: ")

    try:
        user = int(user_input)

        if user == 1:
            option_vulnerability_scanners()
        elif user == 2:
            option_exploitation_tools()
        elif user == 3:
            option_bombing_tools()
        elif user == 4:
            option_phishing_tools()
        elif user == 5:
            option_networking_tools()
        elif user == 6:
            option_instagram_brutal_force()
        elif user == 7:
            option_update_tool()
        elif user == 0:
            option_exit()
        else:
            print(Fore.RED + '''Please Choose Correct Option
        Please Wait for 3 Seconds''')
            time.sleep(3)
            clear_screen()
            home()
    except ValueError:
        error()
        choose()

if __name__ == "__main__":
    home()
            
 
