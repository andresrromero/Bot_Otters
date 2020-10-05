# -*- coding: utf-8 -*-

import tweepy
import time
from datetime import datetime
import nutri_files as nf

CONSUMER_KEY = '352oqn3WeetoWmgUcYOEHeLvQ'
CONSUMER_SECRET = 'fSglbCArqclsxEZzweGckmiMbLFDzAk82UroqwmJfOmHHaYEYH'
ACCESS_KEY = '1271571850045390848-pcobswPwaZVRtWZOnE95aXeQga7X02'
ACCESS_SECRET = 'WHM9prfRsc5XNBptqHLXoqYlieRsTopkWnBrtScZjHZiV'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_TUIT = '../tuit_id.txt'

def tweet():
	print("Subiendo tweet bien chingoooooooooon...")
	try:
	    posicion = nf.get_numero()
	    tuit = api.update_with_media(filename = nf.get_foto(posicion), status = nf.get_frase(posicion))
	    tuit_id = tuit.id
	    nf.guardar_ultimo_tuit(tuit_id, FILE_TUIT)
	except Exception as inst:
	    print(type(inst))
	    print(inst.args)
	    print(inst)
	    print("-----------------------------------------------------")
	    if inst.api_code == 185:
	        print("A dormir media horita crack que has superado los tweets")
	        time.sleep(900)

def faviarOtters(busqueda):
    print("Buscando tuits que faviar... " + busqueda)
    tweets = api.search(busqueda, result_type = "recent")
    for tweet in tweets:
        if tweet.user.screen_name != "Bot_Otters":
            try:
                api.create_favorite(tweet.id)
                print("faviado\n")
            except Exception as inst:
	            print(type(inst))
	            print(inst.args)
	            print(inst)
	            print("-----------------------------------------------------")
        else:
            pass

def horas():
    if datetime.strptime("00:00:00", "%X").time() < momento.time() and datetime.strptime("00:30:05", "%X").time() > momento.time():
        tweet()
    elif datetime.strptime("03:00:00", "%X").time() < momento.time() and datetime.strptime("03:30:05", "%X").time() > momento.time():
        faviarOtters("otters")
        faviarOtters("nutrias")
        faviarOtters("love animal otter")
        faviarOtters("cute animal")
        tweet()
    elif datetime.strptime("06:00:00", "%X").time() < momento.time() and datetime.strptime("06:30:05", "%X").time() > momento.time():
        tweet()
    elif datetime.strptime("09:00:00", "%X").time() < momento.time() and datetime.strptime("09:30:05", "%X").time() > momento.time():
        faviarOtters("otters")
        faviarOtters("nutrias")
        faviarOtters("love animal otter")
        faviarOtters("cute animal")
        tweet()
    elif datetime.strptime("12:00:00", "%X").time() < momento.time() and datetime.strptime("12:30:05", "%X").time() > momento.time():
        tweet()
    elif datetime.strptime("15:00:00", "%X").time() < momento.time() and datetime.strptime("15:30:05", "%X").time() > momento.time():
        faviarOtters("otters")
        faviarOtters("nutrias")
        faviarOtters("love animal otter")
        faviarOtters("cute animal")
        tweet()
    elif datetime.strptime("18:00:00", "%X").time() < momento.time() and datetime.strptime("18:30:05", "%X").time() > momento.time():
        tweet()
    elif datetime.strptime("21:00:00", "%X").time() < momento.time() and datetime.strptime("21:30:05", "%X").time() > momento.time():
        faviarOtters("otters")
        faviarOtters("nutrias")
        faviarOtters("love animal otter")
        faviarOtters("cute animal")
        tweet()
    else:
        print("Nada que haser...")

    #retweetear a los putos carpinchos
'''
    elif datetime.strptime("02:05:00", "%X").time() < momento.time() and datetime.strptime("02:35:04", "%X").time() > momento.time():
        try:
            api.retweet(nf.get_ultimo_tuit(FILE_TUIT))
            print("Retuiteado un tweet de un carpinxo")
        except Exception as inst:
            print("NO se pudo retuitear al puto carpinxo")
            print(type(inst))
            print(inst.args)
            print(inst)
            if inst.api_code == 185:
                print("A dormir media horita crack que has superado los tweets")
                time.sleep(900)
    elif datetime.strptime("08:05:00", "%X").time() < momento.time() and datetime.strptime("08:35:04", "%X").time() > momento.time():
        try:
            api.retweet(nf.get_ultimo_tuit(FILE_TUIT))
            print("Retuiteado un tweet de un carpinxo")
        except Exception as inst:
            print("NO se pudo retuitear al puto carpinxo")
            print(type(inst))
            print(inst.args)
            print(inst)
            if inst.api_code == 185:
                print("A dormir media horita crack que has superado los tweets")
                time.sleep(900)
    elif datetime.strptime("14:05:00", "%X").time() < momento.time() and datetime.strptime("14:35:04", "%X").time() > momento.time():
        try:
            api.retweet(nf.get_ultimo_tuit(FILE_TUIT))
            print("Retuiteado un tweet de un carpinxo")
        except Exception as inst:
            print("NO se pudo retuitear al puto carpinxo")
            print(type(inst))
            print(inst.args)
            print(inst)
            if inst.api_code == 185:
                print("A dormir media horita crack que has superado los tweets")
                time.sleep(900)
    elif datetime.strptime("20:05:00", "%X").time() < momento.time() and datetime.strptime("20:35:04", "%X").time() > momento.time():
        try:
            api.retweet(nf.get_ultimo_tuit(FILE_TUIT))
            print("Retuiteado un tweet de un carpinxo")
        except Exception as inst:
            print("NO se pudo retuitear al puto carpinxo")
            print(type(inst))
            print(inst.args)
            print(inst)
            if inst.api_code == 185:
                print("A dormir media horita crack que has superado los tweets")
                time.sleep(900)'''

while True:

    momento = datetime.now()
    print(momento.time())

    try:
        horas()
    except Exception as inst:
        print(type(inst))
        print(inst)

    print("Prosigamos")
    time.sleep(1800)