import FreeSimpleGUI as sg
import json

FILEPATH = '/home/machine/Documents/Automatizado/00.1-Automatizado/usuários.txt'
FILEARQUIVO = '/home/machine/Documents/Automatizado/00.1-Automatizado/chamado.json'

# with open('/home/machine/Documents/Automatizado/00.1-Automatizado/chamado.json','r') as arquivo:
#             chamado = json.load(arquivo)

def ler_texto(filepath=FILEPATH):
    with open(filepath, 'r') as arquivo:
        usuario = arquivo.readlines()
        return usuario
    

def add_texto(user, filepath=FILEPATH):       
        with open(filepath, 'w') as arquivo:
            arquivo.writelines(user)      

        

label = sg.Text("Digite o usuário: ")
box_usuário = sg.InputText(tooltip="Usuário...", default_text='Digite o usuário..', key='user')
add_buton = sg.Button("Add")
enviar = sg.Button("Enviar")
exit_button = sg.Button("Sair")
window = sg.Window(disable_close=True,title='Chamado Passivo', layout=[[label], [box_usuário, add_buton], [enviar,exit_button]])




while True:
    event, values = window.read()    

    match event:
        case "Add":
            usuarios = ler_texto()
            novo = values['user']
            usuarios.append(novo + "\n")

            add_texto(usuarios)
            
        #case "Editar":
               
            
        case "Sair":
            
            window.close()
            break

    



