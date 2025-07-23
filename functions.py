import time
import json

def abrirJS():
    with open('/home/machine/Documents/credenciais.json','r') as arquivo:
        todo = json.load(arquivo)
    return todo 


def guardar_user(user, filepath='/home/machine/Documents/credenciais.json'):
    with open(filepath, 'w') as arquivo:
        json.dump(user, arquivo, indent=4)
        return user

