import random
from itertools import combinations
import subprocess
import time
import os

def countdown(t):
    while t>0:
        print(t)
        t -= 1
        time.sleep(1)
try:
    os.system("sudo apt install figlet")
    os.system("clear")
    subprocess.call(["figlet","-f","standard","RANDOM MAC"])
    subprocess.call(["figlet","-f","small","Canbrk"])
    time.sleep(2)
    interface = input("İnterface Giriniz (örn:eth0,ens33): ")
    time.sleep(2)
    print("Mac Adresinin Değişmesini İstediğiniz Zaman Aralığını Saniye Cinsinden Giriniz  : ")
    seconds = input()
    while not seconds.isdigit():
        seconds = input()
    seconds = int(seconds)


    while True:
        rasgele = "00:%02x:%02x:%02x:%02x:%02x" % (
        random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),
        random.randint(0, 255),)
        subprocess.call(["ifconfig",interface,"down"])
        subprocess.call(["ifconfig",interface,"hw","ether",rasgele])
        subprocess.call(["ifconfig",interface,"up"])
        print(f"Atanan Mac Adresi {rasgele}")
        countdown(seconds)

except Exception as HATA:
    print(f"Mac Adresi Değiştirilemedi {HATA}")
