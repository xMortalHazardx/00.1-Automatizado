import time
import json

def abrirJS():
    with open('/home/machine/Documents/00.1-Automatizado/credenciais.json','r') as arquivo:
        todo = json.load(arquivo)
    return todo 


def guardar_user(user, filepath='/home/machine/Documents/00.1-Automatizado/credenciais.json'):
    with open(filepath, 'w') as arquivo:
        json.dump(user, arquivo, indent=4)
        return user

