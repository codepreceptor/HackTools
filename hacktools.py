import os

require = '''echo {} | pkg up
pip install colorama lolpython
pkg install python figlet'''

os.system(require)
import  time,webbrowser
from colorama import Fore
from lolpython import lol_py 


def wait():
    time.sleep(1.2)
    
def clear():
    os.system("clear")

def logo():
     print(Fore.RED+"=======================================================")
     text = "echo {}| figlet HACKTOOLS | lolpython"
     os.system(text)
     print(Fore.RED+"===================== version 1.0 =====================\n")


def about_creator():
    creator = "Tool Creator: Code Preceptor"
    telegram = "Telegram Channel: https://t.me/codepreceptor"
    github = "GitHub Profile: https://github.com/codepreceptor"
    youtube = "Youtube Channel: https://youtube.com/@codepreceptor\n"
    
    lol_py(creator)
    lol_py(telegram)
    lol_py(github)
    lol_py(youtube)
    print(Fore.GREEN+"=======================================================\n\n")

def option():
    options = '''    [1] VULNERABILITY SCANNERS (nmap, etc..) 
    [2] EXPLOITATION TOOLS (metasploit, etc..)
    [3] BOMBING TOOLS (xbomb, etc..)
    [4] PHISHING TOOLS (zphisher, etc..)
    [5] NETWORKING TOOLS (ip-tracer, etc..) 
    [0] EXIT'''
    
    
    lol_py(options)

def option_1():
    options_1 = '''    [1] Nmap
    [2] Sqlmap
    [3] TMScanner
    [4] BACK
    [5] EXIT'''
    lol_py(options_1)
    
    user_input =  input(Fore.YELLOW+"Choose Option: ")
    
    try:
        user = int(user_input)
        
        if user == 1:
            option_1()
        elif user == 2:
            option_2()
        elif user == 3:
            option_3()
        elif user == 4:
            clear()
            logo()
            about_creator()
            option()
            choose()
        elif user == 5:
            option_0()
        else:
            option_1()
            
    except ValueError:
        print(Fore.RED+'''Please Choose Correct Option
        Please Wait for 3 Seconds''')
        time.sleep(3)
        os.system("clear")
        option_1()
    
def option_2():
    options_2 = '''    [1] Metasploit Framework
        '''
    lol_py(options_2)
    
    
def option_3():
    options_3 = '''    [1] XBomb
        '''
    lol_py(options_3)
    
          
def option_4():
    options_4 = '''    [1] Zphisher
        '''
    lol_py(options_4)
    
          
def option_5():
    options_5 = '''    [1] Ip-tracer
        '''
    lol_py(options_5)
    
    
def option_0():
    os.system("clear")
    print ("\n\n")
    logo()
    wait()
    about_creator()
    wait()
    thanks = (f"      THANKS FOR USING MY TOOL.\n")
    please = (f"      PLEASE DON'T FORGOT TO JOIN MY YOUTUBE AND TELEGRAM CHANNELS.\n")
    havean = (f"      HAVE A NICE DAY.\n\n") 
    
    lol_py(thanks)
    wait()
    lol_py(please)
    wait ()
    lol_py(havean)
    
    exit()
    
    
def choose():
    print("\n")
    user_input = input(Fore.YELLOW+"Choose Option: ")
    
    try:
        user = int(user_input)
        
        if user == 1:
            option_1()
        elif user == 2:
            option_2()
        elif user == 3:
            option_3()
        elif user == 4:
            option_4()
        elif user == 5:
            option_5()
        elif user == 0:
            option_0()
        else:
            print(Fore.RED+'''Please Choose Correct Option
        Please Wait for 3 Seconds''')
            time.sleep(3)
            os.system("clear")
            home() 
    except ValueError:
        print(Fore.RED+'''Please Choose Correct Option
        Please Wait for 3 Seconds''')
        time.sleep(3)
        os.system("clear")
        return home()
    
        
def home():
    clear()
    logo()
    about_creator()
    option()
    choose()                          
    
    

home() 
