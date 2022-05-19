import os
from xml.dom import NotFoundErr
from discord import Webhook, RequestsWebhookAdapter
import requests


def WebhookComplex(url, username, avatar_url, message):
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    webhook.send(username=username, avatar_url=avatar_url, content=message)

def DeleteWebhook(url):
    webhook = Webhook.from_url(url, adapter=RequestsWebhookAdapter())
    webhook.delete()

def ClearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

ClearConsole()

print("\033[1;35;40m\n")
print("""
                                                             
 _|      _|            _|                            _|  
 _|_|    _|    _|_|_|      _|_|_|  _|_|    _|    _|  _|  
 _|  _|  _|  _|    _|  _|  _|    _|    _|  _|    _|  _|  
 _|    _|_|  _|    _|  _|  _|    _|    _|  _|    _|  _|  
 _|      _|    _|_|_|  _|  _|    _|    _|    _|_|_|  _|  
                       _|                                
                     _|                                  
""")


print("\033[1;32;40m\n")
print("""
1: Spam Webhook
2: Delete Webhook
3: Get Webhook Info
4: Exit
""")

option = int(input("Enter your option: "))

while True:
    if option == 1:
        
        count = 0

        url = input("Webhook url: ")
        username = input("Username: ")
        avatar_url = input("Avatar: ")
        message = input("Message you want to send: ")
        amount = int(input("Amount of times you want to send the message: "))

        for i in range(amount):
            try:
                WebhookComplex(url, username, avatar_url, message)
            except Exception as e:
                if e == "404 Not Found (error code: 10015): Unknown Webhook":
                    print("Webhook has been deleted.")
                    break
            else:
                count += 1
                print(f'Message sent: {count}')
    elif option == 2:

        url = input("Webhook to delete: ")
        try:
            DeleteWebhook(url)
            print("Successfully deleted.")
            break
        except Exception as e:
            if e == "404 Not Found (error code: 10015): Unknown Webhook":
                print("Webhook not found!")
            else:
                print(e)
                exit()
    elif option == 3:
        url = input("Webhook to get info: ")
        try:
            r = requests.get(url)
            json = r.json()

            print("Webhook Info:")
            print("Name: " + json['name'])
            print("Avatar URL: " + f'https://cdn.discordapp.com/avatars/{json["id"]}/{json["avatar"]}.png')
            print("Guild ID: " + json['guild_id'])
            print("Channel ID: " + json['channel_id'])
            print("Webhook ID: " + json['id'])
            print("Webhook Token: " + json['token'])

            break
        except Exception as e:
            if e == "404 Not Found (error code: 10015): Unknown Webhook":
                print("Webhook not found!")
            else:
                print(e)
                exit()
    elif option == 4:
        exit()
    else:
        print("Invalid option!")
        option = int(input("Enter your option: "))






