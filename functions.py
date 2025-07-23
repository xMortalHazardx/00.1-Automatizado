import time
import json
from pathlib import Path

caminho_arquivo = Path.home()

def abrirJS():
    with open('c:/users/%username%/appdata/local/temp/credenciais.json','r') as arquivo:
        todo = json.load(arquivo)
    return todo 



def guardar_user(user, filepath=caminho_arquivo/"credenciais.json"):
    with open(filepath, 'w') as arquivo:
        json.dump(user, arquivo, indent=4)
        return user
    
def chamado_final1(finalizar, filepath='c:/users/%username%/appdata/local/temp/finalizar_chamado.json'):
    with open(filepath, 'w') as arquivo:
        json.dump(finalizar, arquivo, indent=4)
        return finalizar

def chamado_final2(filepath='c:/users/%username%/appdata/local/temp/finalizar_chamado.json'):
    with open(filepath, 'r') as arquivo:
        todo = json.load(arquivo)
        return todo


usuario = {}

guardar_user(usuario)