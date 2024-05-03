import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DLkY3bmYu212WeecRvkuqQ')
satan=platform.architecture()[0]
if satan=="32bit":
    __import__("p32")
elif satan=="64bit":
    __import__("p64")
