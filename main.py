import time
#import tkinter as tk
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




while True:    
    ## --- Chamador do Google Chrome
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)    
    url = "https://ca.grupocarbel.com.br/SSM/Account/LogOn?opcao=logoff"
    driver.get(url)
    time.sleep(1)
    ## --- Função responsavel pelo Login do usuário no C.A
    # def login(user, senha):
    #     element = driver.find_elements(By.ID,"UserName")
    #     element[0].send_keys("usuário")
    #     element = driver.find_elements(By.ID,"Key")
    #     element[0].send_keys("senha")
    #     time.sleep(1)
    #     element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"btnContinuar")))
    #     element.click()

    ## --- Função Responsável por encontrar o chamado e dar seguimento na finalização.
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID,"buscaRapida")))
    # --- Numero do chamado.
    element.send_keys("Colocar o numero do chamado")
    # --- Busca do Chamado.
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@onclick='buscaRapida();']")))
    element.click() 

    ## --- Função para fechar o chamado que foi encontrado.
    element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, "//span[@id='Realizar']")))    
    element.click()
    # --- Selecionador de opção finalizar chamado.
    element = WebDriverWait(
    driver, 10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='StatusDaAtividadeDoChamadoTipoDeStatusDeAtividadeId_input' and @class='k-input']")))
    element.click()
    element.send_keys("Solucionar Chamado")
    # --- No campo de descrição e finalização do chamado adiciona as informações que foram feitas.
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,"//textarea[@name='DescricaoStatusDaAtividade']")))
    element.send_keys(""" Saudações !
                    Realizado varias tentativas de contato sem sucesso, caso seja necessário tratativa de falha em acessar o site do Dealer, gentileza
                    abrir um novo chamado com um numero de contato válido e disponibilidade para traatativa.""")
    element = WebDriverWait(
        driver,10).until(EC.presence_of_element_located((By.XPATH,"//span[@id='Salvar' and @data-i18n='Salvar' and @comando='Salvar' and text()='Salvar']")))
    element.click()             
    
    
    break