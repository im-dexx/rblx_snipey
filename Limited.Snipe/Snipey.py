'''
[=====================================]
[ █▀ █▄░█ █ █▀█ █▀▀ █▄█ ░ █░░ █▀█ █░░ ]
[ ▄█ █░▀█ █ █▀▀ ██▄ ░█░ ▄ █▄▄ █▄█ █▄▄ ]
[=====================================]
Super Nice RBLX Sniper
Developed by dex#9424
'''

import os
import sys
import webbrowser
import time
import requests

banner = """
█▀ █▄░█ █ █▀█ █▀▀ █▄█ ░ █░░ █▀█ █░░
▄█ █░▀█ █ █▀▀ ██▄ ░█░ ▄ █▄▄ █▄█ █▄▄
"""

if sys.platform == "win32":
    os.system(f"title RBLX/Snipe")
else:
    pass

def clear():
    if sys.platform == "win32":
        os.system('cls')
    else:
        os.system('clear')

clear()
robloxapi = "https://api.roblox.com/"

if not os.path.exists('bin'):
    os.mkdir('bin')

if not os.path.exists(f"bin/nostartup.dex"):
    if not os.path.exists(f"C:/Users/{os.getlogin}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/Startup/LimitedSnipe.pyw"):
        print(banner)
        print("""[RBLX.Snipe - Notification]
        Do you want to allow the program to automatically startup?
        ( Whenever your PC starts-up, the sniper does too) (y/n)\n
        """)
        onstartup = input("> ")
        if onstartup == "y":
            try:
                assetid4startup = input("Asset2snipe (For Startup): ")
                sniperstartup = open(f"C:/Users/{os.getlogin}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/LimitedSnipe.pyw", "w")
                sniperstartup.write("""
    asset = requests.get(robloxapi+f"marketplace/productinfo?assetId={assetid4startup}").json()

    while True:
        if asset["IsForSale"] == True:
            webbrowser.open("https://www.roblox.com/catalog/{}/".format(assetid4startup))
            time.sleep(30)
            break
                """)
                sniperstartup.close()
                clear()
            except:
                print("""[RBLX.Snipe - Error]
    Sorry, we do not have permissions to add the program to your startup folder.
                """)
                nostartup = open("bin/nostartup.dex", 'w')
                nostartup.close()
                input("Click [ENTER] to continue")
                clear()
        else:
            nostartup = open("bin/nostartup.dex", 'w')
            nostartup.close()
            clear()
else:
    pass

print(banner)
def sniper():
    try:
        assetid = input("Asset2snipe: ")
        asset = requests.get(robloxapi+f"marketplace/productinfo?assetId={assetid}").json()
        print("\nYou will be automatically [FORCEFULLY] taken to the assets page once it's available,\nplease do not close this program unless you want to stop the sniper.\n")
        print(f"""[RBLX.Snipe - Item info]
Asset Creator: {asset["Creator"]["Name"]} - {str(asset["Creator"]["Id"])}

Asset Name: {asset["Name"]}
Asset Price: {str(asset["PriceInRobux"])}
Asset Availability (As of now): {str(asset["IsForSale"])}

        """)
        while True:
            if asset["IsForSale"] == True:
                print("[+]: Asset for sale!")
                webbrowser.open("https://www.roblox.com/catalog/{}/".format(assetid))
                time.sleep(30)
                break
    except:
        print("Invalid Asset, try again.")
        time.sleep(1.3)
        clear()
        print(banner)
        sniper()
sniper()