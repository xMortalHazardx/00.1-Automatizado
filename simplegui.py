import FreeSimpleGUI as sg
import json
from functions import abrirJS, guardar_user

sg.theme('DarkGrey12')
   

index_chamado = [
            [sg.Text("Digite o usuário: ")],     
            [sg.InputText(tooltip="Digite o usuário...", key='user', size=[42,10])],
            [sg.Multiline(key='caixa de texto', size=[40,10])],
            [sg.Button("Enviar", key="Enviar", tooltip="Envia o chamado"),sg.Button("Sair", key="Sair", tooltip="Sair do programa")]  
]      
index_login = [
            [sg.Text("Digite o usuário: ")],     
            [sg.Input(tooltip="Digite o usuário...", key='user', size=[42,10])],
            [sg.Input(tooltip="Digite sua senha...",password_char='xxxxxxxxxxx', key='pass', size=[42,10])],
            [sg.Button("Add", tooltip="Adicionar Credenciais.")]            
]

tela_chamado = sg.Window('Chamado Passivo', index_chamado)
tela_login = sg.Window('Login', index_login)

while True:

    event, values = tela_login.read()
    usuario = abrirJS()   

    #   Processa os eventos da janela
    match event:
        
        case "Add":
            if values['user'] == usuario['user'] or usuario['pass'] == values['pass']:
                sg.popup("Login Realizado com Sucesso!.")
                tela_login.close()                               
                continue
                # Tenho que criar uma verificação para não adicionar o usuário 
            # elif values['user'] == "" and values['pass'] == "":
            #     sg.popup_error("Usuário admin não pode ser adicionado.")
            #     continue
            else:
                novo_usuario = {
                    "user": values['user'],
                    "pass": values['pass']
                }
                # Lê o arquivo JSON e adiciona o novo usuário
                guardar_user(novo_usuario)               
                
                sg.popup("Usuário adicionado com sucesso!")
                tela_login.close()                
            continue

    event, values = tela_chamado.read()

    match event:

        case "Enviar":
            import Automation as automacao
            automacao.main()  # Chama a função principal do script Automation.py
            continue

        case "Sair":
            tela_chamado.close()
            tela_login.close()
            break          

        case sg.WIN_CLOSED:
            break        




