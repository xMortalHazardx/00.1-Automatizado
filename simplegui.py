import FreeSimpleGUI as sg
import json

sg.theme('DarkGrey12')
FILEUSERS = '/home/machine/Documents/00.1-Automatizado/usuários.txt'
FILECHAMADO = '/home/machine/Documents/00.1-Automatizado/chamado.json'

# with open('/home/machine/Documents/00.1-Automatizado/chamado.json','r') as arquivo:
#             chamado = json.load(arquivo)
# def ler_texto(filepath=FILECHAMADO):
#     with open(filepath, 'r') as arquivo:
#         usuario = arquivo.readlines()
#         return usuario


def add_texto(user, filepath=FILEUSERS):       
        with open(filepath, 'w') as arquivo:
            arquivo.writelines(user)      

index_chamado = [
            [sg.Text("Digite o usuário: ")],     
            [sg.InputText(tooltip="Digite o usuário...", key='user', size=[42,10])],
            [sg.Multiline(key='caixa de texto', size=[40,10])],
            [sg.Button("Enviar"), sg.Button("Editar", tooltip="Editar usuário."),
             sg.Button("Apagar",tooltip="Apagar usuário."), sg.Button("Sair")]  
]      
index_login = [
            [sg.Text("Digite o usuário: ")],     
            [sg.InputText(tooltip="Digite o usuário...", key='user', size=[42,10])],
            [sg.InputText(tooltip="Digite o usuário...", key='user', size=[42,10])],
            [sg.Button("Add", tooltip="Adicionar Credenciais.")]
            
            
]

tela_chamado = sg.Window('Chamado Passivo', index_chamado)
tela_login = sg.Window('Login', index_login)

while True:

    event, values = tela_login.read()

    print(1,event)
    
    

    # Processa os eventos da janela
    match event:

        case "Add":
            usuarios = ler_texto()
            novo = values['user'] + "\n"
            usuarios.append(novo)
            add_texto(usuarios)
            window['users'].update(usuarios) 
            
        #---------------------------------------------------------
        case "Editar":
            usuario_editar = values['users'][0]
            novo_usuario = values['user'] + "\n"
            
            usuarios = ler_texto()            
            index = usuarios.index(usuario_editar)
            usuarios[index] = novo_usuario  # Atualiza o nome do usuário.
            add_texto(usuarios)

            window['users'].update(usuarios) # Atualiza o Listbox com a lista editada.
        #---------------------------------------------------------
        #case "Apagar":

                     
            

        case sg.WIN_CLOSED:
            break        
                
            
        case "Sair":
            
            window.close()
            break

arlindo = ler_texto(filepath=FILEUSERS)   

for item in arlindo:
     item.strip()
     print(item)

