import colorama
import sys
# import pyfiglet
import pyautogui
import random
import os
import tkinter
import requests
import jdatetime
import time

os.system("color")

class start_terminal:
    """
# starts terminal
this class has been updated by soodi592 in 1403-10-9 or 2024-12-29
    """
    


    def __init__(self) -> None:

        helptxt = colorama.Fore.GREEN+"""
commands:
 text commands:
  textadd {name}
  textedit {name}
  textload {name}
  texts
  pyide {filename.py}"""+colorama.Fore.WHITE+"""

 file commands:
  dirm {dirname} (makes a dir)
  dirr {dirname} (removes a dir)
  rnf {oldname_or_dir} {newname} (renames a file)
  dlfile {filename} (deletes a file)
  mkfile {filename} (makes a file)
  open | writefile {file_name_or_path}
  read {file_name_or_path}
 """+colorama.Fore.LIGHTRED_EX+"""
 system commands:
  toc (Turn Off Computer)
  rst (Restart Computer)
  hib (Hibernate Computer)
  slp (Sleep Computer)
 
 """+colorama.Fore.YELLOW+"""
 not categorized:
  info
  cmd
  ps
  net | internet
  c {like_2+2} (calculates anything)
  pypkg {python package name}
  clear | cls
  close
  help"""
    
        ff = """
                                                                                 
       _______  _______  _______  ______   ___   _______  _______  _______       
      |       ||       ||       ||      | |   | |       ||  _    ||       |      
      |  _____||   _   ||   _   ||  _    ||   | |   ____|| | |   ||____   |      
      | |_____ |  | |  ||  | |  || | |   ||   | |  |____ | |_|   | ____|  |      
      |_____  ||  |_|  ||  |_|  || |_|   ||   | |_____  ||___    || ______|      
       _____| ||       ||       ||       ||   |  _____| |    |   || |_____       
      |_______||_______||_______||______| |___| |_______|    |___||_______|      
                                                                                 
                                                                                 
"""

        # ff = pyfiglet.figlet_format("soodi592-Terminal")

        for x in ff:
            sys.stdout.flush()
            print(colorama.Fore.BLACK+colorama.Back.RED+x,end="")
            time.sleep(0.005)
        print(colorama.Style.RESET_ALL)

        now = sys.path[0]
        
        saved = {}
        snames = []
        status = True
        while status == True:
            today = jdatetime.datetime.today()
            print(colorama.Fore.RED+
                  f"[{today.strftime('%Y/%m/%d')}][{time.strftime('%H:%M:%S')}]"+
                  colorama.Fore.GREEN,
                  sys.path[0].capitalize()+">"+
                  colorama.Style.RESET_ALL,"",end="")
            user = input().lower()

            if user == "info" or "about" in user:
                print("""
this terminal have been writed by soodi592
github : """+colorama.Fore.BLUE+"https://github.com/soodi592/",colorama.Style.RESET_ALL+"""
my website :"""+colorama.Fore.BLUE+"https://soodi592.ir/",colorama.Style.RESET_ALL)
            elif user == "help":
                print(helptxt)
            
            elif user.startswith("dirm"):
                dirm = user.replace("dirm","").replace(" ","")
                os.mkdir(dirm)
                print("folder have been created")

            elif user.startswith("dirr"):
                os.rmdir(user.replace("dirr ",""))
                print("delete successfully")

            elif user.startswith("rnf"): 
                try:
                    os.rename(user.removeprefix("rnf ").split(" ")[0],user.removeprefix("rnf ").split(" ")[1])
                except:
                    print("Error")

            elif user.startswith("cd"):
                sys.path[0] = sys.path[0]+user.replace("cd ","")
            

            elif user == "clear" or "cls" in user: os.system("cls")



            elif user.startswith("pypkg "):
                os.system(f"pip install {user.replace('pypkg','')}")

            elif user.startswith("mkfile"):
                open(user.replace("mkfile ",""),"w",encoding="utf-8")
                print("file has been created successfully!")

            elif user.startswith("dlfile"):
                os.remove(user.replace("dlfile ",""))
                print("file has been deleted successfully!")
            
            elif user.startswith("writefile"):
                os.system(user.replace("writefile ",""))
            
            elif user.startswith("open "):
                os.system(user.replace("open ",""))
            
            elif user.startswith("read "):
                print(open(user.replace("read ",""),"r",encoding="utf-8").read())
            
            elif "exit" in user:
                exit()

            elif user.replace(" ","") == "":
                pass

            elif user.replace(" ","") == "tree":
                os.system("tree")

            elif user == "internet" or user == "net":
                try:
                    requests.get("https://google.com/")
                    print("you are"+colorama.Fore.GREEN+" connented "+colorama.Style.RESET_ALL+"to internet")
                except:
                    print("you are "+colorama.Fore.RED+"not"+colorama.Style.RESET_ALL+" conneted to internet")

            elif user.startswith("pyide"):
                n = 0
                ind = ""
                l = []
                while True:
                    i = input(ind)
                    if i.endswith(":"):
                        ind+="    "
                        l.append(ind+i+"\n")
                    elif i.endswith("=|"):
                        ind = ind.removeprefix("    ")
                        l.append(  ind+i+"\n"  )
                    elif i.endswith(";"):
                        l.append(  ind+i.removesuffix(";")+"\n"  )
                        break
                    else:
                        l.append(  ind+i+"\n"  )
                fn = user.removeprefix("pyide ")
                open(fn,"w",encoding="utf-8").writelines(l)




            elif user.startswith("textadd "):
                saved[user.removeprefix("textadd ")] = ""
                snames.append(user.removeprefix("textadd "))



            elif user.startswith("textload "):
                if user.removeprefix("textload ") in snames:
                    print(saved[user.removeprefix("textload ")])
                else:
                    print(f"there is not anything called "+colorama.Fore.RED+f"{user.removeprefix('textload ')}"+colorama.Style.RESET_ALL)

            elif user.startswith("textedit "):
                
                if user.removeprefix("textedit ") in snames:
                    f = ""

                    while True:
                        i=input("> ")
                        if i.endswith(";"):break
                        f+=i+"\n"
                    saved[user.removeprefix("textedit ")] = f
                else:
                    print("can't find that.")

            elif user == "texts":
                print(snames)
            

            elif user.startswith("c "):
                try:
                    print(colorama.Fore.CYAN+str(eval(user.removeprefix("c "))))
                except:
                    print(colorama.Fore.RED+"[ERROR] : "+colorama.Fore.WHITE+f"interpreter couldn't calc this")

            elif user == "cmd":
                print(colorama.Fore.CYAN)
                os.system("cmd")
                print(colorama.Style.RESET_ALL)

            elif user == "ps":
                print(colorama.Fore.GREEN)
                os.system("powershell")
                print(colorama.Style.RESET_ALL)
            
            elif user == "close":
                print(colorama.Fore.LIGHTMAGENTA_EX+"""
            ┊         ┊       ┊   ┊    ┊        ┊
┊         ┊       ┊   ┊   ˚★⋆｡˚  ⋆
┊         ┊       ┊   ⋆
┊         ┊       ★⋆
┊ ◦
★⋆      ┊ .  ˚
           ˚★
           

           Program Closed."""+colorama.Style.RESET_ALL)
                status = False

            elif user == "toc":
                os.system("shutdown /s /t 0")

            elif user == "rst":
                os.system("shutdown /r /t 0")

            elif user == "hib":
                os.system("shutdown /h")

            elif user == "slp":
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            else:
                print(f"'{user}' not in commands.")
            


        

start_terminal()