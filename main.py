from functions import ChamadoPassivo
from selenium import webdriver
import time


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def chamadopass(user):
    # Criar instância da classe e realizar o login
    c = ChamadoPassivo(driver)
    

    c.login()

    c.abertura_passivo(user)
    return c


chamadopass("jessica.alves")
# Fechar o navegador após a execução
driver.quit()