import time
#import tkinter as tk
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

#options.add_argument("--headless=new")  

#template para TKInter


# def abrirJS():
#     with open('/home/machine/Documents/Python/Files/credentials.json','r') as arquivo:
#         todo = json.load(arquivo)
#     return todo 

#root= tk.Tk()
#root.title("Chamado Passivo")

#canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
#canvas1.pack()

#Possivel Logica com o While para realizar a abertura dos chamados de acordo com o index.



class ChamadoPassivo:       

    def __init__(self, driver):
        self.driver = driver        
        # --- Realiza a abertura da página
        url = "https://ca.grupocarbel.com.br/SSM/Account/LogOn?opcao=logoff"        
        self.driver.get(url)
        time.sleep(10)
        pass

    def login(self):
        
        with open('/home/machine/Documents/Jason.json', 'r') as file:
            cred = json.load(file)
        # --- Preenche formulário com usuário e senha.
        usuario = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='UserName']")))   
        usuario.send_keys(cred["User"])

        senha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='Key']")))    
        senha.send_keys(cred["Password"])

        # --- Clica em continuar para login.
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "btnContinuar")))
        button.click()
        time.sleep(5)

        return usuario, senha

    def abertura_passivo(self,user):

        # --- 1- step: Clicar na opção novo chamado na tela do C.A.
        buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"opcaoBoxNovoChamado")))
        buton.click() 
        # --- 2- step: Clicar na Lupa e abrir caixa para filtro de usuário na tela do C.A.
        buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"abrirSelecaoSolicitante")))
        buton.click() 
        # --- 3- step: Clicar na opção Filtro em Seleçao De Pessoa na tela do C.A.
        wait = WebDriverWait(driver, 10)
        icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//th[@data-field='Login']//span[@class='k-icon k-filter']")))
        icon.click()
        # --- Inserção de informação dentro do campo para aplicar a busca especializada.
        buton = driver.find_element(By.XPATH, "//input[@data-bind='value:filters[0].value' and @class='k-textbox']")
        buton.send_keys(user)
        time.sleep(5)
        # --- Botão Aplicar a busca especializada.
        buton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit' and text()='Aplicar']")))
        buton.click()
        # --- Botão Validar para aplicar a busca especializada.
        icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td//span[@class='k-icon k-i-tick']/parent::a")))    
        icon.click()
        time.sleep(15)

        # icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td//span[@class='k-icon k-i-tick']/parent::a")))    
        # icon.click()

        # icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td//span[@class='k-icon k-i-tick']/parent::a")))    
        # icon.click()

        # icon = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//td//span[@class='k-icon k-i-tick']/parent::a")))    
        # icon.click()
        
        pass 

c = ChamadoPassivo(driver)
c.login()
c.abertura_passivo("jessica.alves")

driver.quit()