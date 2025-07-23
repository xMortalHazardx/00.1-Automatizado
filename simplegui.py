import FreeSimpleGUI as sg
import json
import functions as f

sg.theme('DarkGrey12')
   


index_chamado = [
            [sg.Text("Digite o usuário: ")],
            [sg.Input(tooltip="Digite o usuário...", key='user', size=[42,10], justification='right')],
            [sg.Text("Descrição do chamado: "),sg.Text("Finalizar chamado: ")],
            [sg.Multiline(key='descricao_chamado', size=[40,10], justification='left'),             
             sg.Multiline(key='finalizacao_chamado', size=[40,10], justification='right')],
            [sg.Button("Enviar", key="Enviar", tooltip="Envia o chamado com finalização"),sg.Button("Sair", key="Sair", tooltip="Sair do programa")]  
]      
index_login = [
            [sg.Text("Digite o usuário: ")],     
            [sg.Input(tooltip="Digite o usuário...", key='user', size=[42,10])],
            [sg.Input(tooltip="Digite sua senha...",password_char='xxxxxxxxxxx', key='pass', size=[42,10])],
            [sg.Button("Add", tooltip="Adicionar Credenciais.")]            
]

tela_chamado = sg.Window('Chamado Passivo', index_chamado, auto_size_buttons=True, element_justification='center')
tela_login = sg.Window('Login', index_login, element_justification='center')

while True:

    event, values = tela_login.read()
    usuario = f.abrirJS()
    

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
                f.guardar_user(novo_usuario)               
                
                sg.popup("Usuário adicionado com sucesso!")
                tela_login.close()                
            continue

    event, values = tela_chamado.read()

    match event:

        case "Enviar":
            texto = {
                "usuario": values['user'],
                "descricao": values['descricao_chamado'],
                "finalizar": values['finalizacao_chamado']}
            
            f.chamado_final1(texto)
            
            import Automation as automacao
            automacao.main()  # Chama a função principal do script Automation.py
            continue

        case "Sair":
            tela_chamado.close()
            tela_login.close()
            break          

        case sg.WIN_CLOSED:
            break        




