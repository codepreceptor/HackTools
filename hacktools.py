import os, time,pyfiglet,webbrowser
from colorama import Fore
from lolpython import lol_py 



def clear():
    os.system("clear")

def logo():
     print(Fore.RED+"=======================================================")
     print(Fore.GREEN+pyfiglet.figlet_format(" HACKTOOLS "))
    
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
    [3] TMScanner   '''
    lol_py(options_1)
    
    
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
    about_creator()
    thanks = '''      Thanks For Using My Tool.\n
      PLEASE DON'T FORGET TO JOIN MY TELEGRAM AND YOUTUBE CHANNEL.\n
      HAVE A GOOD DAY.\n
    '''   
    lol_py(thanks)
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
    
    
get_url= webbrowser.open('https://t.me/codepreceptor')

home() 
