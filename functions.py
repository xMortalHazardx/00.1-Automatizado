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
    
def chamado_final1(finalizar, filepath='/home/machine/Documents/finalizar_chamado.json'):
    with open(filepath, 'w') as arquivo:
        json.dump(finalizar, arquivo, indent=4)
        return finalizar

def chamado_final2(filepath='/home/machine/Documents/finalizar_chamado.json'):
    with open(filepath, 'r') as arquivo:
        todo = json.load(arquivo)
        return todo
