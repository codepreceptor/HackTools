import os
import  time
from colorama import Fore
from lolpython import lol_py 


def wait():
    time.sleep(1.2)
    
def clear():
    os.system("clear")

def logo():
     print(Fore.RED+"======================================================")
     text = "echo {}| figlet HACKTOOLS | lolpython"
     os.system(text)
     print(Fore.RED+"===================== version 1.0 ====================\n")


def about_creator():
    creator = "Tool Creator: Code Preceptor"
    telegram = "Telegram Channel: https://t.me/codepreceptor"
    github = "GitHub Profile: https://github.com/codepreceptor"
    youtube = "Youtube Channel: https://youtube.com/@codepreceptor\n"
    
    lol_py(creator)
    lol_py(telegram)
    lol_py(github)
    lol_py(youtube)
    print(Fore.GREEN+"======================================================\n\n")

def option():
    options = '''    [1] VULNERABILITY SCANNERS (nmap, etc..) 
    [2] EXPLOITATION TOOLS (metasploit, etc..)
    [3] BOMBING TOOLS (xbomb, etc..)
    [4] PHISHING TOOLS (zphisher, etc..)
    [5] NETWORKING TOOLS (ip-tracer, etc..) 
    [0] EXIT'''
    
    
    lol_py(options)

def option_1():
    options_1_1 = '''    [1] Nmap
    [2] Sqlmap
    [3] TMScanner
    [4] BACK
    [5] EXIT'''
    lol_py(options_1_1)
    
    user_input =  input(Fore.YELLOW+"Choose Option: ")
    
    try:
        user = int(user_input)
        
        if user == 1:
            nmap = "pkg install nmap"
            os.system(nmap)        
            print("Installation Successful. Type nmap --help for getting help.")
        elif user == 2:
            sqlmap = "cd $HOME && git clone --depth 1 https://github.com/sqlmapproject/sqlmap"
            os.system(sqlmap)
            print("Installation Successful. Type cd sqlmap && python sqlmap.py -h to get Help.")
        elif user == 3:
            tmscanner = " cd $HOME && apt update && apt upgrade && apt install git python2 && git clone https://github.com/TechnicalMujeeb/TM-scanner.git && cd TM-scanner && chmod +x * && sh install.sh"
            os.system(tmscanner)
            print("Installation Successful. Type cd TM-scanner && python2 tmscanner.py to Start.")
        elif user == 4:
            home()
        elif user == 5:
            option_0()
        else:
            logo()
            option_1()
            
    except ValueError:
        error()
        option_1()
    
def option_2():
    options_2_1= '''    [1] Metasploit Framework
    [2] BACK
    [0] EXIT'''
    lol_py(options_2_1)
    user_input =  input(Fore.YELLOW+"Choose Option: ")
    try:
        user = int(user_input)
        if user == 1:
            metasploit = ''' cd $HOME && pkg update
            pkg install wget -y
            wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh
            bash metasploit.sh
            rm metasploit.sh
            cd metasploit-framework
            bundle install '''
            os.system(metasploit )
            
        elif user == 0:
            option_0()
        
        elif user == 2:
            home()
            
        else:
            logo()
            about_creator()
            option_2()
            
    except ValueError:
            error()
            option_2()
    
def option_3():
    options_3_1 = '''    [1] XBomb
    [2] BACK
    [3] EXIT
        '''
    lol_py(options_3_1)
    user_input =  input(Fore.YELLOW+"Choose Option: ")
    try:
        user = int(user_input)
        if user == 1:
            xbomb = "cd $HOME && git clone https://github.com/mr-exo/XBomb.git"
            os.system(xbomb)
            print("Installation Successful. Type cd XBomb && pip install -r requirements.txt && python XBomb.py to Start")
            
        elif user == 2:
            home()
         
        elif user == 0:
            option_0()
        
        else:
            logo()
            about_creator()  
            option_3()
            
    except ValueError:
            error()
            option_3()                
    
          
def option_4():
    options_4_1= '''    [1] Zphisher
    [2] BACK
    [0] EXIT        '''
    lol_py(options_4_1)
    user_input = input(Fore.YELLOW+"Choose Option: ")
    try :
          user = int(user_input)
          if user == 1:
              zphisher = '''cd $HOME && pkg install tur-repo
 pkg install zphisher
 zphisher''' 
              os.system(zphisher)
              print("Installation Successful. Type zphisher to Start")
          
          elif user == 2:
              home()
           
          elif user == 0:
              option_0()
           
          else:
              logo()
              about_creator()
              option_4()
              
    except ValueError:
            error()
            option_4()                               
          
def option_5():
    options_5_1 = '''    [1] IP-Tracer
    [2] BACK
    [0] EXIT        '''
    lol_py(options_5_1)
    
    user_input = input(Fore.YELLOW+"Choose Option: ")
    try :
          user = int(user_input)
          if user == 1:
              ip = '''cd $HOME && git clone https://github.com/rajkumardusad/IP-Tracer.git
cd IP-Tracer
chmod +x install
sh install '''
              
              os.system(ip)
              print("Installation Successful. Type trace -t target-ip to Trace.")
          elif user == 2:
             home()
             
          elif user == 0:
             option_0()
             
          else:
             logo()
             about_creator()
             option_5()

    except ValueError:
            error()
            option_5()                  
    
def option_0():
    os.system("clear")
    print ("\n\n")
    logo()
    wait()
    about_creator()
    wait()
    thanks = (f"                      THANKS FOR USING MY TOOL.\n")
    please = (f"      PLEASE🙏 DON'T FORGOT TO JOIN MY YOUTUBE AND TELEGRAM CHANNELS.\n")
    havean = (f"                      HAVE A NICE DAY😊.\n\n") 
    
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
        home()
    
        
def home():
    clear()
    logo()
    about_creator()
    option()
    choose()                          

def error():
        print(Fore.RED+'''Please Choose Correct Option
        Please Wait for 3 Seconds''')
        time.sleep(3)
        os.system("clear")
        logo()
        about_creator()    
    

home() 
