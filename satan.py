import os,platform
os.system('git pull')
os.system("clear")
os.system("pip install pycurl")
os.system("pip uninstall httpx -y")
os.system("pip install httpx")
os.system("pip uninstall httpx requests -y")
os.system("pip install requests httpx")
#print('\033[92;1m Join Whatsapp Group')
#os.system('xdg-open ')
satan=platform.architecture()[0]
if satan=="32bit":
    __import__("p32")
elif satan=="64bit":
    __import__("p64")
