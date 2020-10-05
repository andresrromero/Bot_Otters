# -*- coding: utf-8 -*-

import os
import random

#ultimo tuit contestado

def get_ultimo_id(FILE_NAME):
	f_read = open(FILE_NAME, 'r')
	ultimo_id = int(f_read.read().strip())
	f_read.close()
	return ultimo_id

def guardar_ultimo_id(ultimo_id, FILE_NAME):
	f_write = open(FILE_NAME, 'w')
	f_write.write(str(ultimo_id))
	f_write.close()
	return

#ulimo tuit puesto por nutria o carpi

def get_ultimo_tuit(FILE_TUIT):
	f_read = open(FILE_TUIT, 'r')
	tuit_id = int(f_read.read().strip())
	f_read.close()
	return tuit_id

def guardar_ultimo_tuit(tuit_id, FILE_TUIT):
	f_write = open(FILE_TUIT, 'w')
	f_write.write(str(tuit_id))
	f_write.close()
	return

#foto repetida

FILE_REPES = 'fotosrepe.txt'

def get_repes(FILE_REPES):
	f_read = open(FILE_REPES, 'r')
	repes = f_read.read().split("\n")
	f_read.close()
	return repes

def guardar_repes(numero, FILE_REPES):
    nump = len(frases)
    rep = get_repes()
    numr = len(rep)

    if nump-2 == numr:
        rep.pop()
        rep.append('')
        i = len(rep)-1

        while i >=1:
            rep[i] = rep[i-1]
            i = i-1
        rep[0] = phrase
        rep2 = '\n'.join(rep)

        f_write = open(FILE_REPES, 'w')
        f_write.write(rep2)
        f_write.close()
        return
    else:
        e = 0
        while e <= len(rep)-1:
            rep.pop(e)

        i = 0
        while i <= len(frases)-3:
            rep.insert(i, frases[i])
            i = i+1
        rep2 = '\n'.join(rep)

        f_write = open(FILE_REPES, 'w')
        f_write.write(rep2)
        f_write.close()
        return guardar_repes(frase)

#seguidores nutrias

def get_seguidores(FILE_SEGUIDORES):
	f = open(FILE_SEGUIDORES, "r")
	seguidores = f.read().split("\n")
	f.close()
	return seguidores

def guardar_seguidor(FILE_SEGUIDORES, usuario):
	f = open(FILE_SEGUIDORES, "a+")
	f.write(str(usuario) + '\n')
	f.close()
	return

#----------------------------------

def get_numero():
    ruta = "imagenes/"
    fotos = os.listdir(ruta)
    numero = random.randint(0, len(fotos)-1)
    repes = get_repes(FILE_REPES)
    if str(numero) in repes:
        return get_numero()
    else:
        guardar_repes(numero, FILE_REPES)
    return numero

def get_foto(posicion):
	try:
	    ruta = "imagenes/"
	    fotos = os.listdir(ruta)
	    fotos.sort()
	    archivo = ruta+fotos[posicion]
	    return archivo
	except Exception as inst:
	    print(type(inst))
	    print(inst.args)
	    print(inst)

frases = [u"🦦💞🦦", u"🧑‍🤝‍🧑🦦", u"🦦👶", u"🤔🦦", u"🤗🦦", u"🦦", u"🦦🎩", u"😜🦦", u"😨🦦", u"😄🦦", u"💞🦦🦦🦦💞",
u"👀🦦", u"👀🦦", u"🦦❤️", u"🦦❤️", u"🤨🦦", u"🙂🦦", u"😍🦦", u"💂🦦", u"😃🦦🏊", u"🦦😘🦦", u"🦦🦦❤️",
u"🤭🦦", u"🥺🦦👶", u"🦦🙏", u"😡🦦", u"🥺🦦", u"🦦🙏", u"😍🦦", u"💑🦦", u"🦦🤷",
u"😄🦦", u"😴🦦", u"🥰🦦", u"🦦🦀🦦", u"🦦🎁", u"🦦💑", u"🦦🥌", u"🦦💤", u"🦦🏀", u"🍼🦦", u"👀🦦",u"🦦🏊",u"🦦👨‍🦯",
u"🦦👶", u"🦦🥨", u"🥺🦦", u"🧑‍🤝‍🧑🦦", u"🥰🦦🥰", u"🥰🦦🥰", u"🦦🧸", u"👶🦦👶🦦👶🦦👶🦦", u"🦦🧢", u"🦦🦆", u"🦦❤️",
u"🦦🗑️", u"🦦🦈", u"🦦💞", u"🦦😛", u"🦦😀", u"🦦😍", u"🦦😍", u"👩‍👧🦦", u"😍🦦", u"my new friend 😬🦦",
u"🤘🦦🦦🦦🦦🤘", u"🧑‍🤝‍🧑🦦", u"💑🦦", u"👩‍👧🦦", u"chillin 😴🦦", u"😀🎢🌊", u"🦦💃", u"🦦🥺", u"🦦👶🥺", u"🐼🦦",
u"🦦🥺", u"🦦🦦👀", u"👶👶👶👶🦦", u"👩‍👦🦦", u"🥺👶", u"😀🦦", u"🦦💖", u"🦦", u"😀🦦", u"👩‍👦👶🦦", u"💑💚", u"🥺🥺",
u"need glasses... 🦦", u"👩‍👦🥺", u"💏🦦", u"💑🥺", u"💏🦦", u"👩‍🏫🦦", u"🦦🪑", u"🦦🥰", u"🥺👶", u"👩‍👦🥰",
u"🥰🦦🦦🦦🦦🥰", u"smol 🥺", u"🦦", u"🥰", u"🙈", u"🥺🦦", u"💤💤🦦", u"🥰🥰", u"🦦", u"🙏🦦", u"🥰🦦", u"🌻🦦", u"🤗", u"☃️🦦",
u"🥺", u"🧢😎", u"🥺🥰", u"🎂", u"🐻‍❄️🥺", u"👬", u"🥺", u"🦦", u"🦦👀", u"🌼🦦🌼", u"🏞️", u"am I dreamin? 😯", u"🦦😂🥺",
u"cute booty 🦦", u"🥺🍼", u"🦦", u"🦦", u"🦡", u"🦦", u"🦦😋", u"waitin for some food 🦦", u"😨",
u"I know tis acc is about otters but this reindeer is awesome 😍", u"🦦", u"💤👭", u"👶🥺", u"🔑🦦", u"ouroboros otter",
u"😍", u"hello otter", u"😱", u"🦦", u"🥺", u"😁", u"cute crab", u"need cuddles", u"sleeping it off", u"🦦🐥", u"🦦",
u"icy friends", u"😍", u"🙏",u"zzz", u"😲", u"my new hat rocks", u"🦦", u"💤💤", u"big cuteness", u"iughhh", u"🧸", u"🦦", u"🦦",
u"🦦💞", u"friends 🦦", u"🦦", u"🦦👀", u"👩‍👧", u"🦦", u"superotter", u"💓", u"🦦", u"🦦🦦🦦", u"🦦💓", u"🦦", u"🙌", u"🦦",
u"chill", u"🦦", u"best friends", u"🦦", u"🥰🥰🥰"]
def get_frase(posicion):
	try:
		return frases[posicion]
	except Exception as inst:
	    print(type(inst))
	    print(inst.args)
	    print(inst)