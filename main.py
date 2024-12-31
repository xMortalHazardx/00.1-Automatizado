from functions import ChamadoPassivo
from selenium import webdriver



options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

c = ChamadoPassivo(driver)


c.abertura_passivo("User")

# Fechar o navegador após a execução
driver.quit()