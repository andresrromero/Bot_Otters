# -*- coding: utf-8 -*-

import tweepy
import time
from datetime import datetime
import os
import nutri_files as nf

CONSUMER_KEY = '352oqn3WeetoWmgUcYOEHeLvQ'
CONSUMER_SECRET = 'fSglbCArqclsxEZzweGckmiMbLFDzAk82UroqwmJfOmHHaYEYH'
ACCESS_KEY = '1271571850045390848-pcobswPwaZVRtWZOnE95aXeQga7X02'
ACCESS_SECRET = 'WHM9prfRsc5XNBptqHLXoqYlieRsTopkWnBrtScZjHZiV'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

FILE_NAME = 'ultimo_id_nutri.txt'
FILE_SEGUIDORES = 'seguidores_nutria.txt'

def contestar():
	print("Contestando tweets bien nutriosos...")
	ultimo_id = nf.get_ultimo_id(FILE_NAME)

	try:
	    menciones = api.mentions_timeline(since_id = ultimo_id, tweet_mode='extended', count = 199)
	    for mencion in reversed(menciones):
	        try:
	            if mencion.user.screen_name != "Bot_ArticFox" and mencion.user.screen_name != "Bot_Otters" and mencion.user.screen_name != "Bot_Carpinchos":
	                print(str(mencion.id) + ' - @' + mencion.user.screen_name + ' - ' + mencion.full_text + "\n")
	                posicion = nf.get_numero()
	                foto = nf.get_foto(posicion)
	                api.update_with_media(filename = foto, status = '@' + mencion.user.screen_name + ' ' + nf.get_frase(posicion), in_reply_to_status_id = mencion.id)
	                nf.guardar_ultimo_id(mencion.id, FILE_NAME)
	            else:
	                nf.guardar_ultimo_id(mencion.id, FILE_NAME)
	        except Exception as inst:
	            print(type(inst))
	            print(inst.args)
	            print(inst)
	            print("-----------------------------------------------------")
	            if mencion == menciones[0]:
	                if inst.api_code == 185:
	                    print("A dormir media horita crack que has superado los tweets")
	                    time.sleep(900)
	                elif inst.api_code == 326:
	                    print("MADRE MADREEEEEEEEE")
	                    time.sleep(9000)
	except Exception as inst:
	    print(inst)
	    print(type(inst))
	    print(inst.args)
	    print(u"NO pilló las menciones \n")

def saludar_despedir():
	print("Saludando a los nuevos amantes de las nutrias...")
	seguidores = nf.get_seguidores(FILE_SEGUIDORES)
	seguidores.pop()
	seguidores = seguidores[-500:]

	try:
	    seguidores_actuales = api.followers(count = 199)
	    for seguidor_actual in reversed(seguidores_actuales):
	        if seguidor_actual.screen_name in seguidores[::-1]:
	            pass
	        else:
	            try:
	                print("Nuevo follower amante de las nutrias: @" + seguidor_actual.screen_name + "\n")
	                posicion = nf.get_numero()
	                api.update_with_media(filename = nf.get_foto(posicion), status = u"Welcome, @" + seguidor_actual.screen_name + u" ❤️")
	                nf.guardar_seguidor(FILE_SEGUIDORES, seguidor_actual.screen_name)
	            except Exception as inst:
	                print(type(inst))
	                print(inst.args)
	                print(inst)
	                print("-----------------------------------------------------")
	                if seguidor_actual == seguidores_actuales[0]:
	                    if inst.api_code == 185:
	                        print("A dormir media horita crack que has superado los tweets")
	                        time.sleep(900)
	                    elif inst.api_code == 326:
	                        print("MADRE MADREEEEEEEEE")
	                        time.sleep(9000)
	except Exception as inst:
	    print(inst)
	    print(type(inst))
	    print(inst.args)
	    print(u"NO pilló los seguidores \n")

def compararlong():
    ruta = "imagenes/"
    fotos = os.listdir(ruta)
    print("Fotos: " + str(len(fotos)))
    print("Frases: " + str(len(nf.frases)))

def foto_frase():
    ruta = "imagenes/"
    fotos = os.listdir(ruta)
    fotos.sort()
    i=0
    while i < len(fotos):
	    print(nf.get_foto(i))
	    print(nf.get_frase(i))
	    i = i+1

while True:
    momento = datetime.now()
    print(momento.time())

    #compararlong()
    #foto_frase()

    try:
        contestar()
        saludar_despedir()
    except Exception as inst:
        print(type(inst))
        print(inst)

    #upload_result = api.media_upload('/home/andresdev/nutrias/videos/aaa.mp4')
    #api.update_status(status="test tweet", media_ids=[upload_result.media_id_string])

    print("Prosigamos \n")
    time.sleep(120)