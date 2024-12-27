import time
#import tkinter as tk
import json
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#template para TKInter


# def abrirJS():
#     with open('/home/machine/Documents/Python/Files/credentials.json','r') as arquivo:
#         todo = json.load(arquivo)
#     return todo 

#root= tk.Tk()
#root.title("Chamado Passivo")

#canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
#canvas1.pack()


while True:
    
    
    options = webdriver.ChromeOptions()
    #options.add_argument("--headless=new")    
    driver = webdriver.Chrome(options=options)


    
    url = "https://ca.grupocarbel.com.br/SSM/Account/LogOn?opcao=logoff"

    driver.get(url)
    time.sleep(1)

    buton = driver.find_elements(By.ID,"UserName")
    buton[0].send_keys("usuário")
    buton = driver.find_elements(By.ID,"Key")
    buton[0].send_keys("senha")


    buton = driver.find_elements(By.ID,"btnContinuar")
    buton[0].click()

    time.sleep(1)

    buton = driver.find_elements(By.ID,"opcaoBoxNovoChamado")
    buton[0].click()

    buton = driver.find_elements(By.ID,"abrirSelecaoSolicitante")
    buton[0].click()

    wait = WebDriverWait(driver, 5)
    icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//th[@data-field='Login']//span[@class='k-icon k-filter']")))
    # Clica no ícone
    icon.click()
    time.sleep(5)

    buton = driver.find_element(By.XPATH, "/html/body/div[10]/form/div[1]/input")
    buton.send_keys("leoncio.faria")
    time.sleep(5)

    buton = driver.find_element(By.XPATH, "//button[@class='k-button k-primary']").click()

    icon = driver.find_element(By.XPATH, "//td//span[@class='k-icon k-i-tick']/parent::a")    
    icon.click()
    time.sleep(10)
    driver.quit()
    
    break