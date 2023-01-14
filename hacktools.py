import os, time,pyfiglet,webbrowser
from colorama import Fore
from lolpython import lol_py 



def clear():
    os.system("clear")

logo = Fore.BLUE+pyfiglet.figlet_format("HACKTOOLS")

def option():
    options = '''    [1] VULNERABILITY SCANNERS (nmap, etc..) 
    [2] EXPLOITATION TOOLS (metasploit, etc..)
    [3] BOMBING TOOLS (xbomb, etc..)
    [4] PHISHING TOOLS (zphisher, etc..)
    [5] NETWORKING TOOLS (ip-tracer, etc..) '''
    
    
    lol_py(options)

clear() 
get_url= webbrowser.open('https://t.me/codepreceptor')
print(logo)   
option()