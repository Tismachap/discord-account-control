from art import tprint
from colorama import *
init(autoreset=True)
import requests
from os import system as sys

#Put your token here
token = "YOUR TOKEN HERE"

#Preset des textes
def info(text, complement):
    print("["+Fore.CYAN+text+Fore.RESET+"] "+complement)

def text(text):
    print(Fore.BLACK+Back.WHITE+text)

#Menu de séléctions
tprint('Requests  Discord')
info("1", "Send Messages\n")
info("2", "Modify Messages\n")
info("3", "Delete Messages\n")
info("4", "Add Reactions\n")
info("5", "Infinite Typing\n")

selection = input(">> ")


if selection == str(1):
    sys('cls')

    def url(channel):
        return "https://discord.com/api/v9/channels/"+channel+"/messages"

    auth = {
        'authorization': token
    }

    text("ID CHANNEL :")
    channel_id = input(">> ")

    def send_messages():
        text("\nMESSAGE :")
        message = {
            'content': input(">> ")
        }

        requests.post(url(channel_id), headers=auth, data=message)

        print(info("Tisma", message["content"]))

    while 1<2:
        send_messages() 


if selection == str(2):
    sys('cls')

    def url(channel, message):
        return "https://discord.com/api/v9/channels/"+channel+"/messages/"+message

    auth = {
        'authorization': token
    }

    text("ID CHANNEL :")
    channel_id = input(">> ")

    def edit():
        text("\nID MESSAGE :")
        message_id = input(">> ")

        text("\nMESSAGE :")
        message = {
            'content': input(">> ")
        }

        requests.patch(url(channel_id, message_id), headers=auth, data=message)

    while 1<2:
        edit()


if selection == str(3):
    sys('cls')

    def url(channel, message):
        return "https://discord.com/api/v9/channels/"+channel+"/messages/"+message

    auth = {
        'authorization': token
    }

    def delete():
        text("ID CHANNEL :")
        channel_id = input(">> ")

        text("\nID MESSAGE :")
        message_id = input(">> ")
        
        requests.delete(url(channel_id, message_id), headers=auth)
    while 1<2:
        delete()
    

if selection == str(4):
    sys('cls')

    def url(channel, message, reaction):
        return "https://discord.com/api/v9/channels/"+channel+"/messages/"+message+"/reactions/"+reaction+"/%40me?location=Message&burst=false"
    
    auth = {
        'authorization': token
    }

    def reaction():
        text("ID CHANNEL :")
        channel_id = input(">> ")

        text("\nID MESSAGE :")
        message_id = input(">> ")

        text("\nSELECT REACTION :")
        info("1", "Rofl")
        info("2", "Sob")
        info("3", "Scream")
        info("4", "Confused")
        reaction_selection = input(">> ")

        if reaction_selection == str(1):
            emoji = "%F0%9F%A4%A3"

        if reaction_selection == str(2):
            emoji = "%F0%9F%98%AD"

        if reaction_selection == str(3):
            emoji = "%F0%9F%98%B1"
        
        if reaction_selection == str(4):
            emoji = "%F0%9F%98%95"

        requests.put(url(channel_id, message_id, emoji), headers=auth)

    while 1<2:
        reaction()


if selection == str(5):
    sys('cls')

    def url(channel):
        "https://discord.com/api/v9/channels/"+channel+"/typing"

    auth = {
        'authorization': token
    }

    def typing():
        text("ID CHANNEL :")
        channel_id = input(">> ")

        requests.post(url(channel_id), headers=auth)

    while 1<2:
        typing()

if selection == str(6):
    sys('cls')

    url = "https://canary.discord.com/api/v9/users/@me/settings-proto/1"

    auth = {
        'authorization': "OTgwMTUwMzQ0MDc4MjEzMTYw.GMY873.T0LSWbZ7x49dquCrfK44puOcvimVvIapOfyY6A"
    }
