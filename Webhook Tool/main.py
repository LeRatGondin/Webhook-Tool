"""
MIT License

Copyright (c) 2021 LeRatGondin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

from os import system
import requests
import json
import time
"""
def install():
	try :
		from discord_webhook import DiscordWebhook

	except ModuleNotFoundError :
		print('Les modules necessaires ne sont pas présents le programme va les installer veuillez patienter')
		time.sleep(1.5)

		try :
			system('python -m pip install discord_webhook')
			time.sleep(1.5)
			system('cls')
			print('Les modules necessaires ont bien été installés')
			input()

		except :
			print("""L'installation a echouée veuillez installer manuelement en ecrivant dans le cmd "pip install discord_webhook" """)
			input()

	system("cls")


headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }

def mes():
	system("cls")
	url = input('Url : ')
	avatar = input("""Url de l'avatar : """)
	username = input("""Nom d'utilisateur : """)
	content = input('Contenu : ')
	nb = input('Le nombre de mess : ')
	try:
		for loop in range(nb):
			webhook = DiscordWebhook(url=url, avatar_url=avatar , username=username , content=content)
			response = webhook.execute()
		system("cls")
		print(f"Le message {content} a bien été envoyé avec comme avatar {avatar} et comme nom d'utilisateur {username}")
		input()
	except:
		system("cls")
		print("Une erreur dans les informations a été detectée veuillez verifier si vous avez bien entré les parametres")
		input()

def delete():
	system("cls")
	url = input("Url : ")
	try:
		requests.delete(url)
		system("cls")
		print(f"Le webhook a bien été suprimé")
		input()
	except:
		system("cls")
		print("Une erreur dans les informations a été detectée veuillez verifier si vous avez bien entré les parametres")
		input()

	
	input()

def patch():
	system("cls")
	url = input('Url : ')
	nom = input('Nouveau nom du webhook : ')
	avatar = input('Nouvel avatar : ')
	values = {"name":nom, "avatar":avatar}
	try:
		requests.patch(url, data=json.dumps(values).encode(), headers = headers)
		print('La modification a bien été faite')
	except:
		system("cls")
		print("Une erreur dans les informations a été detectée veuillez verifier si vous avez bien entré les parametres")
	input()

if __name__ == '__main__':
	install()
	print("""
 __          __  _     _                 _      _              _ 
 \ \        / / | |   | |               | |    | |            | |
  \ \  /\  / /__| |__ | |__   ___   ___ | | __ | |_ ___   ___ | |
   \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ / | __/ _ \ / _ \| |
    \  /\  /  __/ |_) | | | | (_) | (_) |   <  | || (_) | (_) | |
     \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\  \__\___/ \___/|_|
      By Le Rat Gondin                                                               

Entrez 1 Pour pouvoir spam ou envoyer des messages via un webhook
Entrez 2 Pour supprimer un webhook
Entrez 3 Pour modifier le nom et/ou l'avatar d'un webhook                                                                 
""")
	mode = int(input(">>> "))
	if mode == 1 :
		mes()
	if mode == 2 :
		delete()
	if mode == 3 :
		patch()
